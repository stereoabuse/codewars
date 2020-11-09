##  Regex validate PIN code
##  7 kyu
##  https://www.codewars.com//kata/55f8a9c06c018a0d6e000132


def validate_pin(pin):
    #return true or false
    if pin.isdigit():
        if len(pin) == 4 or len(pin) ==6:
            return True
        else:
            return False
    else:
        return False
        