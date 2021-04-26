##  Simple Fun #258: Is Divisible By 6
##  6 kyu
##  https://www.codewars.com/kata/5911385598dcd432ae000004


def is_divisible_by_6(s):

      return [str(int(s.replace("*", str(i)))) for i in range(10) if int(s.replace("*", str(i))) % 6 == 0]