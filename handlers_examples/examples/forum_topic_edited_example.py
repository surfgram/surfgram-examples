from surfgram.types import ForumTopicEdited
from typing import Callable


class ExampleForumTopicEdited(ForumTopicEdited):
    """Example implementation of ForumTopicEdited handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_forum_topic_edited",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ForumTopicEdited event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): Optional. New name of the topic, if it was edited
        - update.icon_custom_emoji_id (str): Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed
        """
        # Example implementation
        # Implement your handler logic here
        pass
