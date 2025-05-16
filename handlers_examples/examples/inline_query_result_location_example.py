from surfgram.types import InlineQueryResultLocation
from typing import Callable


class ExampleInlineQueryResultLocation(InlineQueryResultLocation):
    """Example implementation of InlineQueryResultLocation handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_location",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultLocation event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be location
        - update.id (str): Unique identifier for this result, 1-64 Bytes
        - update.latitude (float): Location latitude in degrees
        - update.longitude (float): Location longitude in degrees
        - update.title (str): Location title
        - update.horizontal_accuracy (float): Optional. The radius of uncertainty for the location, measured in meters; 0-1500
        - update.live_period (int): Optional. Period in seconds during which the location can be updated, should be between 60 and 86400, or 0x7FFFFFFF for live locations that can be edited indefinitely.
        - update.heading (int): Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        - update.proximity_alert_radius (int): Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the location
        - update.thumbnail_url (str): Optional. Url of the thumbnail for the result
        - update.thumbnail_width (int): Optional. Thumbnail width
        - update.thumbnail_height (int): Optional. Thumbnail height
        """
        # Example implementation
        # Implement your handler logic here
        pass
