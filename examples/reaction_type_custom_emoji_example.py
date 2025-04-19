from surfgram.types import ReactionTypeCustomEmoji
from typing import Callable


class ExampleReactionTypeCustomEmoji(ReactionTypeCustomEmoji):
    """Example implementation of ReactionTypeCustomEmoji handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_reaction_type_custom_emoji",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ReactionTypeCustomEmoji event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the reaction, always "custom_emoji"
        - update.custom_emoji_id (str): Custom emoji identifier
        """
        # Example implementation
        # Implement your handler logic here
        pass
