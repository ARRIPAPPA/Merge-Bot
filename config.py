import os


class Config(object):
    API_HASH =("d8c9b01c863dabacc484c2c06cdd0f6e")
    BOT_TOKEN = ("5932926601:AAHVnnl6kNepzUGkmxnMzMeu1P9jFPUsusk")
    TELEGRAM_API = ("16501053")
    OWNER = ("5422016608")
    OWNER_USERNAME = ("None")
    PASSWORD = ("blaster")
    DATABASE_URL = ("mongodb+srv://animesaga:animesagas@cluster0.lkpnvsw.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = ("-1001736029601")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING")
    IS_PREMIUM = False
    START_PIC = ("https://graph.org/file/6b56e482d9865a49ed578.jpg")
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
