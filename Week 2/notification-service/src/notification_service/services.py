from .exceptions import InvalidNotificationError
from .interfaces import NotificationSender
from .models import Notification

class NotificationService:
    """Application service that delegates delivery to a selected sender."""

    def __init__(self, sender: NotificationSender) -> None:
        self._sender = sender

    def send(self, recipient: str, message: str) -> Notification:
        if not recipient or not recipient.strip():
            raise InvalidNotificationError("Recipient cannot be empty.")

        if not message or not message.strip():
            raise InvalidNotificationError("Message cannot be empty.")

        notification = Notification(
            recipient=recipient.strip(),
            message=message.strip(),
        )
        self._sender.send(notification.recipient, notification.message)
        return notification
