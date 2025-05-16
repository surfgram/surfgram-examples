from surfgram.types import Story
from typing import Callable


class ExampleStory(Story):
    """Example implementation of Story handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_story",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Story event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): Chat that posted the story
        - update.id (int): Unique identifier for the story in the chat
        """
        # Example implementation
        # Implement your handler logic here
        pass
