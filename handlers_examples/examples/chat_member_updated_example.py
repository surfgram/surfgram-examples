from surfgram.types import ChatMemberUpdated
from typing import Callable


class ExampleChatMemberUpdated(ChatMemberUpdated):
    """Example implementation of ChatMemberUpdated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_member_updated",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatMemberUpdated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): Chat the user belongs to
        - update.from (User): Performer of the action, which resulted in the change
        - update.date (int): Date the change was done in Unix time
        - update.old_chat_member (Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]): Previous information about the chat member
        - update.new_chat_member (Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]): New information about the chat member
        - update.invite_link (ChatInviteLink): Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
        - update.via_join_request (bool): Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator
        - update.via_chat_folder_invite_link (bool): Optional. True, if the user joined the chat via a chat folder invite link
        """
        # Example implementation
        # Implement your handler logic here
        pass
