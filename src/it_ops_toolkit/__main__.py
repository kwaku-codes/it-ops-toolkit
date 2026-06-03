"""
Entry point for the it-ops-toolkit CLI.

Run with: python -m it_ops_toolkit <subcommand> [options]

This file is a SCAFFOLD. Fill it in across the week — the TODOs map to the
evening plan in the project notes.
"""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="it-ops-toolkit",
        description="Small IT operations diagnostics CLI.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # TODO Evening 3: add the `logaudit` subcommand with --path and --threshold-mb
    # logaudit_parser = subparsers.add_parser("logaudit", help="Scan a log file for debug-mode patterns.")
    # logaudit_parser.add_argument("--path", required=True, help="Path to the log file.")
    # logaudit_parser.add_argument("--threshold-mb", type=int, default=100, help="Flag files larger than this.")

    # TODO Evening 4: add the `assetage` subcommand with --path, --max-age-years, --format
    # assetage_parser = subparsers.add_parser("assetage", help="Audit asset CSV for ageing machines.")
    # assetage_parser.add_argument("--path", required=True, help="Path to the CSV export.")
    # assetage_parser.add_argument("--max-age-years", type=int, default=3, help="Threshold in years.")
    # assetage_parser.add_argument("--format", choices=["text", "markdown", "json"], default="text")

    args = parser.parse_args()

    # TODO Evening 3+: dispatch to the right command handler
    # if args.command == "logaudit":
    #     return run_logaudit(args)
    # if args.command == "assetage":
    #     return run_assetage(args)

    print("Hello from it-ops-toolkit. Fill me in across the week.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
