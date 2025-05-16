from surfgram.types import ChatJoinRequest
from typing import Callable


class ExampleChatJoinRequest(ChatJoinRequest):
    """Example implementation of ChatJoinRequest handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_join_request",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatJoinRequest event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): Chat to which the request was sent
        - update.from (User): User that sent the join request
        - update.user_chat_id (int): Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.
        - update.date (int): Date the request was sent in Unix time
        - update.bio (str): Optional. Bio of the user.
        - update.invite_link (ChatInviteLink): Optional. Chat invite link that was used by the user to send the join request
        """
        # Example implementation
        # Implement your handler logic here
        pass
