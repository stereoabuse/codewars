##  Explosive Sum
##  4 kyu
##  https://www.codewars.com/kata/52ec24228a515e620b0005ef


def exp_sum(n):
    nums = list(range(1,n+1))
    parts = [1] + [0] * n
    for c in nums:
        for i, x in enumerate(range(c, n + 1)):
            parts[x] += parts[i]
    return parts[n]