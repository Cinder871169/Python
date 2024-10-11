import re
from collections import Counter


def count_words(n):
    word_count = Counter()

    for _ in range(n):
        line = input().strip()
        words = re.findall(r"\b\w+\b", line.lower())

        for word in words:
            clean_word = "".join(filter(str.isalpha, word))
            if clean_word:
                word_count[clean_word] += 1

    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    for word, count in sorted_words:
        print(f"{word} {count}")


n = int(input())
count_words(n)
