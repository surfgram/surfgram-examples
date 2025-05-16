from surfgram.types import CopyTextButton
from typing import Callable


class ExampleCopyTextButton(CopyTextButton):
    """Example implementation of CopyTextButton handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_copy_text_button",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the CopyTextButton event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.text (str): The text to be copied to the clipboard; 1-256 characters
        """
        # Example implementation
        # Implement your handler logic here
        pass
