from surfgram.types import InlineQueryResultGame
from typing import Callable


class ExampleInlineQueryResultGame(InlineQueryResultGame):
    """Example implementation of InlineQueryResultGame handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_game",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultGame event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be game
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.game_short_name (str): Short name of the game
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        """
        # Example implementation
        # Implement your handler logic here
        pass
