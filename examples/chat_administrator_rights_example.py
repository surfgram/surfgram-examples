from surfgram.types import ChatAdministratorRights
from typing import Callable


class ExampleChatAdministratorRights(ChatAdministratorRights):
    """Example implementation of ChatAdministratorRights handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_administrator_rights",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatAdministratorRights event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.is_anonymous (bool): True, if the user's presence in the chat is hidden
        - update.can_manage_chat (bool): True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.
        - update.can_delete_messages (bool): True, if the administrator can delete messages of other users
        - update.can_manage_video_chats (bool): True, if the administrator can manage video chats
        - update.can_restrict_members (bool): True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics
        - update.can_promote_members (bool): True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user)
        - update.can_change_info (bool): True, if the user is allowed to change the chat title, photo and other settings
        - update.can_invite_users (bool): True, if the user is allowed to invite new users to the chat
        - update.can_post_stories (bool): True, if the administrator can post stories to the chat
        - update.can_edit_stories (bool): True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat's story archive
        - update.can_delete_stories (bool): True, if the administrator can delete stories posted by other users
        - update.can_post_messages (bool): Optional. True, if the administrator can post messages in the channel, or access channel statistics; for channels only
        - update.can_edit_messages (bool): Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only
        - update.can_pin_messages (bool): Optional. True, if the user is allowed to pin messages; for groups and supergroups only
        - update.can_manage_topics (bool): Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only
        """
        # Example implementation
        # Implement your handler logic here
        pass
