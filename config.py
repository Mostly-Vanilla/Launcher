import json

modpackconf = json.load(open("modpack.json"))
appconf = json.load(open("launcher.json.json"))
userdata = json.load(open("userdata.json"))

modpackVersion = modpackconf["modpackVersion"]
modpackSlug = modpackconf["modpackSlug"]
modrinthUserAgent = modpackconf["modrinthUserAgent"]
version_override = modpackconf["version override"]
defaultTheme = modpackconf["defaultTheme"]
themes = modpackconf["themes"]

isInitialised = appconf["isInitialised"]
appPath = appconf["appPath"]



