from surfgram.types import KeyboardButtonPollType
from typing import Callable


class ExampleKeyboardButtonPollType(KeyboardButtonPollType):
    """Example implementation of KeyboardButtonPollType handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_keyboard_button_poll_type",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the KeyboardButtonPollType event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
        """
        # Example implementation
        # Implement your handler logic here
        pass
