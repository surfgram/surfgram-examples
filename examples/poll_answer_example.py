from surfgram.types import PollAnswer
from typing import Callable


class ExamplePollAnswer(PollAnswer):
    """Example implementation of PollAnswer handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_poll_answer",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PollAnswer event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.poll_id (str): Unique poll identifier
        - update.voter_chat (Chat): Optional. The chat that changed the answer to the poll, if the voter is anonymous
        - update.user (User): Optional. The user that changed the answer to the poll, if the voter isn't anonymous
        - update.option_ids (List[int]): 0-based identifiers of chosen answer options. May be empty if the vote was retracted.
        """
        # Example implementation
        # Implement your handler logic here
        pass
