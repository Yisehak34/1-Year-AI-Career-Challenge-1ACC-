from dataclasses import dataclass

@dataclass(frozen=True)
class Notification:
    recipient: str
    message: str
