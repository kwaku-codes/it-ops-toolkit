# it-ops-toolkit

A small Python CLI for IT operations diagnostics. Two subcommands:

- **`logaudit`** — scans a Linux log file for high-verbosity debug patterns and oversized files.
- **`assetage`** — reads a Snipe-IT CSV export and flags machines older than a configurable threshold.

## Why I built this

A learning exercise built off the back of two real problems I encountered in IT support at Thought Machine:

- A Linux workstation filled to 100% disk because SSSD was running in high-verbosity debug mode (`0x0070`), generating 250GB of logs that re-filled the disk within an hour of being cleared. The `logaudit` tool would have caught this earlier.
- A pattern of long compile-time tickets that traced back to ageing under-powered workstations. The `assetage` tool surfaces refresh candidates from a Snipe-IT export — exactly the kind of report that drove a Lenovo ThinkStation procurement project I led.

This is a learning project, not production code.

## Install

```bash
git clone <repo-url>
cd it-ops-toolkit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Scan a log file for debug-mode patterns and oversized files
python -m it_ops_toolkit logaudit --path samples/sssd.log --threshold-mb 100

# Audit asset CSV for machines older than 3 years
python -m it_ops_toolkit assetage --path samples/assets.csv --max-age-years 3 --format markdown
```

## What I'd add next

- Read live `/var/log` paths rather than only sample files.
- Pull asset data directly from the Snipe-IT API rather than a CSV export.
- A `licensecheck` subcommand for dormant SaaS account detection.
- More test coverage and CI.

## Stack

Python 3.11+, standard library only for the core tools, `pytest` for testing.
