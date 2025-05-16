from surfgram.types import Game
from typing import Callable


class ExampleGame(Game):
    """Example implementation of Game handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_game",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Game event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.title (str): Title of the game
        - update.description (str): Description of the game
        - update.photo (List[PhotoSize]): Photo that will be displayed in the game message in chats.
        - update.text (str): Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
        - update.text_entities (List[MessageEntity]): Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
        - update.animation (Animation): Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
        """
        # Example implementation
        # Implement your handler logic here
        pass
