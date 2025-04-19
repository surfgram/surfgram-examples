from surfgram.types import InputPaidMediaPhoto
from typing import Callable


class ExampleInputPaidMediaPhoto(InputPaidMediaPhoto):
    """Example implementation of InputPaidMediaPhoto handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_paid_media_photo",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputPaidMediaPhoto event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the media, must be photo
        - update.media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
        """
        # Example implementation
        # Implement your handler logic here
        pass
