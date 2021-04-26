##  String incrementer
##  5 kyu
##  https://www.codewars.com/kata/54a91a4883a7de5d7800009c


def increment_string(string):    
    nums = '0123456789'
    if len(string) == 0:
        return str(1)
    if all(n.isdigit() for n in string):
        return str(int(string) + 1).zfill(len(string))
    elif not string:
        return str(1)
    elif not string[-1].isdigit():
        return string + str(1)
    else:
        end_nums, end_string = '', ''
        for index, char in enumerate(string[::-1]):
            if char.isdigit():
                end_nums += char
            else:
                return string[:-index] + str(int(end_nums[::-1])+1).zfill(len(end_nums))