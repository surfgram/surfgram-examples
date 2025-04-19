from surfgram.types import InputPaidMediaVideo
from typing import Callable


class ExampleInputPaidMediaVideo(InputPaidMediaVideo):
    """Example implementation of InputPaidMediaVideo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_paid_media_video",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputPaidMediaVideo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the media, must be video
        - update.media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
        - update.thumbnail (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        - update.cover (str): Optional. Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
        - update.start_timestamp (int): Optional. Start timestamp for the video in the message
        - update.width (int): Optional. Video width
        - update.height (int): Optional. Video height
        - update.duration (int): Optional. Video duration in seconds
        - update.supports_streaming (bool): Optional. Pass True if the uploaded video is suitable for streaming
        """
        # Example implementation
        # Implement your handler logic here
        pass
