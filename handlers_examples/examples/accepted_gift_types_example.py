from surfgram.types import AcceptedGiftTypes
from typing import Callable


class ExampleAcceptedGiftTypes(AcceptedGiftTypes):
    """Example implementation of AcceptedGiftTypes handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_accepted_gift_types",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the AcceptedGiftTypes event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.unlimited_gifts (bool): True, if unlimited regular gifts are accepted
        - update.limited_gifts (bool): True, if limited regular gifts are accepted
        - update.unique_gifts (bool): True, if unique gifts or gifts that can be upgraded to unique for free are accepted
        - update.premium_subscription (bool): True, if a Telegram Premium subscription is accepted
        """
        # Example implementation
        # Implement your handler logic here
        pass
