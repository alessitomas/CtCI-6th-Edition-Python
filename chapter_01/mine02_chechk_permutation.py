# Time O(n)
# Space O(n)

def check_permutation_hashtable(w1,w2):
    char_freq = {}
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        char_freq[w1[i]] = char_freq.get(w1[i],0) + 1
        char_freq[w2[i]] = char_freq.get(w2[i],0) - 1
    
    for v in char_freq.values():
        if v != 0:
            return False
    
    return True


# Time O(n)
# Space O(1)
def check_permutation_bitmap(w1, w2):
    bitmap = [0] * 128
    if len(w1) != len(w2):
        return False
    
    for i in range(len(w1)):
        bitmap[ord(w1[i])] = bitmap[ord(w1[i])] + 1
        bitmap[ord(w2[i])] = bitmap[ord(w2[i])] - 1

    for v in bitmap:
        if v != 0:
            return False
    
    return True
    


import unittest

class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_hashtable,
        check_permutation_bitmap

    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
