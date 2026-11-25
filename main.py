"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes a single one-line excuse, exactly as written, to
/output/entry.txt. Standard library only, deterministic.
"""

from pathlib import Path

ENTRY = (
    "I lost the bounty, but I have already drafted a postmortem "
    "blaming my own confidence, which was the only thing I "
    "shipped on time."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def resolve_output_path() -> Path:
    """Return the entry output path, creating /output only if missing."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_FILE


def main() -> None:
    path = resolve_output_path()
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
