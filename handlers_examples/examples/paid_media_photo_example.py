from surfgram.types import PaidMediaPhoto
from typing import Callable


class ExamplePaidMediaPhoto(PaidMediaPhoto):
    """Example implementation of PaidMediaPhoto handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_paid_media_photo",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PaidMediaPhoto event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the paid media, always "photo"
        - update.photo (List[PhotoSize]): The photo
        """
        # Example implementation
        # Implement your handler logic here
        pass
