from surfgram.types import WebhookInfo
from typing import Callable


class ExampleWebhookInfo(WebhookInfo):
    """Example implementation of WebhookInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_webhook_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the WebhookInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.url (str): Webhook URL, may be empty if webhook is not set up
        - update.has_custom_certificate (bool): True, if a custom certificate was provided for webhook certificate checks
        - update.pending_update_count (int): Number of updates awaiting delivery
        - update.ip_address (str): Optional. Currently used webhook IP address
        - update.last_error_date (int): Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
        - update.last_error_message (str): Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
        - update.last_synchronization_error_date (int): Optional. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
        - update.max_connections (int): Optional. The maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
        - update.allowed_updates (List[str]): Optional. A list of update types the bot is subscribed to. Defaults to all update types except chat_member
        """
        # Example implementation
        # Implement your handler logic here
        pass
