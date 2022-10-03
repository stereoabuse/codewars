##  Extract the domain name from a URL
##  5 kyu
##  https://www.codewars.com/kata/514a024011ea4fb54200004b


def domain_name(url):
    possible  =  ['www.', 'https://', 'http://']
    for option in possible:
        url = url.replace(option,'')
    return url.split('.')[0]
