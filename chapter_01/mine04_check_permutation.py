def check_permutation(string):
    char_count = {}
    total_count = 0
    for c in string:
        if c.isalpha():
            char_count[c.lower()] = char_count.get(c.lower(), 0) + 1
            total_count += 1
    n_odd_freq = 0
    for freq in char_count.values():
        if freq % 2 == 1:
            n_odd_freq += 1

    if n_odd_freq > 1:
        return False
    
    if n_odd_freq == 1 and total_count % 2 == 0:
        return False
    
    return True


import unittest

class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        check_permutation,
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
            