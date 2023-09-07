const CONFIG = require('../../modpack.json');
const slug = CONFIG.modpackSlug;
const version = CONFIG.modpackVersion;
const UA = CONFIG.modrinthUserAgent;
const themes = CONFIG.themes;

function loadTheme(themeName){
    themes.forEach(theme => {
        if(theme.name == themeName){
            var root = document.querySelector(":root");
            root.style.setProperty('--primary-color', theme.primaryColor);
            root.style.setProperty('--secondary-color', theme.secondaryColor);
            root.style.setProperty('--tertiary-color', theme.tertiaryColor);
        }
    });
}