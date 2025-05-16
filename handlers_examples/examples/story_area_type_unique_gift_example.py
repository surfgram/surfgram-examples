from surfgram.types import StoryAreaTypeUniqueGift
from typing import Callable


class ExampleStoryAreaTypeUniqueGift(StoryAreaTypeUniqueGift):
    """Example implementation of StoryAreaTypeUniqueGift handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area_type_unique_gift",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryAreaTypeUniqueGift event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the area, always "unique_gift"
        - update.name (str): Unique name of the gift
        """
        # Example implementation
        # Implement your handler logic here
        pass
