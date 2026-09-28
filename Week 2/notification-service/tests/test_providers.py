from notification_service.providers.console import ConsoleSender
from notification_service.providers.email import EmailSender
from notification_service.providers.sms import SMSSender
from notification_service.exceptions import NotificationDeliveryError
import pytest


def test_console_sender(capsys):
    ConsoleSender().send("user@example.com", "Hello")

    output = capsys.readouterr().out
    assert "[CONSOLE]" in output
    assert "Hello" in output


def test_email_sender(capsys):
    EmailSender("app@example.com").send("user@example.com", "Hello")

    output = capsys.readouterr().out
    assert "[EMAIL]" in output
    assert "user@example.com" in output


def test_email_sender_rejects_invalid_address():
    with pytest.raises(NotificationDeliveryError):
        EmailSender().send("not-an-email", "Hello")


def test_sms_sender(capsys):
    SMSSender().send("+251900000000", "Hello")

    output = capsys.readouterr().out
    assert "[SMS]" in output
    assert "+251900000000" in output
