##  Counting Duplicates
##  6 kyu
##  https://www.codewars.com//kata/54bf1c2cd5b56cc47f0007a1


def duplicate_count(text):
    text_dict, total = {}, 0
    for char in text.lower():
        if char not in text_dict:
            text_dict[char] = 1
        elif char in text_dict:
            text_dict[char] += 1
    for key, value in text_dict.items():
        if value >=2:
            total +=1
    return total