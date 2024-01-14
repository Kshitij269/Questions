from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word_1 = Counter(word1)
        word_2 = Counter(word2)
        return (sorted(word_1.values()) == sorted(word_2.values()) and
                sorted(word_1.keys()) == sorted(word_2.keys()))
