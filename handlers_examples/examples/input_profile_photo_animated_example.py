from surfgram.types import InputProfilePhotoAnimated
from typing import Callable


class ExampleInputProfilePhotoAnimated(InputProfilePhotoAnimated):
    """Example implementation of InputProfilePhotoAnimated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_profile_photo_animated",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputProfilePhotoAnimated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the profile photo, must be animated
        - update.animation (str): The animated profile photo. Profile photos can't be reused and can only be uploaded as a new file, so you can pass "attach://<file_attach_name>" if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        - update.main_frame_timestamp (float): Optional. Timestamp in seconds of the frame that will be used as the static profile photo. Defaults to 0.0.
        """
        # Example implementation
        # Implement your handler logic here
        pass
