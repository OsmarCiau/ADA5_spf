"""Data access repository for Customer entities from JSON sources."""

import json
from pathlib import Path
from src.models import Customer


class CustomerRepository:
    """Repository responsible for loading customers from a persistent JSON file."""

    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def get_all(self) -> list[Customer]:
        """Loads and returns all customers from the JSON data file.

        Raises:
            FileNotFoundError: If the data file does not exist.
            ValueError: If the JSON data is malformed or structure is invalid.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"Customer data file not found: {self.file_path}")

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON format in customer data file: {self.file_path}") from exc

        if not isinstance(data, list):
            raise ValueError(f"Expected a JSON list of customer objects in {self.file_path}")

        customers: list[Customer] = []
        for item in data:
            if not isinstance(item, dict):
                continue
            customers.append(
                Customer(
                    id=int(item["id"]),
                    name=str(item["name"]),
                    email=str(item["email"]),
                    phone=str(item["phone"]),
                    status=str(item.get("status", "active")),
                )
            )

        return customers
