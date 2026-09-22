import math


class ModularInteger:
    """Represent an integer in a modular number system."""

    CLOCK_MODULUS = 12

    def __init__(self, value: int, modulus: int) -> None:
        """Initialize a modular integer with a normalized value."""

        if modulus <= 1:
            raise ValueError("Modulus must be greater than 1.")

        self.__modulus = modulus
        self.__value = value % modulus

    @property
    def value(self) -> int:
        """Return the normalized value."""
        return self.__value

    @property
    def modulus(self) -> int:
        """Return the modulus."""
        return self.__modulus

    def __str__(self) -> str:
        """Return the modular integer as a string."""
        return f"{self.__value} (mod {self.__modulus})"

    def __eq__(self, other: object) -> bool:
        """Return whether two modular integers have the same value and modulus."""
        result = NotImplemented

        if isinstance(other, ModularInteger):
            result = (
                self.__value == other.__value
                and self.__modulus == other.__modulus
            )

        return result

    def __add__(self, other: "ModularInteger") -> "ModularInteger":
        """Return the sum of two modular integers with the same modulus."""
        if self.__modulus != other.__modulus:
            raise ValueError("Moduli must be the same.")

        result = ModularInteger(
            self.__value + other.__value,
            self.__modulus
        )

        return result

    def __mul__(self, other: "ModularInteger") -> "ModularInteger":
        """Return the product of two modular integers with the same modulus."""
        if self.__modulus != other.__modulus:
            raise ValueError("Moduli must be the same.")

        result = ModularInteger(
            self.__value * other.__value,
            self.__modulus
        )

        return result

    def __pow__(self, exponent: int) -> "ModularInteger":
        """Return this modular integer raised to a nonnegative power."""
        if exponent < 0:
            raise ValueError("Exponent must be nonnegative.")

        result = ModularInteger(
            self.__value ** exponent,
            self.__modulus
        )

        return result

    @classmethod
    def from_clock(cls, hour: int) -> "ModularInteger":
        """Create a modular integer using the clock modulus."""
        result = cls(hour, cls.CLOCK_MODULUS)

        return result

    @staticmethod
    def are_coprime(first: int, second: int) -> bool:
        """Return whether two integers are relatively prime."""
        result = math.gcd(first, second) == 1

        return result








































