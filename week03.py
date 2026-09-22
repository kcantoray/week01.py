class ModularInteger:
  """Represent an integer in a modular number system."""
  CLOCK_MODULUS = 12
def_init_(self, value: int< modulus: int) -> None:
  """initialize a modular integer with a normalized value."""

    if modulus <= 1:
        raise ValueError("Modulus must be greater than 1.")

    self._modulus = modulus
    self._value = value % modulus

@property
def value(self) -> int:
    """Returns the normalized value."""
    return self._value

@property
def modulus(self) -> int:
    """Returns the modulus"""
    return self._modulus


def_str_(self) ->:
    """Returns the modular integer as a string."""
    return f"{self._value} (mod {self._modulus})"


def __eq__(self, other: object) -> bool:
    """Return whether two modular integers have the same value and modulus."""
    result = NotImplemented

    if isinstance(other, ModularInteger):
        result = self.__value == other.__value and self.__modulus == other.__modulus

    return result

def __add__(self, other: "ModularInteger") -> "ModularInteger":
    """Returns the sum of two modular integers with the same modulus."""
    if self._modulus != other._modulus:
        raise ValueError("Moduli must be the same.")

    result = ModularInteger(
        self._value + other._value,
        self._modulus
    )

    return result

def _mul_(self, other: "ModularInteger") -> "ModularInteger":
    """Returns the product of two modular integers with the same modulus."""
    if self._modulus != other._modulus:
        raise ValueError("Moduli must be the same.")

    result = ModularInteger(
        self._value * other._value,
        self._modulus
    )

    return result

def _pow_(self, exponent: int)) -> "ModularInteger":
    """Returns this modular integer raised to a nonnegative power."""
    if exponent < 0:
        raise ValueError("Exponent must be nonegative.")

    result = ModularInteger(
        self._value ** exponent,
        self._modulus
    )

    return result

@classmethod
def from_clock(cls, hour: int) -> "ModularInteger":
    """Creates a modular integer using the clock modulus."""
    result = cls(hour, cls.CLOCK_MODULUS)

    return result

@ststicmethod
def are_coprime(first: int, second: int) -> bool:
    """Returns whether two integers are relatively prime."""
    result = math.gcd(first, second) == 1

    return result







































