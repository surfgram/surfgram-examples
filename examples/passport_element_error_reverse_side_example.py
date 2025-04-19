from surfgram.types import PassportElementErrorReverseSide
from typing import Callable


class ExamplePassportElementErrorReverseSide(PassportElementErrorReverseSide):
    """Example implementation of PassportElementErrorReverseSide handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_element_error_reverse_side",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportElementErrorReverseSide event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Error source, must be reverse_side
        - update.type (str): The section of the user's Telegram Passport which has the issue, one of "driver_license", "identity_card"
        - update.file_hash (str): Base64-encoded hash of the file with the reverse side of the document
        - update.message (str): Error message
        """
        # Example implementation
        # Implement your handler logic here
        pass
