from surfgram.types import StoryArea
from typing import Callable


class ExampleStoryArea(StoryArea):
    """Example implementation of StoryArea handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryArea event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.position (Union[St, yAreaPosition]): Position of the area
        - update.type (Union[St, yAreaType]): Type of the area
        """
        # Example implementation
        # Implement your handler logic here
        pass
