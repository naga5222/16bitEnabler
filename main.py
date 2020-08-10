number = 200
def DataOf16Bit(number):
    anslist = []
    hexval = ''
    hexint = 0
    hexdictionary = {1:16,'f':15,'e':14,'d':13,'c':12,'b':11,'a':10}

    for hexletter, value in hexdictionary.items():

        while number >= 16:              #specific condition needed for non-repetitive 1s
            if anslist == []:
                anslist.append(hexletter)
                hexint += hexletter
                number -= value
            else:
                anslist[0] = hexint + 1
                hexint += 1
                number -= value

        if number >= 10 and value == number:
            anslist.append(hexletter)
            number -= value

        elif number < 10:
            anslist.append(number)
            number -= number

    for i in anslist:
        if i != 0:
            hexval += str(i)
    
    return hexval

print(DataOf16Bit(number))


