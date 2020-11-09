##  Consecutive strings
##  6 kyu
##  https://www.codewars.com//kata/56a5d994ac971f1ac500003e


def longest_consec(starr, k):
    longest = ''
    if k > len(starr) or k < 1:
        return longest
    for i in range(0, len(starr)):
        current = ''.join(starr[i:i+k])
        if len(current) > len(longest):
            longest = current
    return longest