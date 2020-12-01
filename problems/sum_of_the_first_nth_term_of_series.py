##  Sum of the first nth term of Series
##  7 kyu
##  https://www.codewars.com//kata/555eded1ad94b00403000071


def series_sum(n):
    # Happy Coding ^_^
    if n == 0:
        return '0.00'
    total = 1.0
    for i in range(n-1):
        total += 1/(4 + (3*i))
    answer = str(round(float(round(total,2)),2))
    if len(answer) != 4:
        answer += '0'
    return answer
    