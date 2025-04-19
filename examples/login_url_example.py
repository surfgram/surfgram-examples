from surfgram.types import LoginUrl
from typing import Callable


class ExampleLoginUrl(LoginUrl):
    """Example implementation of LoginUrl handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_login_url",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the LoginUrl event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.url (str): An HTTPS URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
        - update.forward_text (str): Optional. New text of the button in forwarded messages.
        - update.bot_username (str): Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
        - update.request_write_access (bool): Optional. Pass True to request the permission for your bot to send messages to the user.
        """
        # Example implementation
        # Implement your handler logic here
        pass
