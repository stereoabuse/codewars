##  Find the divisors! 
##  7 kyu
##  https://www.codewars.com/kata/544aed4c4a30184e960010f4


def divisors(integer):
    divlist = [i for i in range(2, integer//2 + 1) if integer % i == 0]

    return f'{integer} is prime' if len(divlist) == 0 else divlist
        