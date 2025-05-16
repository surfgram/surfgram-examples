from surfgram.types import GameHighScore
from typing import Callable


class ExampleGameHighScore(GameHighScore):
    """Example implementation of GameHighScore handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_game_high_score",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the GameHighScore event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.position (int): Position in high score table for the game
        - update.user (User): User
        - update.score (int): Score
        """
        # Example implementation
        # Implement your handler logic here
        pass
