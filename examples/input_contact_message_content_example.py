from surfgram.types import InputContactMessageContent
from typing import Callable


class ExampleInputContactMessageContent(InputContactMessageContent):
    """Example implementation of InputContactMessageContent handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_contact_message_content",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputContactMessageContent event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.phone_number (str): Contact's phone number
        - update.first_name (str): Contact's first name
        - update.last_name (str): Optional. Contact's last name
        - update.vcard (str): Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
        """
        # Example implementation
        # Implement your handler logic here
        pass
