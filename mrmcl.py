import webview, sys, subprocess, minecraft_launcher_lib

window = webview.create_window('Minecraft Launcher', 'index.html', width=800, height=600, resizable=False, fullscreen=False)
webview.start(http_server=True)

    