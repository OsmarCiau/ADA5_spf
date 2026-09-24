"""Domain models for Customer Search feature."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    """Represents a customer entity in the system."""

    id: int
    name: str
    email: str
    phone: str
    status: str
