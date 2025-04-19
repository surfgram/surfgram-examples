from surfgram.types import PassportElementErrorFiles
from typing import Callable


class ExamplePassportElementErrorFiles(PassportElementErrorFiles):
    """Example implementation of PassportElementErrorFiles handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_element_error_files",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportElementErrorFiles event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Error source, must be files
        - update.type (str): The section of the user's Telegram Passport which has the issue, one of "utility_bill", "bank_statement", "rental_agreement", "passport_registration", "temporary_registration"
        - update.file_hashes (List[str]): List of base64-encoded file hashes
        - update.message (str): Error message
        """
        # Example implementation
        # Implement your handler logic here
        pass
