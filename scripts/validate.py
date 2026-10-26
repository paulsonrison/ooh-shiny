"""Validate metadata, reference containment, and distributable contents."""
import json
import re
import tempfile
from pathlib import Path
from zipfile import ZipFile
from unittest.mock import patch
import yaml
from jsonschema import Draft202012Validator
from package import ROOT, SKILL_FILES, package


def validate():
    schema = json.loads((ROOT / "scripts/plugin.schema.json").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(manifest)
    for file in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        data = json.loads((ROOT / file).read_text(encoding="utf-8"))
        assert data["name"] == manifest["name"] and data["version"] == manifest["version"]
    for file in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
        data = json.loads((ROOT / file).read_text(encoding="utf-8"))
        assert any(p["name"] == manifest["name"] for p in data["plugins"])
    skill = ROOT / "skills/ooh-shiny"
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["name"] == skill.name
    assert metadata["description"] and len(metadata["description"]) <= 1024
    ui = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
    assert 25 <= len(ui["interface"]["short_description"]) <= 64
    assert "$ooh-shiny" in ui["interface"]["default_prompt"]
    assert ui["policy"]["allow_implicit_invocation"] is True
    links = 0
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts or "dist" in document.parts:
            continue
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (document.parent / target.split("#")[0]).resolve()
            assert resolved.is_relative_to(ROOT) and resolved.exists(), (document, target)
            links += 1
    with tempfile.TemporaryDirectory() as temporary:
        archives = package(temporary)
        for path in archives:
            with ZipFile(path) as archive:
                assert archive.testzip() is None
                names = set(archive.namelist())
                assert not any(n.startswith("/") or ".." in Path(n).parts or ".git/" in n for n in names)
                assert "LICENSE" in names
                expected_skill = {("ooh-shiny/" if "-skill-" in path.name else "skills/ooh-shiny/") + n for n in SKILL_FILES}
                if "-skill-" in path.name:
                    assert names == expected_skill | {"LICENSE"}
                else:
                    assert {n for n in names if n.startswith("skills/")} == expected_skill
                entry = "ooh-shiny/SKILL.md" if "-skill-" in path.name else "skills/ooh-shiny/SKILL.md"
                assert archive.read(entry) == (skill / "SKILL.md").read_bytes()
                for source in (skill / "references").glob("*.md"):
                    expected = ("ooh-shiny/references/" if "-skill-" in path.name else "skills/ooh-shiny/references/") + source.name
                    assert archive.read(expected) == source.read_bytes()
        plugin_files = set(ZipFile(archives[0]).namelist())
        assert {"plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"} <= plugin_files
        fixture = Path(temporary) / "fixture"
        with ZipFile(archives[0]) as archive:
            archive.extractall(fixture)
        (fixture / "skills/ooh-shiny/private-note.txt").write_text("not for distribution", encoding="utf-8")
        with patch("package.ROOT", fixture):
            contaminated = package(Path(temporary) / "contaminated")
        for path in contaminated:
            with ZipFile(path) as archive:
                assert not any("private-note" in name for name in archive.namelist())
    print(f"PASS: portable schema, 2 host manifests, 2 marketplaces, skill/UI metadata, {links} local links, both archive layouts, shared-source parity, exclusion of unlisted private files")


if __name__ == "__main__":
    validate()
