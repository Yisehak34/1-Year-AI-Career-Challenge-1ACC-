# Modular Notification Service

A small Python notification service demonstrating object-oriented software design.

## Features

- Email notification provider
- SMS notification provider
- Console/log notification provider
- Composition instead of inheritance
- `Protocol` interface
- Dataclass model
- Dependency injection
- Strategy pattern
- Custom exceptions
- Type hints
- Unit tests with pytest

The project follows the Week 2 project requirements: the service should support multiple providers while keeping the application service independent of the concrete delivery mechanism.

## Architecture

```text
                 NotificationService
                         |
                         v
                NotificationSender
                  (Protocol)
                   /    |    \
                  /     |     \
                 v      v      v
             Email    SMS   Console
             Sender   Sender  Sender
```

`NotificationService` depends on the `NotificationSender` interface rather than a specific provider. This makes providers interchangeable.

## Project Structure

```text
notification-service/
├── src/
│   └── notification_service/
│       ├── __init__.py
│       ├── models.py
│       ├── interfaces.py
│       ├── services.py
│       ├── providers/
│       │   ├── __init__.py
│       │   ├── email.py
│       │   ├── sms.py
│       │   └── console.py
│       └── exceptions.py
├── tests/
│   ├── test_services.py
│   └── test_providers.py
├── README.md
├── pyproject.toml
└── .gitignore
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install the project and test dependency:

```bash
pip install -e ".[dev]"
```

## Example Usage

```python
from notification_service import NotificationService
from notification_service.providers import EmailSender, SMSSender, ConsoleSender

email_service = NotificationService(EmailSender())
email_service.send(
    recipient="user@example.com",
    message="Your report is ready."
)

sms_service = NotificationService(SMSSender())
sms_service.send(
    recipient="+251900000000",
    message="Your verification code is 123456."
)

console_service = NotificationService(ConsoleSender())
console_service.send(
    recipient="developer",
    message="Test notification."
)
```

## Design Decisions

### 1. Composition

`NotificationService` receives a sender object instead of inheriting from a provider. This models a "has-a" relationship and keeps the service independent of provider implementations.

### 2. Interface

`NotificationSender` is a `Protocol`. Any object implementing the required `send()` method can be used by `NotificationService`.

### 3. Dependency Injection

The sender is injected through the `NotificationService` constructor:

```python
NotificationService(sender)
```

This makes the class easy to test and extend.

### 4. Strategy Pattern

Email, SMS, and Console senders represent interchangeable notification strategies. The service does not need conditional logic such as:

```python
if provider == "email":
    ...
elif provider == "sms":
    ...
```

A new provider can implement the same interface and be injected into the service.

### 5. Dataclass

`Notification` is a small data object, so a frozen dataclass is appropriate. It stores the recipient and message without mixing delivery logic into the data model.

### 6. Exception Handling

Invalid application input raises `InvalidNotificationError`. Provider-specific delivery problems raise `NotificationDeliveryError`.

## Testing

Run:

```bash
pytest
```

Run with detailed output:

```bash
pytest -v
```

## Extending the System

A new provider can be added without changing `NotificationService`.

For example:

```python
class WhatsAppSender:
    def send(self, recipient: str, message: str) -> None:
        print(f"[WHATSAPP] To: {recipient} | Message: {message}")
```

Then:

```python
service = NotificationService(WhatsAppSender())
service.send("+251900000000", "Hello")
```

This demonstrates the Open/Closed Principle: the system can be extended with new providers without modifying the core service.

## Limitations

The Email and SMS providers are intentionally simulated for this learning project. They do not connect to real email servers, SMS gateways, or external APIs.

## Week 2 Design Review

- **Why composition?** It avoids unnecessary inheritance and makes providers interchangeable.
- **Where is the interface?** `NotificationSender` defines the provider contract.
- **What is each class responsible for?** The model stores notification data; the service validates and coordinates delivery; providers perform delivery; exceptions represent errors.
- **Where is dependency injection used?** `NotificationSender` is passed into `NotificationService`.
- **Which SOLID principles influenced the design?** SRP, OCP, ISP, DIP, and practical use of substitutable provider implementations.
- **Which design pattern is used?** Strategy, with providers as interchangeable notification strategies.
- **What if there were 10 providers?** Each provider would implement the same interface, while the service would remain unchanged. A separate factory/registry could be introduced if provider selection becomes complex.

## Learning Goal

The project demonstrates the Week 2 engineering principle:

> OOP is not about creating more classes. Software design is about making responsibilities, dependencies, and changes easier to manage.
