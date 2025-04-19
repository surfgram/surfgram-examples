from surfgram.types import StoryAreaTypeLink
from typing import Callable


class ExampleStoryAreaTypeLink(StoryAreaTypeLink):
    """Example implementation of StoryAreaTypeLink handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area_type_link",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryAreaTypeLink event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the area, always "link"
        - update.url (str): HTTP or tg:// URL to be opened when the area is clicked
        """
        # Example implementation
        # Implement your handler logic here
        pass
