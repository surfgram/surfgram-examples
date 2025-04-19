from surfgram.types import RevenueWithdrawalStatePending
from typing import Callable


class ExampleRevenueWithdrawalStatePending(RevenueWithdrawalStatePending):
    """Example implementation of RevenueWithdrawalStatePending handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_revenue_withdrawal_state_pending",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the RevenueWithdrawalStatePending event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the state, always "pending"
        """
        # Example implementation
        # Implement your handler logic here
        pass
