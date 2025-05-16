from surfgram.types import InputStoryContentPhoto
from typing import Callable


class ExampleInputStoryContentPhoto(InputStoryContentPhoto):
    """Example implementation of InputStoryContentPhoto handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_story_content_photo",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputStoryContentPhoto event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the content, must be photo
        - update.photo (str): The photo to post as a story. The photo must be of the size 1080x1920 and must not exceed 10 MB. The photo can't be reused and can only be uploaded as a new file, so you can pass "attach://<file_attach_name>" if the photo was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        """
        # Example implementation
        # Implement your handler logic here
        pass
