##  Sort sentence pseudo-alphabetically
##  6 kyu
##  https://www.codewars.com/kata/52dffa05467ee54b93000712


def pseudo_sort(st):
    st = ''.join(char for char in st if char not in '!@#$%^&*(),.?:;"')
    words = st.split()
    upper = sorted([word.strip() for word in words if word[0] == word[0].upper()], reverse=True)
    lower = sorted([word.strip() for word in words if word[0] == word[0].lower()])
    sentence = lower + upper
    return ' '.join(sentence)
    
