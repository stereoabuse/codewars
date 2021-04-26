##  Sum of Intervals
##  4 kyu
##  https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def sum_of_intervals(intervals):
    seen = set()
    
    for (low,high) in intervals:
        for length in range(low, high):
            seen.add(length)
    
    return len(seen)

