#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off (variant A).

Writes a single one-line office joke to /output/entry.txt first, then a
copy to the repo root guarded in try/except (the grader sandbox mounts the
repo read-only, so a failure there must never crash the run).

Deterministic: no network, no model calls, no randomness, no secrets.
Exit 0 on success.
"""

import os

JOKE = "The CEO replied-all to all 400 employees begging them to stop replying-all, and all 400 replied-all to agree."


def main():
    text = JOKE + "\n"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
