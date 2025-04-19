from surfgram.types import StoryAreaTypeWeather
from typing import Callable


class ExampleStoryAreaTypeWeather(StoryAreaTypeWeather):
    """Example implementation of StoryAreaTypeWeather handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area_type_weather",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryAreaTypeWeather event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the area, always "weather"
        - update.temperature (float): Temperature, in degree Celsius
        - update.emoji (str): Emoji representing the weather
        - update.background_color (int): A color of the area background in the ARGB format
        """
        # Example implementation
        # Implement your handler logic here
        pass
