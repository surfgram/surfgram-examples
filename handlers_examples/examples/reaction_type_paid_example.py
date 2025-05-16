from surfgram.types import ReactionTypePaid
from typing import Callable


class ExampleReactionTypePaid(ReactionTypePaid):
    """Example implementation of ReactionTypePaid handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_reaction_type_paid",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ReactionTypePaid event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the reaction, always "paid"
        """
        # Example implementation
        # Implement your handler logic here
        pass
