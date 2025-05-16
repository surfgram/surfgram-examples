from surfgram.types import Poll
from typing import Callable


class ExamplePoll(Poll):
    """Example implementation of Poll handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_poll",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Poll event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique poll identifier
        - update.question (str): Poll question, 1-300 characters
        - update.question_entities (List[MessageEntity]): Optional. Special entities that appear in the question. Currently, only custom emoji entities are allowed in poll questions
        - update.options (List[PollOption]): List of poll options
        - update.total_voter_count (int): Total number of users that voted in the poll
        - update.is_closed (bool): True, if the poll is closed
        - update.is_anonymous (bool): True, if the poll is anonymous
        - update.type (str): Poll type, currently can be "regular" or "quiz"
        - update.allows_multiple_answers (bool): True, if the poll allows multiple answers
        - update.correct_option_id (int): Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
        - update.explanation (str): Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
        - update.explanation_entities (List[MessageEntity]): Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
        - update.open_period (int): Optional. Amount of time in seconds the poll will be active after creation
        - update.close_date (int): Optional. Point in time (Unix timestamp) when the poll will be automatically closed
        """
        # Example implementation
        # Implement your handler logic here
        pass
