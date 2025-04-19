from surfgram.types import Document
from typing import Callable


class ExampleDocument(Document):
    """Example implementation of Document handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_document",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Document event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.thumbnail (PhotoSize): Optional. Document thumbnail as defined by the sender
        - update.file_name (str): Optional. Original filename as defined by the sender
        - update.mime_type (str): Optional. MIME type of the file as defined by the sender
        - update.file_size (int): Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
        """
        # Example implementation
        # Implement your handler logic here
        pass
