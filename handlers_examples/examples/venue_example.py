from surfgram.types import Venue
from typing import Callable


class ExampleVenue(Venue):
    """Example implementation of Venue handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_venue",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Venue event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.location (Location): Venue location. Can't be a live location
        - update.title (str): Name of the venue
        - update.address (str): Address of the venue
        - update.foursquare_id (str): Optional. Foursquare identifier of the venue
        - update.foursquare_type (str): Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
        - update.google_place_id (str): Optional. Google Places identifier of the venue
        - update.google_place_type (str): Optional. Google Places type of the venue. (See supported types.)
        """
        # Example implementation
        # Implement your handler logic here
        pass
