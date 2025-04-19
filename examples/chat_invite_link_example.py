from surfgram.types import ChatInviteLink
from typing import Callable


class ExampleChatInviteLink(ChatInviteLink):
    """Example implementation of ChatInviteLink handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_invite_link",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatInviteLink event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.invite_link (str): The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "…".
        - update.creator (User): Creator of the link
        - update.creates_join_request (bool): True, if users joining the chat via the link need to be approved by chat administrators
        - update.is_primary (bool): True, if the link is primary
        - update.is_revoked (bool): True, if the link is revoked
        - update.name (str): Optional. Invite link name
        - update.expire_date (int): Optional. Point in time (Unix timestamp) when the link will expire or has been expired
        - update.member_limit (int): Optional. The maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
        - update.pending_join_request_count (int): Optional. Number of pending join requests created using this link
        - update.subscription_period (int): Optional. The number of seconds the subscription will be active for before the next payment
        - update.subscription_price (int): Optional. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link
        """
        # Example implementation
        # Implement your handler logic here
        pass
