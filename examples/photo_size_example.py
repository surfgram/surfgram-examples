from surfgram.types import PhotoSize
from typing import Callable


class ExamplePhotoSize(PhotoSize):
    """Example implementation of PhotoSize handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_photo_size",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PhotoSize event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.width (int): Photo width
        - update.height (int): Photo height
        - update.file_size (int): Optional. File size in bytes
        """
        # Example implementation
        # Implement your handler logic here
        pass
