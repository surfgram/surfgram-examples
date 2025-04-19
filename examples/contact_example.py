from surfgram.types import Contact
from typing import Callable


class ExampleContact(Contact):
    """Example implementation of Contact handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_contact",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Contact event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.phone_number (str): Contact's phone number
        - update.first_name (str): Contact's first name
        - update.last_name (str): Optional. Contact's last name
        - update.user_id (int): Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.vcard (str): Optional. Additional data about the contact in the form of a vCard
        """
        # Example implementation
        # Implement your handler logic here
        pass
