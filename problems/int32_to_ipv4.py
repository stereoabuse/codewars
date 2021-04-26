##  int32 to IPv4
##  5 kyu
##  https://www.codewars.com/kata/52e88b39ffb6ac53a400022e


def int32_to_ip(int32):
    num = bin(int32)[2:].zfill(32)
    return '.'.join([str(int(num[i:i+8],2)) for i in range(0, len(num), 8)])
