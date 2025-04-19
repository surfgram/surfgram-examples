from surfgram.types import PaidMediaVideo
from typing import Callable


class ExamplePaidMediaVideo(PaidMediaVideo):
    """Example implementation of PaidMediaVideo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_paid_media_video",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PaidMediaVideo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the paid media, always "video"
        - update.video (Video): The video
        """
        # Example implementation
        # Implement your handler logic here
        pass
