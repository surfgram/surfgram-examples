from surfgram.types import PollOption
from typing import Callable


class ExamplePollOption(PollOption):
    """Example implementation of PollOption handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_poll_option",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PollOption event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.text (str): Option text, 1-100 characters
        - update.text_entities (List[MessageEntity]): Optional. Special entities that appear in the option text. Currently, only custom emoji entities are allowed in poll option texts
        - update.voter_count (int): Number of users that voted for this option
        """
        # Example implementation
        # Implement your handler logic here
        pass
