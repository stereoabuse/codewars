##  Extract the domain name from a URL
##  5 kyu
##  https://www.codewars.com//kata/514a024011ea4fb54200004b


import re

def domain_name(url):
    return re.match(r'(www\.|http[s]?://)*([a-z0-9-]*)\..*$', url, re.I).group(2)