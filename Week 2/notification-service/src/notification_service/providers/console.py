from ..interfaces import NotificationSender

class ConsoleSender:
    """Notification provider that writes notifications to the console."""

    def send(self, recipient: str, message: str) -> None:
        print(f"[CONSOLE] To: {recipient} | Message: {message}")
