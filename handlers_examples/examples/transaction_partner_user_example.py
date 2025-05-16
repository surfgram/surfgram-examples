from surfgram.types import TransactionPartnerUser
from typing import Callable


class ExampleTransactionPartnerUser(TransactionPartnerUser):
    """Example implementation of TransactionPartnerUser handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_user",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerUser event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "user"
        - update.transaction_type (str): Type of the transaction, currently one of "invoice_payment" for payments via invoices, "paid_media_payment" for payments for paid media, "gift_purchase" for gifts sent by the bot, "premium_purchase" for Telegram Premium subscriptions gifted by the bot, "business_account_transfer" for direct transfers from managed business accounts
        - update.user (User): Information about the user
        - update.affiliate (AffiliateInfo): Optional. Information about the affiliate that received a commission via this transaction. Can be available only for "invoice_payment" and "paid_media_payment" transactions.
        - update.invoice_payload (str): Optional. Bot-specified invoice payload. Can be available only for "invoice_payment" transactions.
        - update.subscription_period (int): Optional. The duration of the paid subscription. Can be available only for "invoice_payment" transactions.
        - update.paid_media (List[PaidMedia]): Optional. Information about the paid media bought by the user; for "paid_media_payment" transactions only
        - update.paid_media_payload (str): Optional. Bot-specified paid media payload. Can be available only for "paid_media_payment" transactions.
        - update.gift (Gift): Optional. The gift sent to the user by the bot; for "gift_purchase" transactions only
        - update.premium_subscription_duration (int): Optional. Number of months the gifted Telegram Premium subscription will be active for; for "premium_purchase" transactions only
        """
        # Example implementation
        # Implement your handler logic here
        pass
