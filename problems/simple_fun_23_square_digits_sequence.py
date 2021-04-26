##  Simple Fun #23: Square Digits Sequence
##  6 kyu
##  https://www.codewars.com/kata/5886d65e427c27afeb0000c1


def square_digits_sequence(n):
    sd_list = [n]
    while True:
        num = sum([int(i)**2 for i in list(str(n))])
        sd_list.append(num)
        if sd_list.count(num) == 2:
            return len(sd_list)
        n = num