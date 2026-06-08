"""
logaudit — scan a Linux log file for high-verbosity debug patterns and oversized files.

Inspired by a real SSSD incident: a workstation filled to 100% disk because SSSD
was running in high-verbosity debug mode (0x0070), producing ~250GB of logs.
This tool surfaces that kind of failure earlier by counting log-level frequencies
and flagging the file size against a threshold.

Fill in across the week — the TODOs map to the evening plan.
"""

import re
from collections import Counter
from pathlib import Path


# TODO Evening 1: open samples/sssd.log and print each line.
# Hints:
#   - Use a `with open(path) as f:` block (the `with` statement closes the file
#     for you when the block ends — covered in Evening 1 theory).
#   - Iterate the file object directly: `for line in f:` reads it line by line
#     without loading the whole file into memory.


# TODO Evening 2: parse each line, extract the log level, count with Counter.
# Hints:
#   - Log lines look like:
#       (Tue Mar 11 09:15:22 2025) [sssd[be[lan.example.com]]] [INFO] message...
#       (Tue Mar 11 09:15:23 2025) [sssd[be[lan.example.com]]] [DEBUG] (0x0070) trace
#   - A regex like r"\[(DEBUG|INFO|WARN|FATAL)\]" will capture the level in group 1.
#   - Feed each matched level into a `collections.Counter` and print the totals.


def count_levels(path: str) -> Counter:
    """Return a Counter of log-level occurrences in the file at `path`."""
    # CODE ADDED FOR EVENING 2 BUILD 👇🏾
    pattern =re.compile(r"\[(DEBUG|INFO|WARN|FATAL)\]")
    counts = Counter()
    with open(path) as f: 
        for line in f: 
            match = pattern.search(line)
            if match: 
                level = match.group(1)
                counts[level] += 1 

    return counts 


# TODO Evening 3: file-size check and exit codes.
# Hints:
#   - `Path(path).stat().st_size` gives bytes; divide by 1024 * 1024 for MB.
#   - If size_mb > threshold_mb OR DEBUG ratio is high, return exit code 1.
#   - Otherwise return 0. Monitoring systems read these exit codes.


def run(args) -> int:
    """Entry point called from __main__.py once argparse is wired up (Evening 3)."""
    # TODO Evening 3: implement this.
    raise NotImplementedError("Implement on Evening 3")

# CODE ADDED FROM EVENING 1 BUILD 👇🏾
#if __name__ == "__main__": 
   # log_path = "samples/sssd.log" 
   # with open(log_path) as f:
       # for line in f:
          #  print(line, end="")

#UPDATED VERSION FOR EVENING 2 BUILD 
if __name__ == "__main__":
    log_path = "samples/sssd.log"
    counts = count_levels(log_path)
    for level, count in counts.most_common():
        print(f"{level}: {count}")