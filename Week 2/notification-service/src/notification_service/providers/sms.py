from ..exceptions import NotificationDeliveryError

class SMSSender:
    """SMS provider.

    This educational implementation simulates an SMS gateway.
    """

    def send(self, recipient: str, message: str) -> None:
        if not recipient.strip():
            raise NotificationDeliveryError("Phone number cannot be empty.")

        print(f"[SMS] To: {recipient} | Message: {message}")
