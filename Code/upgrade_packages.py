import subprocess, json

outdated_packages_json = subprocess.run(
    ["pip", "list", "--outdated", "--format=json"],
    capture_output=True,
    text=True
).stdout

packages = [pkg["name"] for pkg in json.loads(outdated_packages_json)]

for package in packages:
    subprocess.run(["pip", "install", "--upgrade", package], check=True)
