# time O(n log n)
# space O(N)

def is_unique_sorting(word):
    word = sorted(word)
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            return False
    return True

# time O(Nˆ2)
# space O(1)
def is_unique_double_for(word):
    for i in range(0, len(word) -1):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True


# time O(Nˆ2)
# space O(1)
def is_unique_bitmap(word):
    set_membership = [0] * 256
    for c in word:
        ascii_representation = ord(c)
        if set_membership[ascii_representation] == 1:
            return False
        set_membership[ascii_representation] = 1
    return True

import time
import unittest
from collections import defaultdict

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_sorting,
        is_unique_double_for,
        is_unique_bitmap
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()


