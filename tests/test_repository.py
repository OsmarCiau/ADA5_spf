"""Unit tests for CustomerRepository."""

import json
import pytest
from pathlib import Path
from src.repository import CustomerRepository


def test_repository_loads_valid_customers(tmp_path: Path):
    data = [
        {"id": 1, "name": "Ana", "email": "ana@test.com", "phone": "123", "status": "active"},
        {"id": 2, "name": "Bob", "email": "bob@test.com", "phone": "456", "status": "inactive"},
    ]
    file_path = tmp_path / "customers.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    repo = CustomerRepository(file_path)
    customers = repo.get_all()

    assert len(customers) == 2
    assert customers[0].id == 1
    assert customers[0].name == "Ana"
    assert customers[1].name == "Bob"
    assert customers[1].status == "inactive"


def test_repository_file_not_found(tmp_path: Path):
    non_existent = tmp_path / "does_not_exist.json"
    repo = CustomerRepository(non_existent)
    with pytest.raises(FileNotFoundError, match="Customer data file not found"):
        repo.get_all()


def test_repository_invalid_json(tmp_path: Path):
    corrupt_file = tmp_path / "corrupt.json"
    corrupt_file.write_text("{ this is not valid json", encoding="utf-8")

    repo = CustomerRepository(corrupt_file)
    with pytest.raises(ValueError, match="Invalid JSON format"):
        repo.get_all()


def test_repository_non_list_json(tmp_path: Path):
    obj_file = tmp_path / "object.json"
    obj_file.write_text('{"error": "not a list"}', encoding="utf-8")

    repo = CustomerRepository(obj_file)
    with pytest.raises(ValueError, match="Expected a JSON list"):
        repo.get_all()
