def urlify(string, str_len):
    string = list(string)
    end_pointer = len(string) - 1
    start_pointer = str_len - 1

    while start_pointer >= 0:
        if string[start_pointer] != " ":
            string[end_pointer] = string[start_pointer]
            end_pointer -= 1
        else:
            for c in "02%":
                string[end_pointer] = c
                end_pointer -= 1
        start_pointer -= 1
    
    return "".join(string)

print(len("Mr John Smith   "))
print(len("Mr%20John%20Smith"))



def ctci_urlify(string, str_len):
    string = list(string)
    count_space = 0
    SPACE = " "
    
    for i in range(str_len):
        c = string[i]
        if c == SPACE:
            count_space += 1
    
    final_len = str_len + count_space * 2
    index = final_len - 1
    if str_len < len(string) : string[str_len] = "p"
    for i in reversed(range(str_len)):
        char = string[i]
        if char == SPACE:
            string[index] = "0" 
            string[index - 1] = "2"
            string[index - 2] = "%"
            index -= 3
        else:
            string[index] = char
            index -= 1
    return "".join(string)



import unittest
# O(N)
class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith    ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify, ctci_urlify]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()