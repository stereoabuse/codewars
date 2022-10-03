##  Reversing Words in a String
##  8 kyu
##  https://www.codewars.com/kata/57a55c8b72292d057b000594


def reverse(st):
    # Your Code Here
    return ' '.join(st.split()[::-1])