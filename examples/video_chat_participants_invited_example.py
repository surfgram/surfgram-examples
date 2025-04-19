from surfgram.types import VideoChatParticipantsInvited
from typing import Callable


class ExampleVideoChatParticipantsInvited(VideoChatParticipantsInvited):
    """Example implementation of VideoChatParticipantsInvited handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_video_chat_participants_invited",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the VideoChatParticipantsInvited event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.users (List[User]): New members that were invited to the video chat
        """
        # Example implementation
        # Implement your handler logic here
        pass
