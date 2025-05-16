from surfgram.types import ChatMemberRestricted
from typing import Callable


class ExampleChatMemberRestricted(ChatMemberRestricted):
    """Example implementation of ChatMemberRestricted handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_member_restricted",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatMemberRestricted event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.status (str): The member's status in the chat, always "restricted"
        - update.user (User): Information about the user
        - update.is_member (bool): True, if the user is a member of the chat at the moment of the request
        - update.can_send_messages (bool): True, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues
        - update.can_send_audios (bool): True, if the user is allowed to send audios
        - update.can_send_documents (bool): True, if the user is allowed to send documents
        - update.can_send_photos (bool): True, if the user is allowed to send photos
        - update.can_send_videos (bool): True, if the user is allowed to send videos
        - update.can_send_video_notes (bool): True, if the user is allowed to send video notes
        - update.can_send_voice_notes (bool): True, if the user is allowed to send voice notes
        - update.can_send_polls (bool): True, if the user is allowed to send polls
        - update.can_send_other_messages (bool): True, if the user is allowed to send animations, games, stickers and use inline bots
        - update.can_add_web_page_previews (bool): True, if the user is allowed to add web page previews to their messages
        - update.can_change_info (bool): True, if the user is allowed to change the chat title, photo and other settings
        - update.can_invite_users (bool): True, if the user is allowed to invite new users to the chat
        - update.can_pin_messages (bool): True, if the user is allowed to pin messages
        - update.can_manage_topics (bool): True, if the user is allowed to create forum topics
        - update.until_date (int): Date when restrictions will be lifted for this user; Unix time. If 0, then the user is restricted forever
        """
        # Example implementation
        # Implement your handler logic here
        pass
