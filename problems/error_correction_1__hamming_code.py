##  Error correction #1 - Hamming Code
##  6 kyu
##  https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e


def encode(string):
    s = [str(bin(ord(c))[2:]).zfill(8) for c in string]
    encoded_string = ''.join(['000' if i == '0' else '111' for i in ''.join(s)])
    return encoded_string

def decode(string):
    s = [string[i:i+3] for i in range(0, len(string), 3)]
    decoded_string = ''.join([max(list(item), key=list(item).count) for item in s])
    decoded_string = [int(decoded_string[i:i+8],2) for i in range(0, len(decoded_string), 8)]
    decoded_string = ''.join(chr(i) for i in decoded_string)
    return decoded_string