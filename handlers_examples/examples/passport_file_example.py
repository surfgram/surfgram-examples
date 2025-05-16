from surfgram.types import PassportFile
from typing import Callable


class ExamplePassportFile(PassportFile):
    """Example implementation of PassportFile handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_passport_file",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PassportFile event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.file_size (int): File size in bytes
        - update.file_date (int): Unix time when the file was uploaded
        """
        # Example implementation
        # Implement your handler logic here
        pass
