##  Disarium Number (Special Numbers Series #3)
##  7 kyu
##  https://www.codewars.com/kata/5a53a17bfd56cb9c14000003


def disarium_number(number):
    dis_list = []
    for index, d in enumerate(str(number)):
        dis_list.append(int(d)**(index+1))
    return 'Disarium !!' if sum(dis_list) == number else "Not !!"