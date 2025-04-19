from surfgram.types import MessageReactionCountUpdated
from typing import Callable


class ExampleMessageReactionCountUpdated(MessageReactionCountUpdated):
    """Example implementation of MessageReactionCountUpdated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_reaction_count_updated",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageReactionCountUpdated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): The chat containing the message
        - update.message_id (int): Unique message identifier inside the chat
        - update.date (int): Date of the change in Unix time
        - update.reactions (List[ReactionCount]): List of reactions that are present on the message
        """
        # Example implementation
        # Implement your handler logic here
        pass
