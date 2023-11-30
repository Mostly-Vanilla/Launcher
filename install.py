import minecraft_launcher_lib, webview, json, config, os

# This script is used to manage both the modpack and the launcher installation and updates.

mrpack_path = config.appPath + config.modpackSlug + "-" + config.modpackVersion + ".mrpack"
minecraft_path = os.getenv('APPDATA') + "\.minecraft"
modpack_path = config.appPath + config.modpackSlug


def getPack():

    return mrpack

def packInstall():
    minecraft_launcher_lib.mrpack.install_mrpack(path=mrpack_path, minecraft_directory=minecraft_path, modpack_directory=modpack_path)
