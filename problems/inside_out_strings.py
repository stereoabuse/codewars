##  Inside Out Strings
##  6 kyu
##  https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5


def flip_word(word):
    if len(word) == 1:
        return word
    elif len(word) % 2 != 0 :
        return word[:len(word)//2][::-1] + word[len(word)//2] + word[-len(word)//2 +1:][::-1]
    else:
        return word[:len(word)//2][::-1] + word[-len(word)//2:][::-1]
    
def inside_out(st):
    return ' '.join(flip_word(word) for word in st.split(' '))
    