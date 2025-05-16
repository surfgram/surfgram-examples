from surfgram.types import VideoChatScheduled
from typing import Callable


class ExampleVideoChatScheduled(VideoChatScheduled):
    """Example implementation of VideoChatScheduled handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_video_chat_scheduled",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the VideoChatScheduled event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.start_date (int): Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator
        """
        # Example implementation
        # Implement your handler logic here
        pass
