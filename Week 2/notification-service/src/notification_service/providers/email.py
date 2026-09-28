from ..exceptions import NotificationDeliveryError

class EmailSender:
    """Email provider.

    This educational implementation simulates email delivery rather than
    connecting to a real SMTP/email API.
    """

    def __init__(self, sender_address: str = "noreply@example.com") -> None:
        self.sender_address = sender_address

    def send(self, recipient: str, message: str) -> None:
        if "@" not in recipient:
            raise NotificationDeliveryError(
                f"Invalid email recipient: {recipient}"
            )

        print(
            f"[EMAIL] From: {self.sender_address} | "
            f"To: {recipient} | Message: {message}"
        )
