from surfgram.types import ReactionTypeEmoji
from typing import Callable


class ExampleReactionTypeEmoji(ReactionTypeEmoji):
    """Example implementation of ReactionTypeEmoji handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_reaction_type_emoji",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ReactionTypeEmoji event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the reaction, always "emoji"
        - update.emoji (str): Reaction emoji. Currently, it can be one of "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        """
        # Example implementation
        # Implement your handler logic here
        pass
