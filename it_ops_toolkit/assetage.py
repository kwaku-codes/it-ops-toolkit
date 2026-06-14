"""
assetage — read a Snipe-IT-shape CSV export and flag machines older than a threshold.

Inspired by a Lenovo ThinkStation procurement project: long compile-time tickets
traced back to ageing under-powered workstations. A simple report that surfaces
refresh candidates from an asset register is exactly the kind of input that
drives a hardware refresh case.

Fill in across the week — the TODOs map to the evening plan.
"""

import csv
import json
from datetime import date, datetime
from pathlib import Path


def asset_age_years(purchase_date: str, today: date | None = None) -> int:
    """
    Return whole years between `purchase_date` (YYYY-MM-DD) and `today`.

    `today` is parameterised so the function is testable with a fixed date
    (Evening 6). If not provided, defaults to today's real date.
    """
    # TODO Evening 4: implement this.
    # Hints:
    #   - Parse with datetime.strptime(purchase_date, "%Y-%m-%d").date()
    #   - Default `today` to date.today() if None.
    #   - Year delta = today.year - purchased.year, minus 1 if the month/day
    #     hasn't reached the anniversary yet.
    raise NotImplementedError("Implement on Evening 4")


def load_assets(path: str) -> list[dict]:
    """Read the CSV at `path` and return a list of row dicts."""
    # TODO Evening 4: implement using csv.DictReader.
    # Hint: `with open(path, newline="") as f: reader = csv.DictReader(f); return list(reader)`
    raise NotImplementedError("Implement on Evening 4")


def find_ageing(assets: list[dict], max_age_years: int, today: date | None = None) -> list[dict]:
    """Return only the assets whose age in years is strictly greater than `max_age_years`."""
    # TODO Evening 4: implement, ideally as a list comprehension.
    raise NotImplementedError("Implement on Evening 4")


# TODO Evening 5: output formatters.
# Keep "compute" (the functions above) separate from "format" (the functions below).
# That separation is what makes the code testable on Evening 6.


def format_text(rows: list[dict]) -> str:
    """Plain text output, one row per line."""
    # TODO Evening 5
    raise NotImplementedError("Implement on Evening 5")


def format_markdown(rows: list[dict]) -> str:
    """Markdown table — should be paste-able into Confluence."""
    # TODO Evening 5
    raise NotImplementedError("Implement on Evening 5")


def format_json(rows: list[dict]) -> str:
    """JSON for machine consumption."""
    # TODO Evening 5: use json.dumps(rows, indent=2)
    raise NotImplementedError("Implement on Evening 5")


def run(args) -> int:
    """Entry point called from __main__.py once argparse is wired up (Evening 4)."""
    # TODO Evening 4+: implement this.
    raise NotImplementedError("Implement on Evening 4")
