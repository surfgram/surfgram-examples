from surfgram.types import RevenueWithdrawalStateSucceeded
from typing import Callable


class ExampleRevenueWithdrawalStateSucceeded(RevenueWithdrawalStateSucceeded):
    """Example implementation of RevenueWithdrawalStateSucceeded handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_revenue_withdrawal_state_succeeded",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the RevenueWithdrawalStateSucceeded event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the state, always "succeeded"
        - update.date (int): Date the withdrawal was completed in Unix time
        - update.url (str): An HTTPS URL that can be used to see transaction details
        """
        # Example implementation
        # Implement your handler logic here
        pass
