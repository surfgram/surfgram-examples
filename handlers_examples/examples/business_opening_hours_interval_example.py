from surfgram.types import BusinessOpeningHoursInterval
from typing import Callable


class ExampleBusinessOpeningHoursInterval(BusinessOpeningHoursInterval):
    """Example implementation of BusinessOpeningHoursInterval handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_opening_hours_interval",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessOpeningHoursInterval event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.opening_minute (int): The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60
        - update.closing_minute (int): The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60
        """
        # Example implementation
        # Implement your handler logic here
        pass
