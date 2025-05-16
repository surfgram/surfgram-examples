from surfgram.types import ForumTopic
from typing import Callable


class ExampleForumTopic(ForumTopic):
    """Example implementation of ForumTopic handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_forum_topic",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ForumTopic event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.message_thread_id (int): Unique identifier of the forum topic
        - update.name (str): Name of the topic
        - update.icon_color (int): Color of the topic icon in RGB format
        - update.icon_custom_emoji_id (str): Optional. Unique identifier of the custom emoji shown as the topic icon
        """
        # Example implementation
        # Implement your handler logic here
        pass
