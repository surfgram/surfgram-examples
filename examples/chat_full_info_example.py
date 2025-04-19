from surfgram.types import ChatFullInfo
from typing import Callable


class ExampleChatFullInfo(ChatFullInfo):
    """Example implementation of ChatFullInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_full_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatFullInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (int): Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.type (str): Type of the chat, can be either "private", "group", "supergroup" or "channel"
        - update.title (str): Optional. Title, for supergroups, channels and group chats
        - update.username (str): Optional. Username, for private chats, supergroups and channels if available
        - update.first_name (str): Optional. First name of the other party in a private chat
        - update.last_name (str): Optional. Last name of the other party in a private chat
        - update.is_forum (bool): Optional. True, if the supergroup chat is a forum (has topics enabled)
        - update.accent_color_id (int): Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details.
        - update.max_reaction_count (int): The maximum number of reactions that can be set on a message in the chat
        - update.photo (ChatPhoto): Optional. Chat photo
        - update.active_usernames (List[str]): Optional. If non-empty, the list of all active chat usernames; for private chats, supergroups and channels
        - update.birthdate (Birthdate): Optional. For private chats, the date of birth of the user
        - update.business_intro (BusinessIntro): Optional. For private chats with business accounts, the intro of the business
        - update.business_location (BusinessLocation): Optional. For private chats with business accounts, the location of the business
        - update.business_opening_hours (BusinessOpeningHours): Optional. For private chats with business accounts, the opening hours of the business
        - update.personal_chat (Chat): Optional. For private chats, the personal channel of the user
        - update.available_reactions (List[ReactionType]): Optional. List of available reactions allowed in the chat. If omitted, then all emoji reactions are allowed.
        - update.background_custom_emoji_id (str): Optional. Custom emoji identifier of the emoji chosen by the chat for the reply header and link preview background
        - update.profile_accent_color_id (int): Optional. Identifier of the accent color for the chat's profile background. See profile accent colors for more details.
        - update.profile_background_custom_emoji_id (str): Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background
        - update.emoji_status_custom_emoji_id (str): Optional. Custom emoji identifier of the emoji status of the chat or the other party in a private chat
        - update.emoji_status_expiration_date (int): Optional. Expiration date of the emoji status of the chat or the other party in a private chat, in Unix time, if any
        - update.bio (str): Optional. Bio of the other party in a private chat
        - update.has_private_forwards (bool): Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user
        - update.has_restricted_voice_and_video_messages (bool): Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat
        - update.join_to_send_messages (bool): Optional. True, if users need to join the supergroup before they can send messages
        - update.join_by_request (bool): Optional. True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators
        - update.description (str): Optional. Description, for groups, supergroups and channel chats
        - update.invite_link (str): Optional. Primary invite link, for groups, supergroups and channel chats
        - update.pinned_message (Message): Optional. The most recent pinned message (by sending date)
        - update.permissions (ChatPermissions): Optional. Default chat member permissions, for groups and supergroups
        - update.accepted_gift_types (AcceptedGiftTypes): Information about types of gifts that are accepted by the chat or by the corresponding user for private chats
        - update.can_send_paid_media (bool): Optional. True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.
        - update.slow_mode_delay (int): Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user; in seconds
        - update.unrestrict_boost_count (int): Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions
        - update.message_auto_delete_time (int): Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds
        - update.has_aggressive_anti_spam_enabled (bool): Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.
        - update.has_hidden_members (bool): Optional. True, if non-administrators can only get the list of bots and administrators in the chat
        - update.has_protected_content (bool): Optional. True, if messages from the chat can't be forwarded to other chats
        - update.has_visible_history (bool): Optional. True, if new chat members will have access to old messages; available only to chat administrators
        - update.sticker_set_name (str): Optional. For supergroups, name of the group sticker set
        - update.can_set_sticker_set (bool): Optional. True, if the bot can change the group sticker set
        - update.custom_emoji_sticker_set_name (str): Optional. For supergroups, the name of the group's custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.
        - update.linked_chat_id (int): Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        - update.location (ChatLocation): Optional. For supergroups, the location to which the supergroup is connected
        """
        # Example implementation
        # Implement your handler logic here
        pass
