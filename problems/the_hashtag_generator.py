##  The Hashtag Generator
##  5 kyu
##  https://www.codewars.com/kata/52449b062fb80683ec000024


# hashtag generator
def generate_hashtag(s):
    if not s:
        return False
    s = ''.join(i.capitalize() for i in s.strip().split(' ') if i)
    if not s.startswith('#'):
        s = '#' + s
    return s if len(s) <= 140 else False