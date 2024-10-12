import sys
from typing import List


def count_characters(words: List[str]) -> dict:
    character_count: dict[str] = {}
    for word in words:
        for char in word.lower():
            character_count[char] = (
                character_count[char] + 1 if char in character_count else 1
            )

    return character_count


def print_character_count(character_counts: dict[str]):
    # Leaving all chars in otherwise the total and individual counts will be off
    for character_count in sorted(
        character_counts, key=lambda c: character_counts[c], reverse=True
    ):
        print(
            f"The '{character_count}' character was found {character_counts[character_count]} times"
        )


def print_report(words: List[str], filename: str):
    print(f"--- Begin report of {filename} ---")
    print(f"{len(words)} words were found in the document\n")

    count = count_characters(words)

    print_character_count(count)

    print('--- End report ---')


def main() -> None:
    # TODO: pass in the filename as a param to script
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
        words = text.split()

        print_report(words, "books/frankenstein.txt")


if __name__ == "__main__":
    sys.exit(main())
