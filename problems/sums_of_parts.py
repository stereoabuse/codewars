##  Sums of Parts
##  6 kyu
##  https://www.codewars.com/kata/5ce399e0047a45001c853c2b


def parts_sums(ls):
    ans = []
    current_sum = sum(ls)
    ans.append(current_sum)
    for item in ls:
        ans.append(current_sum - item)
        current_sum -= item
    return ans