##  Complementary DNA
##  7 kyu
##  https://www.codewars.com//kata/554e4a2f232cdd87d9000038


def DNA_strand(dna):
    the_strand = ''
    for letter in dna:
        if letter == 'A':
            the_strand += 'T'
        elif letter == 'T':
            the_strand += 'A'
        elif letter == 'C':
            the_strand += 'G'
        else:
            the_strand += 'C'
    return the_strand