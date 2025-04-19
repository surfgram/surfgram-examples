from surfgram.types import BusinessIntro
from typing import Callable


class ExampleBusinessIntro(BusinessIntro):
    """Example implementation of BusinessIntro handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_intro",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessIntro event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.title (str): Optional. Title text of the business intro
        - update.message (str): Optional. Message text of the business intro
        - update.sticker (Sticker): Optional. Sticker of the business intro
        """
        # Example implementation
        # Implement your handler logic here
        pass
