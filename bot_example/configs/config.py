from surfgram import configs
from surfgram import listeners
import os
from dotenv import load_dotenv

load_dotenv()


class Config(configs.BaseConfig):
    __bot_token__ = os.getenv("BOT_TOKEN")
    __listener__ = listeners.BaseListener
