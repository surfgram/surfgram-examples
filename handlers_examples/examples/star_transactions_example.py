from surfgram.types import StarTransactions
from typing import Callable


class ExampleStarTransactions(StarTransactions):
    """Example implementation of StarTransactions handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_star_transactions",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StarTransactions event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.transactions (List[StarTransaction]): The list of transactions
        """
        # Example implementation
        # Implement your handler logic here
        pass
