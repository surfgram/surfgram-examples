from surfgram.types import BusinessOpeningHours
from typing import Callable


class ExampleBusinessOpeningHours(BusinessOpeningHours):
    """Example implementation of BusinessOpeningHours handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_opening_hours",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessOpeningHours event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.time_zone_name (str): Unique name of the time zone for which the opening hours are defined
        - update.opening_hours (List[BusinessOpeningHoursInterval]): List of time intervals describing business opening hours
        """
        # Example implementation
        # Implement your handler logic here
        pass
