##  Human readable duration format
##  4 kyu
##  https://www.codewars.com//kata/52742f58faf5485cae000b9a


def format_duration(seconds):
    

    times = {'year': 31536000, 'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}
    answers = []

    for time, amount in times.items():

        total = seconds // amount

        if total == 1:
            answers.append(f'{total} {time}')
        elif total > 1:
            answers.append(f'{total} {time}s')
        seconds -= total * amount


    if len(answers) == 0:
        return 'now'
    elif len(answers) == 1:
        return answers[0]
    elif len(answers) == 2:
        return f'{answers[0]} and {answers[1]}'
    else:
        return f"{', '.join(answers[:-1])} and {answers[-1]}"

    
format_duration(3662)