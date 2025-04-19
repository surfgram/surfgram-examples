from surfgram.types import ReactionCount
from typing import Callable


class ExampleReactionCount(ReactionCount):
    """Example implementation of ReactionCount handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_reaction_count",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ReactionCount event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (ReactionType): Type of the reaction
        - update.total_count (int): Number of times the reaction was added
        """
        # Example implementation
        # Implement your handler logic here
        pass
