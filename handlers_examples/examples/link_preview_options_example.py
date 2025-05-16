from surfgram.types import LinkPreviewOptions
from typing import Callable


class ExampleLinkPreviewOptions(LinkPreviewOptions):
    """Example implementation of LinkPreviewOptions handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_link_preview_options",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the LinkPreviewOptions event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.is_disabled (bool): Optional. True, if the link preview is disabled
        - update.url (str): Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used
        - update.prefer_small_media (bool): Optional. True, if the media in the link preview is supposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
        - update.prefer_large_media (bool): Optional. True, if the media in the link preview is supposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview
        - update.show_above_text (bool): Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text
        """
        # Example implementation
        # Implement your handler logic here
        pass
