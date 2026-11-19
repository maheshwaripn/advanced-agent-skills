"""Check the promoted catalog and exercise the installer in temporary directories."""
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def catalog():
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    require(market["plugins"][0]["name"] == plugin["name"], "Marketplace name mismatch")
    files = sorted(path for bucket in ("engineering", "productivity")
                   for path in (ROOT / "skills" / bucket).glob("*/SKILL.md"))
    paths = ["./" + str(path.parent.relative_to(ROOT)) for path in files]
    require(bool(paths) and sorted(plugin["skills"]) == sorted(paths), "Catalog mismatch")
    names = set()
    index = (ROOT / "README.md").read_text()
    for path in files:
        folder = path.parent
        name = folder.name
        require(name not in names, f"Duplicate skill {name}")
        names.add(name)
        _, meta, body = path.read_text().split("---", 2)
        require(re.search(rf"^name: {re.escape(name)}$", meta, re.M), f"Bad name in {path}")
        require(re.search(r"^description: .+", meta, re.M) and body.strip(), f"Incomplete {path}")
        require(str(path.relative_to(ROOT)) in index, f"Missing index entry {name}")
        require(f"{name}/SKILL.md" in (folder.parent / "README.md").read_text(), f"Bucket index {name}")
        require((ROOT / "docs" / folder.parent.name / (name + ".md")).is_file(), f"Missing docs {name}")
        policy = folder / "agents/openai.yaml"
        explicit = policy.exists() and "allow_implicit_invocation: false" in policy.read_text()
        require(explicit == ("disable-model-invocation: true" in meta), f"Invocation mismatch {name}")
    return names


def test_install(names):
    with TemporaryDirectory() as temp:
        dest = Path(temp)
        cmd = ["bash", str(ROOT / "scripts/link-skills.sh"), temp]
        conflict = dest / "tdd"
        conflict.mkdir()
        marker = conflict / "personal.md"
        marker.write_text("keep")
        result = subprocess.run(cmd, capture_output=True)
        require(result.returncode != 0 and marker.read_text() == "keep", "Conflict handling failed")
        require(list(dest.iterdir()) == [conflict], "Partial install after conflict")
        marker.unlink()
        conflict.rmdir()
        for _ in range(2):
            subprocess.run(cmd, check=True)
        require({p.name for p in dest.iterdir()} == names, "Installed set mismatch")
        for link in dest.iterdir():
            require(link.is_symlink() and (link / "SKILL.md").is_file(), f"Broken link {link}")


if __name__ == "__main__":
    names = catalog()
    test_install(names)
    print(f"Verified {len(names)} promoted skills, conflict preservation, installation and repeat installation.")
