from surfgram.types import Location
from typing import Callable


class ExampleLocation(Location):
    """Example implementation of Location handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_location",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Location event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.latitude (float): Latitude as defined by the sender
        - update.longitude (float): Longitude as defined by the sender
        - update.horizontal_accuracy (float): Optional. The radius of uncertainty for the location, measured in meters; 0-1500
        - update.live_period (int): Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
        - update.heading (int): Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
        - update.proximity_alert_radius (int): Optional. The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
        """
        # Example implementation
        # Implement your handler logic here
        pass
