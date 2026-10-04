from abc import ABC, abstractmethod
import inspect


class Notification(ABC):
    """Represents a notification with common notification information."""

    def __init__(self, recipient: str, title: str, body: str) -> None:
        """Initialize and validate the common notification fields."""
        if not recipient.strip():
            raise ValueError("Recipient cannot be empty.")
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not body.strip():
            raise ValueError("Body cannot be empty.")
        self.__recipient = recipient
        self.__title = title
        self.__body = body

    @property
    def recipient(self) -> str:
        """Return notification recipient."""
        return self.__recipient

    @property
    def title(self) -> str:
        """Return notification title."""
        return self.__title

    @property
    def body(self) -> str:
        """Return notification body."""
        return self.__body

    @abstractmethod
    def render(self) -> str:
        """Render notification for its specific channel."""
        pass

    def summary(self) -> str:
        """Return a summary containing the recipient and title."""
        # The summary uses only the common notification information.
        result = f"{self.__recipient}: {self.__title}"
        return result


class EmailNotification(Notification):
    """Represent an email notification."""

    def render(self) -> str:
        """Render the notification as an email."""
        result = (
            f"To: {self.recipient}\n"
            f"Subject: {self.title}\n"
            f"{self.body}"
        )
        return result


class SMSNotification(Notification):
    """Represent an SMS notification."""

    _MAX_LENGTH = 160

    def __init__(self, recipient: str, title: str, body: str) -> None:
        """Initialize and validate an SMS notification."""
        super().__init__(recipient, title, body)
        # An SMS must be a single-line message.
        if "\n" in self.title or "\n" in self.body:
            raise ValueError("SMS title and body cannot contain newlines.")
        message = f"{self.title}: {self.body}"
        # Reject an invalid SMS instead of truncating its message.
        if len(message) > self._MAX_LENGTH:
            raise ValueError(
                f"SMS message cannot exceed {self._MAX_LENGTH} characters."
            )

    def render(self) -> str:
        """Render the notification as an SMS message."""
        result = f"{self.title}: {self.body}"
        return result


class InAppNotification(Notification):
    """Represent an in-app notification."""

    _MAX_PREVIEW_LENGTH = 40

    def render(self) -> str:
        """Render the notification with a short body preview."""
        preview = self.body[:self._MAX_PREVIEW_LENGTH]
        # Add an ellipsis when the full body is longer than the preview.
        if len(self.body) > self._MAX_PREVIEW_LENGTH:
            preview += "..."
        result = (
            f"Recipient: {self.recipient}\n"
            f"Title: {self.title}\n"
            f"Preview: {preview}"
        )
        return result


class NotificationFactory:
    """Create notification objects based on their channel."""

    _registry: dict[str, type[Notification]] = {
        "email": EmailNotification,
        "sms": SMSNotification,
    }

    @classmethod
    def create(
        cls,
        channel: str,
        recipient: str,
        title: str,
        body: str
    ) -> Notification:
        """Create and return a notification for the requested channel."""
        if channel not in cls._registry:
            raise ValueError("Unknown notification channel.")
        notification_type = cls._registry[channel]
        result = notification_type(recipient, title, body)
        return result

    @classmethod
    def register(
        cls,
        channel: str,
        notification_type: type[Notification]
    ) -> None:
        """Register a notification class for a new channel."""
        if not channel.strip():
            raise ValueError("Channel cannot be empty.")
        if channel in cls._registry:
            raise ValueError("Channel is already registered.")
        # Check that the value is a class before using issubclass().
        if not inspect.isclass(notification_type):
            raise ValueError("Notification type must be a class.")
        if not issubclass(notification_type, Notification):
            raise ValueError(
                "Notification type must be a subclass of Notification."
            )
        if inspect.isabstract(notification_type):
            raise ValueError("Notification type cannot be abstract.")
        cls._registry[channel] = notification_type

    @classmethod
    def available_channels(cls) -> tuple[str, ...]:
        """Return the registered channels in alphabetical order."""
        result = tuple(sorted(cls._registry.keys()))
        return result


def main() -> None:
    """Run a scenario that uses the notification factory."""
    # The factory reports its channels before and after registration.
    print("Before registration:", NotificationFactory.available_channels())
    NotificationFactory.register("in_app", InAppNotification)
    print("After registration:", NotificationFactory.available_channels())
    print()

    # Client code names a channel; the factory chooses the class.
    email = NotificationFactory.create(
        "email",
        "kennaoui@luc.edu",
        "Room change",
        "Class meets in Cuneo 218."
    )
    print(type(email).__name__)
    print(email.summary())
    print(email.render())
    print()

    # Create notifications through the factory.
    sms = NotificationFactory.create(
        "sms",
        "Sam",
        "Reminder",
        "Class starts at 2 PM."
    )
    in_app = NotificationFactory.create(
        "in_app",
        "Alex",
        "Announcement",
        "This is a longer message with more than forty characters."
    )
    notifications: list[Notification] = [email, sms, in_app]

    # Polymorphism lets each object decide how it should render.
    for notification in notifications:
        print(notification.summary())
        print(notification.render())
        print()

    # The notification constructor must reject a blank title.
    try:
        NotificationFactory.create("email", "Sam", "  ", "Hello")
        print("ERROR: blank title was accepted")
    except ValueError as error:
        print("Blank title rejected:", error)

    # The factory must reject an unknown channel.
    try:
        NotificationFactory.create(
            "fax",
            "Sam",
            "Update",
            "Hello"
        )
        print("ERROR: unknown channel was accepted")
    except ValueError as error:
        print("Unknown channel rejected:", error)

    # A message of exactly 160 characters must be accepted.
    sms_160 = NotificationFactory.create(
        "sms",
        "Sam",
        "A",
        "x" * 157
    )
    print("160-character SMS accepted:", len(sms_160.render()))

    # A message of 161 characters must be rejected.
    try:
        NotificationFactory.create(
            "sms",
            "Sam",
            "A",
            "x" * 158
        )
        print("ERROR: 161-character SMS was accepted")
    except ValueError as error:
        print("161-character SMS rejected:", error)

    # An SMS containing a newline must be rejected.
    try:
        NotificationFactory.create(
            "sms",
            "Sam",
            "A",
            "Hello\nWorld"
        )
        print("ERROR: SMS newline was accepted")
    except ValueError as error:
        print("SMS newline rejected:", error)

    # Registering an existing channel must be rejected.
    try:
        NotificationFactory.register("in_app", InAppNotification)
        print("ERROR: duplicate channel was accepted")
    except ValueError as error:
        print("Duplicate channel rejected:", error)

    # Registering an instance instead of a class must be rejected.
    email_instance = EmailNotification("Sam", "Hi", "Hello")
    try:
        NotificationFactory.register("email_copy", email_instance)
        print("ERROR: notification instance was accepted")
    except ValueError as error:
        print("Notification instance rejected:", error)

    # The abstract Notification class cannot be registered.
    try:
        NotificationFactory.register("generic", Notification)
        print("ERROR: abstract class was accepted")
    except ValueError as error:
        print("Abstract class rejected:", error)

    # The abstract Notification class cannot be instantiated directly.
    try:
        Notification("Sam", "Update", "Hello")
        print("ERROR: abstract Notification was created")
    except TypeError as error:
        print("Abstract Notification rejected:", error)


if __name__ == "__main__":
    main()











