##  Title Case
##  6 kyu
##  https://www.codewars.com//kata/5202ef17a402dd033c000009


def title_case(title, minor_words=''):
    title, minor_words = title.split(), minor_words.lower().split()
    for i, word in enumerate(title):
        if word.lower() in minor_words:
            title[i] = word.lower()
        else:
            title[i] = word.title()

    if title:
        title[0] = title[0].title()
    return ' '.join(title)