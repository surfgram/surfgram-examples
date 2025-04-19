from surfgram.types import InputMediaVideo
from typing import Callable


class ExampleInputMediaVideo(InputMediaVideo):
    """Example implementation of InputMediaVideo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_media_video",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputMediaVideo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be video
        - update.media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
        - update.thumbnail (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        - update.cover (str): Optional. Cover for the video in the message. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
        - update.start_timestamp (int): Optional. Start timestamp for the video in the message
        - update.caption (str): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the video caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.width (int): Optional. Video width
        - update.height (int): Optional. Video height
        - update.duration (int): Optional. Video duration in seconds
        - update.supports_streaming (bool): Optional. Pass True if the uploaded video is suitable for streaming
        - update.has_spoiler (bool): Optional. Pass True if the video needs to be covered with a spoiler animation
        """
        # Example implementation
        # Implement your handler logic here
        pass
