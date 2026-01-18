# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

    if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count(":") == 1:
        print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
        exit(1)

    if (
        not getenv("SESSION_STRING")
        or getenv("SESSION_STRING") == "xxxxxxxxxxxxxxxxxxxxxxx"
    ):
        print("Error: SESSION_STRING must be set with a valid string")
        exit(1)


# Pyrogram setup
class PyroConf(object):
    API_ID = int(getenv("API_ID", "26357539"))
    API_HASH = getenv("API_HASH", "09ad257e2c2bc27f541f0464cf6f2976")
    BOT_TOKEN = getenv("8262726640:AAH_4LZ2HomteyM-J67itE_P31o6SITLN4k")
    SESSION_STRING = getenv("BQGSLyMAtcVPxPRtQDA_JwnZooAhEkDR2SxKSo4gNPy-GYXojaFgdTFz2Qjl-65Ns_0QEzAHLXmMDtOX-cLqXCywF05D9YQzvBWOA3OhB31HNsL3ruiTahX718rYKY2H_wd58leFyo3Gynxpu0hqlV_Dxkrz9U6rHETHl3gcmxofkBPGcLS6PzlQ6ORr-DNFZqXNYmuq7UPpSGFNBihO7WUX1XW4E4mImOTFJazY-kXnBbdGBYVz4sxAhhjDVWot3y-UyaFZZbWWEj3YQtWV-3Dum3n-znAxKkjEABAWuL8xaC2Gz_OSasQxVMzlIWRHOJzhludJGPLS2yZ0jve_jMYduSFK7QAAAAHxl_zaAA")
    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = int(getenv("MAX_CONCURRENT_DOWNLOADS", "3"))
    BATCH_SIZE = int(getenv("BATCH_SIZE", "100"))
    FLOOD_WAIT_DELAY = int(getenv("FLOOD_WAIT_DELAY", "3"))
