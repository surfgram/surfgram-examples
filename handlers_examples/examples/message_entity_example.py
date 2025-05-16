from surfgram.types import MessageEntity
from typing import Callable


class ExampleMessageEntity(MessageEntity):
    """Example implementation of MessageEntity handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_entity",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageEntity event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag or #hashtag@chatusername), "cashtag" ($USD or $USD@chatusername), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "blockquote" (block quotation), "expandable_blockquote" (collapsed-by-default block quotation), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames), "custom_emoji" (for inline custom emoji stickers)
        - update.offset (int): Offset in UTF-16 code units to the start of the entity
        - update.length (int): Length of the entity in UTF-16 code units
        - update.url (str): Optional. For "text_link" only, URL that will be opened after user taps on the text
        - update.user (User): Optional. For "text_mention" only, the mentioned user
        - update.language (str): Optional. For "pre" only, the programming language of the entity text
        - update.custom_emoji_id (str): Optional. For "custom_emoji" only, unique identifier of the custom emoji. Use getCustomEmojiStickers to get full information about the sticker
        """
        # Example implementation
        # Implement your handler logic here
        pass
