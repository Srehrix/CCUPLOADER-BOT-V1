
# (c) Shrimadhav U K | Modifieded By @LISA_FAN_LK

import os
from config import Config, PORT
from pyrogram import Client as Clinton
from aiohttp import web
from plugins import web_server


if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@UploadLinkToFileBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
    
app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
