from surfgram.types import ChatPhoto
from typing import Callable


class ExampleChatPhoto(ChatPhoto):
    """Example implementation of ChatPhoto handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_photo",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatPhoto event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.small_file_id (str): File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
        - update.small_file_unique_id (str): Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.big_file_id (str): File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
        - update.big_file_unique_id (str): Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        """
        # Example implementation
        # Implement your handler logic here
        pass
