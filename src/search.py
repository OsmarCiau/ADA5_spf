"""Search service and business logic for Customer Search feature."""

from src.models import Customer
from src.repository import CustomerRepository


class ValidationError(Exception):
    """Raised when user search query fails domain validation rules."""


class CustomerSearchService:
    """Service encapsulating search rules, validation, and sorting."""

    def __init__(self, repository: CustomerRepository) -> None:
        self.repository = repository

    def validate_query(self, query: str) -> str:
        """Validates the search query.

        Rules:
            1. Cannot be empty or exclusively whitespace.
            2. Minimum length of 2 non-whitespace characters.

        Returns:
            Normalized lowercase query string stripped of leading/trailing spaces.

        Raises:
            ValidationError: If query violates validation rules.
        """
        if query is None or not isinstance(query, str):
            raise ValidationError("Search query must contain at least 2 non-whitespace characters.")

        stripped = query.strip()
        if len(stripped) < 2:
            raise ValidationError("Search query must contain at least 2 non-whitespace characters.")

        return stripped.lower()

    def search(self, query: str, limit: int = 50) -> list[Customer]:
        """Performs partial, case-insensitive search across customer name and email fields.

        Returns matching customers sorted in ascending order by ID.
        """
        normalized_query = self.validate_query(query)
        all_customers = self.repository.get_all()

        matches = [
            customer
            for customer in all_customers
            if (
                normalized_query in customer.name.lower()
                or normalized_query in customer.email.lower()
            )
        ]

        matches.sort(key=lambda c: c.id)
        return matches[:limit]
