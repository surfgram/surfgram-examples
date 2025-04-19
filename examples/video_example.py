from surfgram.types import Video
from typing import Callable


class ExampleVideo(Video):
    """Example implementation of Video handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_video",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Video event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.width (int): Video width as defined by the sender
        - update.height (int): Video height as defined by the sender
        - update.duration (int): Duration of the video in seconds as defined by the sender
        - update.thumbnail (PhotoSize): Optional. Video thumbnail
        - update.cover (List[PhotoSize]): Optional. Available sizes of the cover of the video in the message
        - update.start_timestamp (int): Optional. Timestamp in seconds from which the video will play in the message
        - update.file_name (str): Optional. Original filename as defined by the sender
        - update.mime_type (str): Optional. MIME type of the file as defined by the sender
        - update.file_size (int): Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
        """
        # Example implementation
        # Implement your handler logic here
        pass
