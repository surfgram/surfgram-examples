from surfgram.types import ExternalReplyInfo
from typing import Callable


class ExampleExternalReplyInfo(ExternalReplyInfo):
    """Example implementation of ExternalReplyInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_external_reply_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ExternalReplyInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.origin (MessageOrigin): Origin of the message replied to by the given message
        - update.chat (Chat): Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
        - update.message_id (int): Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
        - update.link_preview_options (LinkPreviewOptions): Optional. Options used for link preview generation for the original message, if it is a text message
        - update.animation (Animation): Optional. Message is an animation, information about the animation
        - update.audio (Audio): Optional. Message is an audio file, information about the file
        - update.document (Document): Optional. Message is a general file, information about the file
        - update.paid_media (PaidMediaInfo): Optional. Message contains paid media; information about the paid media
        - update.photo (List[PhotoSize]): Optional. Message is a photo, available sizes of the photo
        - update.sticker (Sticker): Optional. Message is a sticker, information about the sticker
        - update.story (Union[St, y]): Optional. Message is a forwarded story
        - update.video (Video): Optional. Message is a video, information about the video
        - update.video_note (VideoNote): Optional. Message is a video note, information about the video message
        - update.voice (Voice): Optional. Message is a voice message, information about the file
        - update.has_media_spoiler (bool): Optional. True, if the message media is covered by a spoiler animation
        - update.contact (Contact): Optional. Message is a shared contact, information about the contact
        - update.dice (Dice): Optional. Message is a dice with random value
        - update.game (Game): Optional. Message is a game, information about the game. More about games »
        - update.giveaway (Giveaway): Optional. Message is a scheduled giveaway, information about the giveaway
        - update.giveaway_winners (GiveawayWinners): Optional. A giveaway with public winners was completed
        - update.invoice (Invoice): Optional. Message is an invoice for a payment, information about the invoice. More about payments »
        - update.location (Location): Optional. Message is a shared location, information about the location
        - update.poll (Poll): Optional. Message is a native poll, information about the poll
        - update.venue (Venue): Optional. Message is a venue, information about the venue
        """
        # Example implementation
        # Implement your handler logic here
        pass
