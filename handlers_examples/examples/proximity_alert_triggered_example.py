from surfgram.types import ProximityAlertTriggered
from typing import Callable


class ExampleProximityAlertTriggered(ProximityAlertTriggered):
    """Example implementation of ProximityAlertTriggered handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_proximity_alert_triggered",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ProximityAlertTriggered event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.traveler (User): User that triggered the alert
        - update.watcher (User): User that set the alert
        - update.distance (int): The distance between the users
        """
        # Example implementation
        # Implement your handler logic here
        pass
