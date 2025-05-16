from surfgram.types import MessageReactionUpdated
from typing import Callable


class ExampleMessageReactionUpdated(MessageReactionUpdated):
    """Example implementation of MessageReactionUpdated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_reaction_updated",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageReactionUpdated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): The chat containing the message the user reacted to
        - update.message_id (int): Unique identifier of the message inside the chat
        - update.user (User): Optional. The user that changed the reaction, if the user isn't anonymous
        - update.actor_chat (Chat): Optional. The chat on behalf of which the reaction was changed, if the user is anonymous
        - update.date (int): Date of the change in Unix time
        - update.old_reaction (List[ReactionType]): Previous list of reaction types that were set by the user
        - update.new_reaction (List[ReactionType]): New list of reaction types that have been set by the user
        """
        # Example implementation
        # Implement your handler logic here
        pass
