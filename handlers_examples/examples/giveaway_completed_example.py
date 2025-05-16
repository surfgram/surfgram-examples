from surfgram.types import GiveawayCompleted
from typing import Callable


class ExampleGiveawayCompleted(GiveawayCompleted):
    """Example implementation of GiveawayCompleted handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_giveaway_completed",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the GiveawayCompleted event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.winner_count (int): Number of winners in the giveaway
        - update.unclaimed_prize_count (int): Optional. Number of undistributed prizes
        - update.giveaway_message (Message): Optional. Message with the giveaway that was completed, if it wasn't deleted
        - update.is_star_giveaway (bool): Optional. True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.
        """
        # Example implementation
        # Implement your handler logic here
        pass
