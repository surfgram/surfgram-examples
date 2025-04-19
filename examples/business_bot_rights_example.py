from surfgram.types import BusinessBotRights
from typing import Callable


class ExampleBusinessBotRights(BusinessBotRights):
    """Example implementation of BusinessBotRights handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_bot_rights",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessBotRights event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.can_reply (bool): Optional. True, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours
        - update.can_read_messages (bool): Optional. True, if the bot can mark incoming private messages as read
        - update.can_delete_outgoing_messages (bool): Optional. True, if the bot can delete messages sent by the bot
        - update.can_delete_all_messages (bool): Optional. True, if the bot can delete all private messages in managed chats
        - update.can_edit_name (bool): Optional. True, if the bot can edit the first and last name of the business account
        - update.can_edit_bio (bool): Optional. True, if the bot can edit the bio of the business account
        - update.can_edit_profile_photo (bool): Optional. True, if the bot can edit the profile photo of the business account
        - update.can_edit_username (bool): Optional. True, if the bot can edit the username of the business account
        - update.can_change_gift_settings (bool): Optional. True, if the bot can change the privacy settings pertaining to gifts for the business account
        - update.can_view_gifts_and_stars (bool): Optional. True, if the bot can view gifts and the amount of Telegram Stars owned by the business account
        - update.can_convert_gifts_to_stars (bool): Optional. True, if the bot can convert regular gifts owned by the business account to Telegram Stars
        - update.can_transfer_and_upgrade_gifts (bool): Optional. True, if the bot can transfer and upgrade gifts owned by the business account
        - update.can_transfer_stars (bool): Optional. True, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts
        - update.can_manage_stories (bool): Optional. True, if the bot can post, edit and delete stories on behalf of the business account
        """
        # Example implementation
        # Implement your handler logic here
        pass
