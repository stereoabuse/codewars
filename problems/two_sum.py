##  Two Sum
##  6 kyu
##  https://www.codewars.com/kata/52c31f8e6605bcc646000082


def two_sum(numbers, target):
    for i, num in enumerate(numbers):
        for j, num2 in enumerate(numbers[:i] + numbers[i:]):
            if target - num == num2:
                if num == num2:
                    return [i, j + 1]
                else:
                    return [i, j]