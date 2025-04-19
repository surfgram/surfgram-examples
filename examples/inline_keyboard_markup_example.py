from surfgram.types import InlineKeyboardMarkup
from typing import Callable


class ExampleInlineKeyboardMarkup(InlineKeyboardMarkup):
    """Example implementation of InlineKeyboardMarkup handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_keyboard_markup",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineKeyboardMarkup event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.inline_keyboard (List[InlineKeyboardButton]): Array of button rows, each represented by an Array of InlineKeyboardButton objects
        """
        # Example implementation
        # Implement your handler logic here
        pass
