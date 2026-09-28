from notification_service import NotificationService
from notification_service.providers import ConsoleSender, EmailSender, SMSSender

def main() -> None:
    NotificationService(EmailSender()).send(
        "user@example.com",
        "Your report is ready."
    )

    NotificationService(SMSSender()).send(
        "+251900000000",
        "Your verification code is 123456."
    )

    NotificationService(ConsoleSender()).send(
        "developer",
        "Notification service is working."
    )

if __name__ == "__main__":
    main()
