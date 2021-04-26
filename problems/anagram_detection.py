##  Anagram Detection
##  7 kyu
##  https://www.codewars.com/kata/529eef7a9194e0cbc1000255


# write the function is_anagram
def is_anagram(test, original):
    test_list = sorted([item.lower() for item in test])
    original_list = sorted([item.lower() for item in original])
    return test_list == original_list