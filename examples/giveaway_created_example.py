from surfgram.types import GiveawayCreated
from typing import Callable


class ExampleGiveawayCreated(GiveawayCreated):
    """Example implementation of GiveawayCreated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_giveaway_created",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the GiveawayCreated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.prize_star_count (int): Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
        """
        # Example implementation
        # Implement your handler logic here
        pass
