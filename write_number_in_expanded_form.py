##  Write Number in Expanded Form
##  6 kyu
##  https://www.codewars.com//kata/5842df8ccbd22792a4000245


def expanded_form(num):
    answers = [
        (str(num)[i] + "0" * (len(str(num)[i:]) - 1))
        for i in range(len(str(num)))
        if str(num)[i] != "0"
    ]
    return " + ".join(answers)