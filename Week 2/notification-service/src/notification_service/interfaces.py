from typing import Protocol

class NotificationSender(Protocol):
    def send(self, recipient: str, message: str) -> None:
        """Send a notification to the recipient."""
        ...
