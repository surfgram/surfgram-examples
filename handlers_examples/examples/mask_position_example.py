from surfgram.types import MaskPosition
from typing import Callable


class ExampleMaskPosition(MaskPosition):
    """Example implementation of MaskPosition handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_mask_position",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MaskPosition event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.point (str): The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin".
        - update.x_shift (float): Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
        - update.y_shift (float): Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
        - update.scale (float): Mask scaling coefficient. For example, 2.0 means double size.
        """
        # Example implementation
        # Implement your handler logic here
        pass
