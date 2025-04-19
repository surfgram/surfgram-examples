from surfgram.types import PassportElementErrorSelfie
from typing import Callable


class ExamplePassportElementErrorSelfie(PassportElementErrorSelfie):
    """Example implementation of PassportElementErrorSelfie handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_element_error_selfie",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportElementErrorSelfie event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Error source, must be selfie
        - update.type (str): The section of the user's Telegram Passport which has the issue, one of "passport", "driver_license", "identity_card", "internal_passport"
        - update.file_hash (str): Base64-encoded hash of the file with the selfie
        - update.message (str): Error message
        """
        # Example implementation
        # Implement your handler logic here
        pass
