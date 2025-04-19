from surfgram.types import StoryAreaPosition
from typing import Callable


class ExampleStoryAreaPosition(StoryAreaPosition):
    """Example implementation of StoryAreaPosition handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area_position",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryAreaPosition event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.x_percentage (float): The abscissa of the area's center, as a percentage of the media width
        - update.y_percentage (float): The ordinate of the area's center, as a percentage of the media height
        - update.width_percentage (float): The width of the area's rectangle, as a percentage of the media width
        - update.height_percentage (float): The height of the area's rectangle, as a percentage of the media height
        - update.rotation_angle (float): The clockwise rotation angle of the rectangle, in degrees; 0-360
        - update.corner_radius_percentage (float): The radius of the rectangle corner rounding, as a percentage of the media width
        """
        # Example implementation
        # Implement your handler logic here
        pass
