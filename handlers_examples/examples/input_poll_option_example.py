from surfgram.types import InputPollOption
from typing import Callable


class ExampleInputPollOption(InputPollOption):
    """Example implementation of InputPollOption handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_poll_option",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputPollOption event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.text (str): Option text, 1-100 characters
        - update.text_parse_mode (str): Optional. Mode for parsing entities in the text. See formatting options for more details. Currently, only custom emoji entities are allowed
        - update.text_entities (List[MessageEntity]): Optional. A JSON-serialized list of special entities that appear in the poll option text. It can be specified instead of text_parse_mode
        """
        # Example implementation
        # Implement your handler logic here
        pass
