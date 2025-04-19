from surfgram.types import Giveaway
from typing import Callable


class ExampleGiveaway(Giveaway):
    """Example implementation of Giveaway handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_giveaway",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Giveaway event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chats (List[Chat]): The list of chats which the user must join to participate in the giveaway
        - update.winners_selection_date (int): Point in time (Unix timestamp) when winners of the giveaway will be selected
        - update.winner_count (int): The number of users which are supposed to be selected as winners of the giveaway
        - update.only_new_members (bool): Optional. True, if only users who join the chats after the giveaway started should be eligible to win
        - update.has_public_winners (bool): Optional. True, if the list of giveaway winners will be visible to everyone
        - update.prize_description (str): Optional. Description of additional giveaway prize
        - update.country_codes (List[str]): Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.
        - update.prize_star_count (int): Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
        - update.premium_subscription_month_count (int): Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only
        """
        # Example implementation
        # Implement your handler logic here
        pass
