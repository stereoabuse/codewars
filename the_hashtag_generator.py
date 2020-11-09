##  The Hashtag Generator
##  5 kyu
##  https://www.codewars.com//kata/52449b062fb80683ec000024


def generate_hashtag(s):
    s1 = "#" + "".join([item.capitalize() for item in s.split()])
    return s1 if s1 != "#" and len(s1) < 140 else False