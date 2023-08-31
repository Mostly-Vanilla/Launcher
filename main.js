var CONFIG = require('./modpack.json');
var slug = CONFIG.modpackSlug;
var version = CONFIG.modpackVersion;
var UA = CONFIG.modrinthUserAgent;

var theme = CONFIG.theme;
var primaryColour = CONFIG.primaryColour;
var secondaryColour = CONFIG.secondaryColour;

const shell = require('electron').shell;


const {app, BrowserWindow} = require('electron')
const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        resizable: false,
        webPreferences: {
        nodeIntegration: true
        },
        icon: __dirname + '/assets/textures/icon.png'
    });
    win.loadFile('index.html');
    win.webContents.setWindowOpenHandler(({ url }) => {
        shell.openExternal(url);
        return { action: 'deny' };
      });
}

app.on('ready', createWindow);
app.on("activate", createWindow);



function update(){
    
}