from surfgram.types import InputStoryContentVideo
from typing import Callable


class ExampleInputStoryContentVideo(InputStoryContentVideo):
    """Example implementation of InputStoryContentVideo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_story_content_video",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputStoryContentVideo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the content, must be video
        - update.video (str): The video to post as a story. The video must be of the size 720x1280, streamable, encoded with H.265 codec, with key frames added each second in the MPEG4 format, and must not exceed 30 MB. The video can't be reused and can only be uploaded as a new file, so you can pass "attach://<file_attach_name>" if the video was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        - update.duration (float): Optional. Precise duration of the video in seconds; 0-60
        - update.cover_frame_timestamp (float): Optional. Timestamp in seconds of the frame that will be used as the static cover for the story. Defaults to 0.0.
        - update.is_animation (bool): Optional. Pass True if the video has no sound
        """
        # Example implementation
        # Implement your handler logic here
        pass
