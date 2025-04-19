from surfgram.types import BackgroundTypeWallpaper
from typing import Callable


class ExampleBackgroundTypeWallpaper(BackgroundTypeWallpaper):
    """Example implementation of BackgroundTypeWallpaper handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_type_wallpaper",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundTypeWallpaper event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background, always "wallpaper"
        - update.document (Document): Document with the wallpaper
        - update.dark_theme_dimming (int): Dimming of the background in dark themes, as a percentage; 0-100
        - update.is_blurred (bool): Optional. True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12
        - update.is_moving (bool): Optional. True, if the background moves slightly when the device is tilted
        """
        # Example implementation
        # Implement your handler logic here
        pass
