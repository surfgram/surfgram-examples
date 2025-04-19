from surfgram.types import VideoChatEnded
from typing import Callable


class ExampleVideoChatEnded(VideoChatEnded):
    """Example implementation of VideoChatEnded handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_video_chat_ended",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the VideoChatEnded event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.duration (int): Video chat duration in seconds
        """
        # Example implementation
        # Implement your handler logic here
        pass
