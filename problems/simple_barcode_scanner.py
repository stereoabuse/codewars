##  Simple Barcode Scanner
##  6 kyu
##  https://www.codewars.com/kata/55f4ad47ada1dd22f1000088


codes = {'0001101': 0,
'0011001': 1,
'0010011': 2,
'0111101': 3,
'0100011': 4,
'0110001': 5,
'0101111': 6,
'0111011': 7,
'0110111': 8,
'0001011': 9}

def barcode_scanner(barcode):
    L = barcode[3:len(barcode) // 2-2]
    R = ''
    for char in barcode[len(barcode) // 2+3:-3]:
        if char == '0':
            R += '1'
        else:
            R += '0'
    Ls = [L[i:i+7] for i in range(0, len(L), 7)]
    Rs = [R[i:i+7] for i in range(0, len(R), 7)]
    return ''.join(str(codes[x]) for x in Ls) + ''.join(str(codes[x]) for x in Rs)
