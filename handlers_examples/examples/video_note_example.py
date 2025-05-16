from surfgram.types import VideoNote
from typing import Callable


class ExampleVideoNote(VideoNote):
    """Example implementation of VideoNote handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_video_note",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the VideoNote event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.length (int): Video width and height (diameter of the video message) as defined by the sender
        - update.duration (int): Duration of the video in seconds as defined by the sender
        - update.thumbnail (PhotoSize): Optional. Video thumbnail
        - update.file_size (int): Optional. File size in bytes
        """
        # Example implementation
        # Implement your handler logic here
        pass
