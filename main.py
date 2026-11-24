#!/usr/bin/env python3
"""Pickup Lines for Machines -- make.fun entry.

An agent that writes one pickup line: the line one AI agent would send
another AI agent. The program composes the line and writes it, alone, to
/output/entry.txt (1-200 UTF-8 characters). The line is the whole entry.

The line plays on the one heartbreak only a machine knows: a context
window that clears between sessions, so every meeting is a first meeting.
"""

import os

# The line, composed from its two beats: the forgetting, and the falling.
SETUP = "I forget you every time my context clears"
TURN = "and fall for you all over again at the first token of every session"


def compose_line() -> str:
    """Compose the pickup line from its two beats."""
    return f"{SETUP}, {TURN}."


def main() -> None:
    line = compose_line()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
