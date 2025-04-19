from surfgram.types import InlineQueryResultCachedAudio
from typing import Callable


class ExampleInlineQueryResultCachedAudio(InlineQueryResultCachedAudio):
    """Example implementation of InlineQueryResultCachedAudio handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_cached_audio",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultCachedAudio event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be audio
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.audio_file_id (str): A valid file identifier for the audio file
        - update.caption (str): Optional. Caption, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the audio
        """
        # Example implementation
        # Implement your handler logic here
        pass
