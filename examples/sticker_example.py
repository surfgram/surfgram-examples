from surfgram.types import Sticker
from typing import Callable


class ExampleSticker(Sticker):
    """Example implementation of Sticker handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_sticker",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Sticker event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.file_id (str): Identifier for this file, which can be used to download or reuse the file
        - update.file_unique_id (str): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        - update.type (str): Type of the sticker, currently one of "regular", "mask", "custom_emoji". The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video.
        - update.width (int): Sticker width
        - update.height (int): Sticker height
        - update.is_animated (bool): True, if the sticker is animated
        - update.is_video (bool): True, if the sticker is a video sticker
        - update.thumbnail (PhotoSize): Optional. Sticker thumbnail in the .WEBP or .JPG format
        - update.emoji (str): Optional. Emoji associated with the sticker
        - update.set_name (str): Optional. Name of the sticker set to which the sticker belongs
        - update.premium_animation (File): Optional. For premium regular stickers, premium animation for the sticker
        - update.mask_position (MaskPosition): Optional. For mask stickers, the position where the mask should be placed
        - update.custom_emoji_id (str): Optional. For custom emoji stickers, unique identifier of the custom emoji
        - update.needs_repainting (bool): Optional. True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places
        - update.file_size (int): Optional. File size in bytes
        """
        # Example implementation
        # Implement your handler logic here
        pass
