"""Unit tests for Customer domain model."""

import pytest
from src.models import Customer


def test_customer_creation():
    customer = Customer(
        id=1,
        name="Ana García",
        email="ana@example.com",
        phone="+52 999 123 4567",
        status="active",
    )
    assert customer.id == 1
    assert customer.name == "Ana García"
    assert customer.email == "ana@example.com"
    assert customer.phone == "+52 999 123 4567"
    assert customer.status == "active"


def test_customer_immutability():
    customer = Customer(
        id=1,
        name="Ana García",
        email="ana@example.com",
        phone="+52 999 123 4567",
        status="active",
    )
    with pytest.raises(Exception):
        customer.name = "Otro Nombre"  # Frozen dataclass prohibits mutation
