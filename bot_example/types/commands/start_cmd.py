from surfgram.types import BotCommand
from bot_example.types.keyboards import PressMeKeyboard
from typing import Callable


class StartCommand(BotCommand):
    @property
    def __names__(self):
        return ["start"]

    @property
    def __callback__(self) -> Callable:
        return self.handle

    async def handle(self, update, bot):
        await bot.send_message(
            chat_id=update.message.chat.id,
            text="Hello, World! Press the button!",
            reply_markup=PressMeKeyboard(),
        )
