from surfgram.types import Dice
from typing import Callable


class ExampleDice(Dice):
    """Example implementation of Dice handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_dice",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Dice event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.emoji (str): Emoji on which the dice throw animation is based
        - update.value (int): Value of the dice, 1-6 for "", "" and "" base emoji, 1-5 for "" and "" base emoji, 1-64 for "" base emoji
        """
        # Example implementation
        # Implement your handler logic here
        pass
