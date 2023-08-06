const {app, BrowserWindow} = require('electron')
const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        resizable: false,
        webPreferences: {
        nodeIntegration: true
        },
        icon: __dirname + '/icon.png'
    });
    win.loadFile('index.html');
}

app.on('ready', createWindow);

var CONFIG = require('./modpack.json');
var slug = CONFIG.modpackSlug;
var version = CONFIG.modpackVersion;

var minecraft = CONFIG.MCVersion;
var loader = CONFIG.modloader;
var loaderVersion = CONFIG.modloaderVersion; 

var theme = CONFIG.theme;
var primaryColour = CONFIG.primaryColour;
var secondaryColour = CONFIG.secondaryColour;

function update(){
    
}