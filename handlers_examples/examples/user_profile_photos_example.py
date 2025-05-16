from surfgram.types import UserProfilePhotos
from typing import Callable


class ExampleUserProfilePhotos(UserProfilePhotos):
    """Example implementation of UserProfilePhotos handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_user_profile_photos",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UserProfilePhotos event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.total_count (int): Total number of profile pictures the target user has
        - update.photos (List[PhotoSize]): Requested profile pictures (in up to 4 sizes each)
        """
        # Example implementation
        # Implement your handler logic here
        pass
