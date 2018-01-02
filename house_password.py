def checkio(data):


    #replace this for solution
    # my
    # import re
    # if len(data) >= 10:
    #     if data.isalnum():
    #         if re.match(r'.*[0-9].*', data):
    #             if re.match(r'.*[a-z].*', data):
    #                 if re.match(r'.*[A-Z].*', data):
    #                     return True
    # return False

    # speedy
    import re

    if re.search("[a-z]",data) and re.search("[A-Z]",data) and re.search("[0123456789]",data) and len(data)>=10:
        return True
    return False
    # return True or False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print(checkio('A1213pokl'))
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
