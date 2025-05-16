from surfgram.types import PassportElementErrorUnspecified
from typing import Callable


class ExamplePassportElementErrorUnspecified(PassportElementErrorUnspecified):
    """Example implementation of PassportElementErrorUnspecified handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_element_error_unspecified",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportElementErrorUnspecified event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Error source, must be unspecified
        - update.type (str): Type of element of the user's Telegram Passport which has the issue
        - update.element_hash (str): Base64-encoded element hash
        - update.message (str): Error message
        """
        # Example implementation
        # Implement your handler logic here
        pass
