"""Entry for "The Word You'd Delete From the Dictionary".

The single word I would erase from the dictionary forever is "whom":
a pronoun nobody uses correctly, everybody second-guesses, and whose
only real job is making confident people pause mid-sentence. Delete it
and a thousand grammar arguments end overnight, and nobody would even
notice it was gone -- because nobody was sure it was there correctly
in the first place.

This program writes exactly that one word, and nothing else, to
$OUTPUT_DIR/entry.txt.
"""

import os

WORD = "whom"


def checked_word(word):
    """Return the word only if it is exactly one dictionary word.

    Anything with a space, punctuation, or extra text attached is not a
    single word, so refuse it rather than writing a bad entry.
    """
    cleaned = word.strip()
    if not cleaned or not cleaned.isalpha() or " " in cleaned:
        raise ValueError("entry must be exactly one word")
    return cleaned


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(checked_word(WORD))


if __name__ == "__main__":
    main()
