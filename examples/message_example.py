from surfgram.types import Message
from typing import Callable


class ExampleMessage(Message):
    """Example implementation of Message handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Message event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.message_id (int): Unique message identifier inside this chat. In specific instances (e.g., message containing a video sent to a big chat), the server might automatically schedule a message instead of sending it immediately. In such cases, this field will be 0 and the relevant message will be unusable until it is actually sent
        - update.message_thread_id (int): Optional. Unique identifier of a message thread to which the message belongs; for supergroups only
        - update.from (User): Optional. Sender of the message; may be empty for messages sent to channels. For backward compatibility, if the message was sent on behalf of a chat, the field contains a fake sender user in non-channel chats
        - update.sender_chat (Chat): Optional. Sender of the message when sent on behalf of a chat. For example, the supergroup itself for messages sent by its anonymous administrators or a linked channel for messages automatically forwarded to the channel's discussion group. For backward compatibility, if the message was sent on behalf of a chat, the field from contains a fake sender user in non-channel chats.
        - update.sender_boost_count (int): Optional. If the sender of the message boosted the chat, the number of boosts added by the user
        - update.sender_business_bot (User): Optional. The bot that actually sent the message on behalf of the business account. Available only for outgoing messages sent on behalf of the connected business account.
        - update.date (int): Date the message was sent in Unix time. It is always a positive number, representing a valid date.
        - update.business_connection_id (str): Optional. Unique identifier of the business connection from which the message was received. If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
        - update.chat (Chat): Chat the message belongs to
        - update.forward_origin (MessageOrigin): Optional. Information about the original message for forwarded messages
        - update.is_topic_message (bool): Optional. True, if the message is sent to a forum topic
        - update.is_automatic_forward (bool): Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group
        - update.reply_to_message (Message): Optional. For replies in the same chat and message thread, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        - update.external_reply (ExternalReplyInfo): Optional. Information about the message that is being replied to, which may come from another chat or forum topic
        - update.quote (TextQuote): Optional. For replies that quote part of the original message, the quoted part of the message
        - update.reply_to_story (Union[St, y]): Optional. For replies to a story, the original story
        - update.via_bot (User): Optional. Bot through which the message was sent
        - update.edit_date (int): Optional. Date the message was last edited in Unix time
        - update.has_protected_content (bool): Optional. True, if the message can't be forwarded
        - update.is_from_offline (bool): Optional. True, if the message was sent by an implicit action, for example, as an away or a greeting business message, or as a scheduled message
        - update.media_group_id (str): Optional. The unique identifier of a media message group this message belongs to
        - update.author_signature (str): Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
        - update.paid_star_count (int): Optional. The number of Telegram Stars that were paid by the sender of the message to send it
        - update.text (str): Optional. For text messages, the actual UTF-8 text of the message
        - update.entities (List[MessageEntity]): Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
        - update.link_preview_options (LinkPreviewOptions): Optional. Options used for link preview generation for the message, if it is a text message and link preview options were changed
        - update.effect_id (str): Optional. Unique identifier of the message effect added to the message
        - update.animation (Animation): Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
        - update.audio (Audio): Optional. Message is an audio file, information about the file
        - update.document (Document): Optional. Message is a general file, information about the file
        - update.paid_media (PaidMediaInfo): Optional. Message contains paid media; information about the paid media
        - update.photo (List[PhotoSize]): Optional. Message is a photo, available sizes of the photo
        - update.sticker (Sticker): Optional. Message is a sticker, information about the sticker
        - update.story (Union[St, y]): Optional. Message is a forwarded story
        - update.video (Video): Optional. Message is a video, information about the video
        - update.video_note (VideoNote): Optional. Message is a video note, information about the video message
        - update.voice (Voice): Optional. Message is a voice message, information about the file
        - update.caption (str): Optional. Caption for the animation, audio, document, paid media, photo, video or voice
        - update.caption_entities (List[MessageEntity]): Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
        - update.show_caption_above_media (bool): Optional. True, if the caption must be shown above the message media
        - update.has_media_spoiler (bool): Optional. True, if the message media is covered by a spoiler animation
        - update.contact (Contact): Optional. Message is a shared contact, information about the contact
        - update.dice (Dice): Optional. Message is a dice with random value
        - update.game (Game): Optional. Message is a game, information about the game. More about games »
        - update.poll (Poll): Optional. Message is a native poll, information about the poll
        - update.venue (Venue): Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
        - update.location (Location): Optional. Message is a shared location, information about the location
        - update.new_chat_members (List[User]): Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
        - update.left_chat_member (User): Optional. A member was removed from the group, information about them (this member may be the bot itself)
        - update.new_chat_title (str): Optional. A chat title was changed to this value
        - update.new_chat_photo (List[PhotoSize]): Optional. A chat photo was change to this value
        - update.delete_chat_photo (bool): Optional. Service message: the chat photo was deleted
        - update.group_chat_created (bool): Optional. Service message: the group has been created
        - update.supergroup_chat_created (bool): Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
        - update.channel_chat_created (bool): Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
        - update.message_auto_delete_timer_changed (MessageAutoDeleteTimerChanged): Optional. Service message: auto-delete timer settings changed in the chat
        - update.migrate_to_chat_id (int): Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.migrate_from_chat_id (int): Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.pinned_message (MaybeInaccessibleMessage): Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        - update.invoice (Invoice): Optional. Message is an invoice for a payment, information about the invoice. More about payments »
        - update.successful_payment (SuccessfulPayment): Optional. Message is a service message about a successful payment, information about the payment. More about payments »
        - update.refunded_payment (RefundedPayment): Optional. Message is a service message about a refunded payment, information about the payment. More about payments »
        - update.users_shared (UsersShared): Optional. Service message: users were shared with the bot
        - update.chat_shared (ChatShared): Optional. Service message: a chat was shared with the bot
        - update.gift (GiftInfo): Optional. Service message: a regular gift was sent or received
        - update.unique_gift (UniqueGiftInfo): Optional. Service message: a unique gift was sent or received
        - update.connected_website (str): Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
        - update.write_access_allowed (WriteAccessAllowed): Optional. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess
        - update.passport_data (Union[Passp, tData]): Optional. Telegram Passport data
        - update.proximity_alert_triggered (ProximityAlertTriggered): Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
        - update.boost_added (ChatBoostAdded): Optional. Service message: user boosted the chat
        - update.chat_background_set (ChatBackground): Optional. Service message: chat background set
        - update.forum_topic_created (Union[F, umTopicCreated]): Optional. Service message: forum topic created
        - update.forum_topic_edited (Union[F, umTopicEdited]): Optional. Service message: forum topic edited
        - update.forum_topic_closed (Union[F, umTopicClosed]): Optional. Service message: forum topic closed
        - update.forum_topic_reopened (Union[F, umTopicReopened]): Optional. Service message: forum topic reopened
        - update.general_forum_topic_hidden (Union[GeneralF, umTopicHidden]): Optional. Service message: the 'General' forum topic hidden
        - update.general_forum_topic_unhidden (Union[GeneralF, umTopicUnhidden]): Optional. Service message: the 'General' forum topic unhidden
        - update.giveaway_created (GiveawayCreated): Optional. Service message: a scheduled giveaway was created
        - update.giveaway (Giveaway): Optional. The message is a scheduled giveaway message
        - update.giveaway_winners (GiveawayWinners): Optional. A giveaway with public winners was completed
        - update.giveaway_completed (GiveawayCompleted): Optional. Service message: a giveaway without public winners was completed
        - update.paid_message_price_changed (PaidMessagePriceChanged): Optional. Service message: the price for paid messages has changed in the chat
        - update.video_chat_scheduled (VideoChatScheduled): Optional. Service message: video chat scheduled
        - update.video_chat_started (VideoChatStarted): Optional. Service message: video chat started
        - update.video_chat_ended (VideoChatEnded): Optional. Service message: video chat ended
        - update.video_chat_participants_invited (VideoChatParticipantsInvited): Optional. Service message: new participants invited to a video chat
        - update.web_app_data (WebAppData): Optional. Service message: data sent by a Web App
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
        """
        # Example implementation


await bot.send_message(
    chat_id=update.message.chat.id, text=f"Received message: {update.message.text}"
)
