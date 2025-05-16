from surfgram.types import ChatBoostSourceGiveaway
from typing import Callable


class ExampleChatBoostSourceGiveaway(ChatBoostSourceGiveaway):
    """Example implementation of ChatBoostSourceGiveaway handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost_source_giveaway",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoostSourceGiveaway event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Source of the boost, always "giveaway"
        - update.giveaway_message_id (int): Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn't sent yet.
        - update.user (User): Optional. User that won the prize in the giveaway if any; for Telegram Premium giveaways only
        - update.prize_star_count (int): Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only
        - update.is_unclaimed (bool): Optional. True, if the giveaway was completed, but there was no user to win the prize
        """
        # Example implementation
        # Implement your handler logic here
        pass
