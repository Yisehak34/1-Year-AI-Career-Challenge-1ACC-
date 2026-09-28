class NotificationError(Exception):
    """Base exception for notification errors."""


class InvalidNotificationError(NotificationError):
    """Raised when notification data is invalid."""


class NotificationDeliveryError(NotificationError):
    """Raised when a provider cannot deliver a notification."""
