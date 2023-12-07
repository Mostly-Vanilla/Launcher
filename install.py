import minecraft_launcher_lib, webview, json, config, os, requests

# This script is used to manage both the modpack and the launcher installation and updates.

mrpack_path = config.appPath + "\\"+ config.modpackSlug + "-" + config.modpackVersion + ".mrpack"
minecraft_path = os.getenv('APPDATA') + "\\.minecraft"
modpack_path = config.appPath + "\\" +config.modpackSlug


def packInstall():
    minecraft_launcher_lib.mrpack.install_mrpack(path=mrpack_path, minecraft_directory=minecraft_path, modpack_directory=modpack_path)
    return True

def downloadPack(url):
    if os.path.exists(mrpack_path):
        os.remove(mrpack_path)
    os.makedirs(config.appPath, exist_ok=True)
    response = requests.get(url, stream=True)
    with open(mrpack_path, 'wb') as handle:
        for data in response.iter_content():
            handle.write(data)
    return True

if downloadPack("https://cdn.modrinth.com/data/JAJzedIU/versions/P47lwuuz/Mostly%20Vanilla%20Client%201.2.0.mrpack"):
    print("Downloaded pack")
if packInstall():
    print("Installed pack")