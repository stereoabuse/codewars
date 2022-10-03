##  Delete occurrences of an element if it occurs more than n times
##  6 kyu
##  https://www.codewars.com/kata/554ca54ffa7d91b236000023


def delete_nth(order, max_e):
    """create a new list that contains each number of 
    lst at most N times without reordering.
    """
    answer_dict = {}
    answer_list = []
    for number in order:
        if number not in answer_dict:
            answer_dict[number] = 1
        else:
            answer_dict[number] += 1
        if answer_dict[number] <= max_e:
            answer_list.append(number)
            
    return answer_list