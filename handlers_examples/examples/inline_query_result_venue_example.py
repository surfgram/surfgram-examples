from surfgram.types import InlineQueryResultVenue
from typing import Callable


class ExampleInlineQueryResultVenue(InlineQueryResultVenue):
    """Example implementation of InlineQueryResultVenue handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_venue",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultVenue event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be venue
        - update.id (str): Unique identifier for this result, 1-64 Bytes
        - update.latitude (float): Latitude of the venue location in degrees
        - update.longitude (float): Longitude of the venue location in degrees
        - update.title (str): Title of the venue
        - update.address (str): Address of the venue
        - update.foursquare_id (str): Optional. Foursquare identifier of the venue if known
        - update.foursquare_type (str): Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
        - update.google_place_id (str): Optional. Google Places identifier of the venue
        - update.google_place_type (str): Optional. Google Places type of the venue. (See supported types.)
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the venue
        - update.thumbnail_url (str): Optional. Url of the thumbnail for the result
        - update.thumbnail_width (int): Optional. Thumbnail width
        - update.thumbnail_height (int): Optional. Thumbnail height
        """
        # Example implementation
        # Implement your handler logic here
        pass
