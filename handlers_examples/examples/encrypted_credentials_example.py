from surfgram.types import EncryptedCredentials
from typing import Callable


class ExampleEncryptedCredentials(EncryptedCredentials):
    """Example implementation of EncryptedCredentials handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_encrypted_credentials",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the EncryptedCredentials event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.data (str): Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
        - update.hash (str): Base64-encoded data hash for data authentication
        - update.secret (str): Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
        """
        # Example implementation
        # Implement your handler logic here
        pass
