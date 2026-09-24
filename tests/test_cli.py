"""Integration tests for CLI entrypoint and presentation layer."""

import pytest
from pathlib import Path
from src.cli import main, run_cli, format_table
from src.models import Customer


def test_format_table():
    """AC-06: Verifies tabular ASCII output formatting."""
    customers = [
        Customer(id=1, name="Ana García", email="ana@example.com", phone="123", status="active"),
    ]
    table = format_table(customers)
    assert "ID | Name" in table
    assert "1  | Ana García" in table
    assert "ana@example.com" in table


def test_cli_successful_search(capsys: pytest.CaptureFixture):
    """AC-01, AC-06: Successful search prints table and exits with code 0."""
    code = main(["ana"])
    assert code == 0

    captured = capsys.readouterr()
    assert "Ana García" in captured.out
    assert "ID | Name" in captured.out
    assert captured.err == ""


def test_cli_empty_results(capsys: pytest.CaptureFixture):
    """AC-05: Unmatched query prints informational message and exits with code 0."""
    code = main(["terminoquenoexiste"])
    assert code == 0

    captured = capsys.readouterr()
    assert "No customers found matching 'terminoquenoexiste'." in captured.out
    assert captured.err == ""


def test_cli_validation_error_short_query(capsys: pytest.CaptureFixture):
    """AC-04, NFR-03: Short query emits error to stderr and exits with code 1."""
    code = main(["a"])
    assert code == 1

    captured = capsys.readouterr()
    assert "Error: Search query must contain at least 2 non-whitespace characters." in captured.err


def test_cli_validation_error_whitespace(capsys: pytest.CaptureFixture):
    """AC-04, NFR-03: Whitespace query emits error to stderr and exits with code 1."""
    code = main(["   "])
    assert code == 1

    captured = capsys.readouterr()
    assert "Error: Search query must contain at least 2 non-whitespace characters." in captured.err


def test_cli_file_not_found(capsys: pytest.CaptureFixture):
    """NFR-03: Non-existent data file emits error to stderr and exits with code 1."""
    code = main(["ana", "--file", "nonexistent_file.json"])
    assert code == 1

    captured = capsys.readouterr()
    assert "Error: Unable to load data file" in captured.err
