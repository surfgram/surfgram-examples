from surfgram.types import PassportData
from typing import Callable


class ExamplePassportData(PassportData):
    """Example implementation of PassportData handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_data",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportData event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.data (List[Union[EncryptedPassp, tElement]]): Array with information about documents and other Telegram Passport elements that was shared with the bot
        - update.credentials (EncryptedCredentials): Encrypted credentials required to decrypt the data
        """
        # Example implementation
        # Implement your handler logic here
        pass
