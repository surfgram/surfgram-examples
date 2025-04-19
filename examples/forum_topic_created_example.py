from surfgram.types import ForumTopicCreated
from typing import Callable


class ExampleForumTopicCreated(ForumTopicCreated):
    """Example implementation of ForumTopicCreated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_forum_topic_created",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ForumTopicCreated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): Name of the topic
        - update.icon_color (int): Color of the topic icon in RGB format
        - update.icon_custom_emoji_id (str): Optional. Unique identifier of the custom emoji shown as the topic icon
        """
        # Example implementation
        # Implement your handler logic here
        pass
