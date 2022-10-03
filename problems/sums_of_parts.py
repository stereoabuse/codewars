##  Sums of Parts
##  6 kyu
##  https://www.codewars.com/kata/5ce399e0047a45001c853c2b


def parts_sums(ls):
    answer = [0]
    for item in ls[::-1]:
        answer.append(answer[-1] + item)
    return answer[::-1]
    