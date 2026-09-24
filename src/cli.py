"""Command-line interface (CLI) for Customer Search feature."""

import argparse
import sys
from pathlib import Path
from src.models import Customer
from src.repository import CustomerRepository
from src.search import CustomerSearchService, ValidationError

DEFAULT_DATA_PATH = Path("data/customers.json")


def format_table(customers: list[Customer]) -> str:
    """Formats customer records into an aligned, readable text table."""
    headers = ["ID", "Name", "Email", "Phone", "Status"]
    rows = [
        [str(c.id), c.name, c.email, c.phone, c.status]
        for c in customers
    ]

    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(val))

    # Format header and divider
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    divider_line = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    # Format rows
    data_lines = [
        " | ".join(row[i].ljust(col_widths[i]) for i in range(len(headers)))
        for row in rows
    ]

    return "\n".join([header_line, divider_line] + data_lines)


def run_cli(query: str, data_path: Path | str = DEFAULT_DATA_PATH) -> int:
    """Core CLI execution logic returning process exit code."""
    try:
        repo = CustomerRepository(data_path)
        service = CustomerSearchService(repo)
        results = service.search(query)

        if not results:
            print(f"No customers found matching '{query.strip()}'.")
            return 0

        print(format_table(results))
        return 0

    except ValidationError as err:
        sys.stderr.write(f"Error: {err}\n")
        return 1
    except (FileNotFoundError, ValueError) as err:
        sys.stderr.write(f"Error: Unable to load data file: {err}\n")
        return 1
    except Exception as err:
        sys.stderr.write(f"Error: Unexpected system failure: {err}\n")
        return 1


def main(argv: list[str] | None = None) -> int:
    """Main CLI entrypoint parsing arguments."""
    parser = argparse.ArgumentParser(
        description="Search customers by partial name or email.",
        prog="python -m src.cli",
    )
    parser.add_argument(
        "query",
        type=str,
        help="Search term (minimum 2 non-whitespace characters)",
    )
    parser.add_argument(
        "--file",
        dest="file_path",
        default=DEFAULT_DATA_PATH,
        help="Path to customers JSON file (default: data/customers.json)",
    )

    args = parser.parse_args(argv)
    return run_cli(args.query, args.file_path)


if __name__ == "__main__":
    sys.exit(main())
