from surfgram.types import InlineQueryResultVideo
from typing import Callable


class ExampleInlineQueryResultVideo(InlineQueryResultVideo):
    """Example implementation of InlineQueryResultVideo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_video",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultVideo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be video
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.video_url (str): A valid URL for the embedded video player or video file
        - update.mime_type (str): MIME type of the content of the video URL, "text/html" or "video/mp4"
        - update.thumbnail_url (str): URL of the thumbnail (JPEG only) for the video
        - update.title (str): Title for the result
        - update.caption (str): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the video caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.video_width (int): Optional. Video width
        - update.video_height (int): Optional. Video height
        - update.video_duration (int): Optional. Video duration in seconds
        - update.description (str): Optional. Short description of the result
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
        """
        # Example implementation
        # Implement your handler logic here
        pass
