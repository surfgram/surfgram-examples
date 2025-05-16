from surfgram.types import PassportElementErrorDataField
from typing import Callable


class ExamplePassportElementErrorDataField(PassportElementErrorDataField):
    """Example implementation of PassportElementErrorDataField handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_element_error_data_field",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportElementErrorDataField event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Error source, must be data
        - update.type (str): The section of the user's Telegram Passport which has the error, one of "personal_details", "passport", "driver_license", "identity_card", "internal_passport", "address"
        - update.field_name (str): Name of the data field which has the error
        - update.data_hash (str): Base64-encoded data hash
        - update.message (str): Error message
        """
        # Example implementation
        # Implement your handler logic here
        pass
