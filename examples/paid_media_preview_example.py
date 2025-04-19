from surfgram.types import PaidMediaPreview
from typing import Callable


class ExamplePaidMediaPreview(PaidMediaPreview):
    """Example implementation of PaidMediaPreview handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_paid_media_preview",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PaidMediaPreview event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the paid media, always "preview"
        - update.width (int): Optional. Media width as defined by the sender
        - update.height (int): Optional. Media height as defined by the sender
        - update.duration (int): Optional. Duration of the media in seconds as defined by the sender
        """
        # Example implementation
        # Implement your handler logic here
        pass
