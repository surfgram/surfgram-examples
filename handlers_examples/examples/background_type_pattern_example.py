from surfgram.types import BackgroundTypePattern
from typing import Callable


class ExampleBackgroundTypePattern(BackgroundTypePattern):
    """Example implementation of BackgroundTypePattern handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_type_pattern",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundTypePattern event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background, always "pattern"
        - update.document (Document): Document with the pattern
        - update.fill (BackgroundFill): The background fill that is combined with the pattern
        - update.intensity (int): Intensity of the pattern when it is shown above the filled background; 0-100
        - update.is_inverted (bool): Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only
        - update.is_moving (bool): Optional. True, if the background moves slightly when the device is tilted
        """
        # Example implementation
        # Implement your handler logic here
        pass
