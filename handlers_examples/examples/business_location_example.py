from surfgram.types import BusinessLocation
from typing import Callable


class ExampleBusinessLocation(BusinessLocation):
    """Example implementation of BusinessLocation handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_location",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessLocation event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.address (str): Address of the business
        - update.location (Location): Optional. Location of the business
        """
        # Example implementation
        # Implement your handler logic here
        pass
