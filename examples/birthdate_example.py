from surfgram.types import Birthdate
from typing import Callable


class ExampleBirthdate(Birthdate):
    """Example implementation of Birthdate handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_birthdate",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Birthdate event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.day (int): Day of the user's birth; 1-31
        - update.month (int): Month of the user's birth; 1-12
        - update.year (int): Optional. Year of the user's birth
        """
        # Example implementation
        # Implement your handler logic here
        pass
