"""Script splitting engine.

This module splits long scripts into TTS-safe segments while trying
to preserve complete sentences and natural pauses.
"""

import re


def split_text(text: str, max_chars: int = 500) -> list[str]:
    """
    Split a long text into segments suitable for text-to-speech.

    The function tries to:
    - keep complete sentences together;
    - avoid exceeding max_chars;
    - split very long sentences by words if necessary;
    - remove unnecessary whitespace.

    Args:
        text: Text that will be divided into segments.
        max_chars: Maximum number of characters per segment.

    Returns:
        A list of text segments.
    """

    if not text or not text.strip():
        return []

    if max_chars <= 0:
        raise ValueError("max_chars must be greater than 0")

    # Normalize spaces and line breaks.
    cleaned_text = re.sub(r"\s+", " ", text).strip()

    # Split after common sentence-ending punctuation.
    sentences = re.split(r"(?<=[.!?])\s+", cleaned_text)

    segments = []
    current_segment = ""

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        # If a single sentence is too long, split it by words.
        if len(sentence) > max_chars:
            if current_segment:
                segments.append(current_segment.strip())
                current_segment = ""

            words = sentence.split()
            temporary_segment = ""

            for word in words:
                candidate = (
                    f"{temporary_segment} {word}".strip()
                    if temporary_segment
                    else word
                )

                if len(candidate) <= max_chars:
                    temporary_segment = candidate
                else:
                    if temporary_segment:
                        segments.append(temporary_segment.strip())

                    temporary_segment = word

            if temporary_segment:
                current_segment = temporary_segment

            continue

        candidate = (
            f"{current_segment} {sentence}".strip()
            if current_segment
            else sentence
        )

        if len(candidate) <= max_chars:
            current_segment = candidate
        else:
            if current_segment:
                segments.append(current_segment.strip())

            current_segment = sentence

    if current_segment:
        segments.append(current_segment.strip())

    return segments