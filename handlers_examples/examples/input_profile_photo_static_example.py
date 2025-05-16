from surfgram.types import InputProfilePhotoStatic
from typing import Callable


class ExampleInputProfilePhotoStatic(InputProfilePhotoStatic):
    """Example implementation of InputProfilePhotoStatic handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_profile_photo_static",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputProfilePhotoStatic event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the profile photo, must be static
        - update.photo (str): The static profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass "attach://<file_attach_name>" if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        """
        # Example implementation
        # Implement your handler logic here
        pass
