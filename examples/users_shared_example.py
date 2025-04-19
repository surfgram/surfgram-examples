from surfgram.types import UsersShared
from typing import Callable


class ExampleUsersShared(UsersShared):
    """Example implementation of UsersShared handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_users_shared",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UsersShared event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.request_id (int): Identifier of the request
        - update.users (List[SharedUser]): Information about users shared with the bot.
        """
        # Example implementation
        # Implement your handler logic here
        pass
