from surfgram.types import ChatPermissions
from typing import Callable


class ExampleChatPermissions(ChatPermissions):
    """Example implementation of ChatPermissions handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_permissions",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatPermissions event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.can_send_messages (bool): Optional. True, if the user is allowed to send text messages, contacts, giveaways, giveaway winners, invoices, locations and venues
        - update.can_send_audios (bool): Optional. True, if the user is allowed to send audios
        - update.can_send_documents (bool): Optional. True, if the user is allowed to send documents
        - update.can_send_photos (bool): Optional. True, if the user is allowed to send photos
        - update.can_send_videos (bool): Optional. True, if the user is allowed to send videos
        - update.can_send_video_notes (bool): Optional. True, if the user is allowed to send video notes
        - update.can_send_voice_notes (bool): Optional. True, if the user is allowed to send voice notes
        - update.can_send_polls (bool): Optional. True, if the user is allowed to send polls
        - update.can_send_other_messages (bool): Optional. True, if the user is allowed to send animations, games, stickers and use inline bots
        - update.can_add_web_page_previews (bool): Optional. True, if the user is allowed to add web page previews to their messages
        - update.can_change_info (bool): Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
        - update.can_invite_users (bool): Optional. True, if the user is allowed to invite new users to the chat
        - update.can_pin_messages (bool): Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
        - update.can_manage_topics (bool): Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages
        """
        # Example implementation
        # Implement your handler logic here
        pass
