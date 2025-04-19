from surfgram.types import ForceReply
from typing import Callable


class ExampleForceReply(ForceReply):
    """Example implementation of ForceReply handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_force_reply",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ForceReply event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.force_reply (bool): Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
        - update.input_field_placeholder (str): Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters
        - update.selective (bool): Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply to a message in the same chat and forum topic, sender of the original message.
        """
        # Example implementation
        # Implement your handler logic here
        pass
