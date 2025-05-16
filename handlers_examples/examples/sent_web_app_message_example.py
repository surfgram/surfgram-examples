from surfgram.types import SentWebAppMessage
from typing import Callable


class ExampleSentWebAppMessage(SentWebAppMessage):
    """Example implementation of SentWebAppMessage handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_sent_web_app_message",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the SentWebAppMessage event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.inline_message_id (str): Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message.
        """
        # Example implementation
        # Implement your handler logic here
        pass
