##  Mexican Wave
##  6 kyu
##  https://www.codewars.com//kata/58f5c63f1e26ecda7e000029


def wave(people):
    ans = []
    for i in range(len(people)):
        p = [c for c in people]
        if p[i] != ' ':
            p[i] = p[i].upper()
            ans.append(''.join(p))
    return ans