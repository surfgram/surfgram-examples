from surfgram.types import InputSticker
from typing import Callable


class ExampleInputSticker(InputSticker):
    """Example implementation of InputSticker handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_sticker",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputSticker event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.sticker (str): The added sticker. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new file using multipart/form-data under <file_attach_name> name. Animated and video stickers can't be uploaded via HTTP URL. More information on Sending Files »
        - update.format (str): Format of the added sticker, must be one of "static" for a .WEBP or .PNG image, "animated" for a .TGS animation, "video" for a .WEBM video
        - update.emoji_list (List[str]): List of 1-20 emoji associated with the sticker
        - update.mask_position (MaskPosition): Optional. Position where the mask should be placed on faces. For "mask" stickers only.
        - update.keywords (List[str]): Optional. List of 0-20 search keywords for the sticker with total length of up to 64 characters. For "regular" and "custom_emoji" stickers only.
        """
        # Example implementation
        # Implement your handler logic here
        pass
