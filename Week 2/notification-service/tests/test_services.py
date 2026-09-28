import pytest

from notification_service.exceptions import InvalidNotificationError
from notification_service.services import NotificationService


class FakeSender:
    def __init__(self):
        self.calls = []

    def send(self, recipient: str, message: str) -> None:
        self.calls.append((recipient, message))


def test_notification_service_delegates_to_sender():
    sender = FakeSender()
    service = NotificationService(sender)

    result = service.send(" user@example.com ", " Hello World ")

    assert result.recipient == "user@example.com"
    assert result.message == "Hello World"
    assert sender.calls == [("user@example.com", "Hello World")]


@pytest.mark.parametrize("recipient", ["", "   "])
def test_empty_recipient_is_rejected(recipient):
    service = NotificationService(FakeSender())

    with pytest.raises(InvalidNotificationError):
        service.send(recipient, "Hello")


@pytest.mark.parametrize("message", ["", "   "])
def test_empty_message_is_rejected(message):
    service = NotificationService(FakeSender())

    with pytest.raises(InvalidNotificationError):
        service.send("user@example.com", message)


def test_service_works_with_different_strategies():
    first = FakeSender()
    second = FakeSender()

    NotificationService(first).send("a@example.com", "First")
    NotificationService(second).send("b@example.com", "Second")

    assert first.calls == [("a@example.com", "First")]
    assert second.calls == [("b@example.com", "Second")]
