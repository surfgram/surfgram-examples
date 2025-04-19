from surfgram.types import File
from typing import Callable


class ExampleFile(File):
    """Example implementation of File handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_file",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the File event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.file_size (int): Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
        - update.file_path (str): Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
        """
        # Example implementation
        # Implement your handler logic here
        pass
