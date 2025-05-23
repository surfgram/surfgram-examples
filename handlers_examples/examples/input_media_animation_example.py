from surfgram.types import InputMediaAnimation
from typing import Callable


class ExampleInputMediaAnimation(InputMediaAnimation):
    """Example implementation of InputMediaAnimation handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_media_animation",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputMediaAnimation event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be animation
        - update.media (str): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More information on Sending Files »
        - update.thumbnail (str): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More information on Sending Files »
        - update.caption (str): Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.width (int): Optional. Animation width
        - update.height (int): Optional. Animation height
        - update.duration (int): Optional. Animation duration in seconds
        - update.has_spoiler (bool): Optional. Pass True if the animation needs to be covered with a spoiler animation
        """
        # Example implementation
        # Implement your handler logic here
        pass
