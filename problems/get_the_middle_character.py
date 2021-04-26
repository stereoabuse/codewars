##  Get the Middle Character
##  7 kyu
##  https://www.codewars.com/kata/56747fd5cb988479af000028


def get_middle(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return "{}{}".format(s[len(s)//2 -1], s[len(s)//2])
  