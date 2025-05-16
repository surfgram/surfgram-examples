from surfgram.types import ChosenInlineResult
from typing import Callable


class ExampleChosenInlineResult(ChosenInlineResult):
    """Example implementation of ChosenInlineResult handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chosen_inline_result",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChosenInlineResult event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.result_id (str): The unique identifier for the result that was chosen
        - update.from (User): The user that chose the result
        - update.location (Location): Optional. Sender location, only for bots that require user location
        - update.inline_message_id (str): Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        - update.query (str): The query that was used to obtain the result
        """
        # Example implementation
        # Implement your handler logic here
        pass
