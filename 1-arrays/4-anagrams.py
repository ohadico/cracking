from collections import defaultdict


# space: O(n), time: O(n)
def is_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = defaultdict(int)
    for c1, c2 in zip(str1, str2):
        counter[c1] += 1
        counter[c2] -= 1
    return not any(counter.values())


def test_anagrams():
    assert is_anagrams("abc", "bcd") is False
    assert is_anagrams("abbaba", "aaabbb") is True
