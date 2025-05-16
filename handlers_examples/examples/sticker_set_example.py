from surfgram.types import StickerSet
from typing import Callable


class ExampleStickerSet(StickerSet):
    """Example implementation of StickerSet handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_sticker_set",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StickerSet event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): Sticker set name
        - update.title (str): Sticker set title
        - update.sticker_type (str): Type of stickers in the set, currently one of "regular", "mask", "custom_emoji"
        - update.stickers (List[Sticker]): List of all set stickers
        - update.thumbnail (PhotoSize): Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
        """
        # Example implementation
        # Implement your handler logic here
        pass
