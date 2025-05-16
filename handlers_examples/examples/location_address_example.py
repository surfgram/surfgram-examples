from surfgram.types import LocationAddress
from typing import Callable


class ExampleLocationAddress(LocationAddress):
    """Example implementation of LocationAddress handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_location_address",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the LocationAddress event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.country_code (str): The two-letter ISO 3166-1 alpha-2 country code of the country where the location is located
        - update.state (str): Optional. State of the location
        - update.city (str): Optional. City of the location
        - update.street (str): Optional. Street address of the location
        """
        # Example implementation
        # Implement your handler logic here
        pass
