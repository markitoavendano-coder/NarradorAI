"""NarradorAI - command-line entry point."""

import argparse
from pathlib import Path

from engine.splitter import split_text


def read_text_file(file_path: str) -> str:
    """Read a UTF-8 text file."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return path.read_text(encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description=(
            "Split a text script into smaller segments suitable "
            "for text-to-speech processing."
        )
    )

    parser.add_argument(
        "input_file",
        help="Path to the UTF-8 text file containing the script.",
    )

    parser.add_argument(
        "--max-chars",
        type=int,
        default=500,
        help="Maximum characters per segment. Default: 500.",
    )

    return parser


def main() -> None:
    """Run NarradorAI from the command line."""

    parser = build_parser()
    args = parser.parse_args()

    try:
        text = read_text_file(args.input_file)
        segments = split_text(text, max_chars=args.max_chars)

    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    if not segments:
        print("No text segments were generated.")
        return

    print(f"Generated {len(segments)} segment(s):")
    print()

    for index, segment in enumerate(segments, start=1):
        print(f"[{index}] {segment}")


if __name__ == "__main__":
    main()