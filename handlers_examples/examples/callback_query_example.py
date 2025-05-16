from surfgram.types import CallbackQuery
from typing import Callable


class ExampleCallbackQuery(CallbackQuery):
    """Example implementation of CallbackQuery handler"""
    
    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_callback_query",
        ]
    
    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle
    
    async def handle(self, update, bot):
        """Processes the CallbackQuery event
        
        Args:
            update: Incoming update object
            bot: Bot instance for making API calls
            
        Example fields available:
- update.id (str): Unique identifier for this query
- update.from (User): Sender
- update.message (MaybeInaccessibleMessage): Optional. Message sent by the bot with the callback button that originated the query
- update.inline_message_id (str): Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
- update.chat_instance (str): Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
- update.data (str): Optional. Data associated with the callback button. Be aware that the message originated the query can contain no callback buttons with this data.
- update.game_short_name (str): Optional. Short name of a Game to be returned, serves as the unique identifier for the game
        """
        # Example implementation
await bot.answer_callback_query(
            callback_query_id=update.callback_query.id,
            text="Callback processed!"
        )
        await bot.send_message(
            chat_id=update.callback_query.message.chat.id,
            text="Callback query handled successfully"
        )
