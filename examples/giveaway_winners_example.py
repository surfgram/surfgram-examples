from surfgram.types import GiveawayWinners
from typing import Callable


class ExampleGiveawayWinners(GiveawayWinners):
    """Example implementation of GiveawayWinners handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_giveaway_winners",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the GiveawayWinners event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): The chat that created the giveaway
        - update.giveaway_message_id (int): Identifier of the message with the giveaway in the chat
        - update.winners_selection_date (int): Point in time (Unix timestamp) when winners of the giveaway were selected
        - update.winner_count (int): Total number of winners in the giveaway
        - update.winners (List[User]): List of up to 100 winners of the giveaway
        - update.additional_chat_count (int): Optional. The number of other chats the user had to join in order to be eligible for the giveaway
        - update.prize_star_count (int): Optional. The number of Telegram Stars that were split between giveaway winners; for Telegram Star giveaways only
        - update.premium_subscription_month_count (int): Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only
        - update.unclaimed_prize_count (int): Optional. Number of undistributed prizes
        - update.only_new_members (bool): Optional. True, if only users who had joined the chats after the giveaway started were eligible to win
        - update.was_refunded (bool): Optional. True, if the giveaway was canceled because the payment for it was refunded
        - update.prize_description (str): Optional. Description of additional giveaway prize
        """
        # Example implementation
        # Implement your handler logic here
        pass
