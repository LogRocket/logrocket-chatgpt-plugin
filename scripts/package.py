"""Build the plugin ZIP from an explicit inventory of plugin files plus the repository license."""
import json
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
package = root / "plugins/logrocket"
manifest = json.loads((package / "plugin.json").read_text())
output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / "dist" / f"logrocket-{manifest['version']}.zip"
if output.is_relative_to(package):
    raise SystemExit("Write the archive outside the plugin directory")
sources = {
    name: package / name
    for name in ["plugin.json", "mcp.json", "README.md", "assets/logo.png", "skills/use-logrocket/SKILL.md"]
}
sources["LICENSE"] = root / "LICENSE"
files = list(sources)
for name, path in sources.items():
    if path.is_symlink() or not path.is_file():
        raise SystemExit(f"Missing or symlinked component: {name}")
output.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for name, path in sources.items():
        archive.write(path, name)
with ZipFile(output) as archive:
    if archive.testzip() is not None or set(archive.namelist()) != set(files):
        raise SystemExit("Archive verification failed")
    for name in ("plugin.json", "mcp.json"):
        json.loads(archive.read(name))
print(output)
