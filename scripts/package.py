"""Build focused archives from an explicit public-file allowlist."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
SKILL_FILES = (
    "SKILL.md", "agents/openai.yaml", "references/design-sources.md",
    "references/design-principles.md", "references/motion-guidelines.md",
    "references/implementation-workflow.md",
)


def package(output=None):
    output = Path(output) if output else ROOT / "dist"
    output.mkdir(parents=True, exist_ok=True)
    skill = [ROOT / "skills/ooh-shiny" / relative for relative in SKILL_FILES]
    shared = [ROOT / "LICENSE", *skill]
    plugin = shared + [ROOT / p for p in (
        "plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json",
        "README.md", "docs/installation.md", "docs/validation.md", "evals/scenarios.md")]
    built = []
    for kind, files in (("plugin", plugin), ("skill", shared)):
        destination = output / f"ooh-shiny-{kind}-{VERSION}.zip"
        with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
            for source in files:
                relative = source.relative_to(ROOT)
                if kind == "skill" and source in skill:
                    relative = source.relative_to(ROOT / "skills")
                archive.write(source, relative.as_posix())
        built.append(destination)
    (output / "SHA256SUMS.txt").write_text("".join(
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in built), encoding="utf-8")
    return built


if __name__ == "__main__":
    for archive in package():
        print(archive)
