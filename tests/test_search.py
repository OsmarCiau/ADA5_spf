"""Unit tests for CustomerSearchService covering AC-01 to AC-05, rules, and NFR-01."""

import time
import pytest
from src.models import Customer
from src.search import CustomerSearchService, ValidationError


class MockCustomerRepository:
    """In-memory repository for isolated unit testing."""

    def __init__(self, customers: list[Customer]) -> None:
        self.customers = customers

    def get_all(self) -> list[Customer]:
        return self.customers


@pytest.fixture
def sample_customers() -> list[Customer]:
    return [
        Customer(id=1, name="Roberto Gómez", email="roberto@mail.com", phone="111", status="active"),
        Customer(id=2, name="Lucía Morales", email="lucia@mail.com", phone="222", status="active"),
        Customer(id=3, name="Ana García", email="ana.garcia@example.com", phone="333", status="active"),
        Customer(id=4, name="Carlos López", email="carlos@empresa.mx", phone="444", status="inactive"),
    ]


@pytest.fixture
def search_service(sample_customers: list[Customer]) -> CustomerSearchService:
    repo = MockCustomerRepository(sample_customers)
    return CustomerSearchService(repo)


def test_search_by_name_partial(search_service: CustomerSearchService):
    """AC-01 & Scenario 1: Partial match by customer name."""
    results = search_service.search("gómez")
    assert len(results) == 1
    assert results[0].id == 1
    assert results[0].name == "Roberto Gómez"

    # Match substring in middle
    results_morales = search_service.search("moral")
    assert len(results_morales) == 1
    assert results_morales[0].id == 2


def test_search_by_email_partial(search_service: CustomerSearchService):
    """AC-02 & Scenario 2: Partial match by email."""
    results = search_service.search("lucia@")
    assert len(results) == 1
    assert results[0].id == 2

    # Match domain
    results_empresa = search_service.search("empresa.mx")
    assert len(results_empresa) == 1
    assert results_empresa[0].id == 4


def test_case_insensitivity(search_service: CustomerSearchService):
    """AC-03 & Scenario 3: Searches are case-insensitive."""
    res_upper = search_service.search("LUCÍA")
    res_lower = search_service.search("lucía")
    res_mixed = search_service.search("LuCíA")

    assert res_upper == res_lower == res_mixed
    assert len(res_upper) == 1
    assert res_upper[0].id == 2


def test_unified_search_matches_both(search_service: CustomerSearchService):
    """FR-03 & Rule 3: Single query matches both name and email simultaneously."""
    # "mail" appears in email of Roberto, Lucía, and potentially others
    results = search_service.search("mail")
    ids = [c.id for c in results]
    assert 1 in ids  # roberto@mail.com
    assert 2 in ids  # lucia@mail.com


def test_query_validation_too_short(search_service: CustomerSearchService):
    """AC-04 & Scenario 4: Reject queries with less than 2 characters."""
    with pytest.raises(ValidationError, match="at least 2 non-whitespace characters"):
        search_service.search("a")


def test_query_validation_whitespace_only(search_service: CustomerSearchService):
    """AC-04: Reject empty strings or whitespace-only queries."""
    with pytest.raises(ValidationError, match="at least 2 non-whitespace characters"):
        search_service.search("   ")

    with pytest.raises(ValidationError, match="at least 2 non-whitespace characters"):
        search_service.search("")


def test_search_no_matches(search_service: CustomerSearchService):
    """AC-05 & Scenario 5: Search yielding zero matches returns empty list without error."""
    results = search_service.search("nonexistentterm")
    assert results == []


def test_search_ordering_by_id(sample_customers: list[Customer]):
    """Rule 4: Results are ordered ascending by id."""
    # Reverse customer list order in repository
    reversed_customers = list(reversed(sample_customers))
    repo = MockCustomerRepository(reversed_customers)
    service = CustomerSearchService(repo)

    results = service.search("com")  # Matches roberto (1), lucia (2), ana (3)
    assert [c.id for c in results] == [1, 2, 3]


def test_search_performance():
    """NFR-01: Performance requirement (< 200 ms on 10,000 records)."""
    large_dataset = [
        Customer(
            id=i,
            name=f"Customer Name {i}",
            email=f"customer{i}@domain.com",
            phone=f"+52 999 000 {i:04d}",
            status="active" if i % 2 == 0 else "inactive",
        )
        for i in range(1, 10001)
    ]
    repo = MockCustomerRepository(large_dataset)
    service = CustomerSearchService(repo)

    start = time.perf_counter()
    results = service.search("9999")
    elapsed_ms = (time.perf_counter() - start) * 1000

    assert len(results) > 0
    assert elapsed_ms < 200, f"Search took {elapsed_ms:.2f} ms (exceeded 200 ms limit)"
