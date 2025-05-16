from surfgram.types import StoryAreaTypeLocation
from typing import Callable


class ExampleStoryAreaTypeLocation(StoryAreaTypeLocation):
    """Example implementation of StoryAreaTypeLocation handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area_type_location",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryAreaTypeLocation event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the area, always "location"
        - update.latitude (float): Location latitude in degrees
        - update.longitude (float): Location longitude in degrees
        - update.address (LocationAddress): Optional. Address of the location
        """
        # Example implementation
        # Implement your handler logic here
        pass
