##  Valid Spacing
##  7 kyu
##  https://www.codewars.com/kata/5f77d62851f6bc0033616bd8


def valid_spacing(s):
    if s.strip() != s or '  ' in s:
        return False
    return True