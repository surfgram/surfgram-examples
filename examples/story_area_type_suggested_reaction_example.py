from surfgram.types import StoryAreaTypeSuggestedReaction
from typing import Callable


class ExampleStoryAreaTypeSuggestedReaction(StoryAreaTypeSuggestedReaction):
    """Example implementation of StoryAreaTypeSuggestedReaction handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story_area_type_suggested_reaction",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StoryAreaTypeSuggestedReaction event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the area, always "suggested_reaction"
        - update.reaction_type (ReactionType): Type of the reaction
        - update.is_dark (bool): Optional. Pass True if the reaction area has a dark background
        - update.is_flipped (bool): Optional. Pass True if reaction area corner is flipped
        """
        # Example implementation
        # Implement your handler logic here
        pass
