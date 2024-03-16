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
    USER_SESSION_STRING = ("BAF4f7kACJSU0Rqn2xWUz5NR9oTLraTXyqCgmLq1o9mF1R7AhxWdo1nJI38UO4rCTwKQ4Z4AI2Ys3Js4Sa9NrsG51V4YFog0BeUa-B2-Q-BWGlIl93NgUV1o10finQ8RplfsCgZOSvlK30wSOLEv9auC95oLUafmwWMNnckHgYVCWfxGMIrqM-WaXd9sJ67CMAWsK1x0NCvUC8IMMcdaBJQagaCxafG0RB1pusOVbx0Sq6XHNpJ59OBeIQqWpjl75Dza5gxFVftMsdnDpBEhjE-7r1X1SiSQP4GHYap7z_2dnpOKJeP0JpeNSF9xvV9gsdyhaTofkznfTSfuunnWAXJhankJhQAAAAFwDOYhAA")
    IS_PREMIUM = True
    START_PIC = ("https://graph.org/file/6b56e482d9865a49ed578.jpg")
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
