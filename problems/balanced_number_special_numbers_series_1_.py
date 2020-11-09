# Balanced Number (Special Numbers Series #1 )
# 7 kyu


def balanced_num(number):
    length = len(str(number))
    if length % 2 == 0:
        return "Balanced" if sum(int(i) for i in str(number)[:(length-1)//2]) == sum(int(i) for i in str(number)[(length+2)//2:]) else "Not Balanced"
    return "Balanced" if sum(int(i) for i in str(number)[:(length)//2]) == sum(int(i) for i in str(number)[(length+1)//2:]) else "Not Balanced"