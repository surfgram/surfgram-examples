from surfgram.types import MessageAutoDeleteTimerChanged
from typing import Callable


class ExampleMessageAutoDeleteTimerChanged(MessageAutoDeleteTimerChanged):
    """Example implementation of MessageAutoDeleteTimerChanged handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_auto_delete_timer_changed",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageAutoDeleteTimerChanged event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.message_auto_delete_time (int): New auto-delete time for messages in the chat; in seconds
        """
        # Example implementation
        # Implement your handler logic here
        pass
