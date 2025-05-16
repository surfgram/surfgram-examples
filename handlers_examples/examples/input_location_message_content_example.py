from surfgram.types import InputLocationMessageContent
from typing import Callable


class ExampleInputLocationMessageContent(InputLocationMessageContent):
    """Example implementation of InputLocationMessageContent handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_location_message_content",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputLocationMessageContent event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.latitude (float): Latitude of the location in degrees
        - update.longitude (float): Longitude of the location in degrees
        - update.horizontal_accuracy (float): Optional. The radius of uncertainty for the location, measured in meters; 0-1500
        - update.live_period (int): Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
        - update.heading (int): Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        - update.proximity_alert_radius (int): Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        """
        # Example implementation
        # Implement your handler logic here
        pass
