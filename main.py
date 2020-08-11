number = 235

def Calc16Bit(number):
    anslist = []
    hexint = 0
    hexdictionary = {1:16,'F':15,'E':14,'D':13,'C':12,'B':11,'A':10}

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

        elif number < 10 and number != 0:
            anslist.append(number)
            number -= number

        else:
            pass
    
    return anslist

def DataOf16Bit(number):
    hexdictionary = {1:16,'f':15,'e':14,'d':13,'c':12,'b':11,'a':10}
    hexval = ''

    ans = Calc16Bit(number)
    print(ans)
    for i in ans:

        if i >= 10:
            ansactual = Calc16Bit(i)
            for j in ansactual:
                hexval += str(j)

        elif i != 0:
            hexval += str(i)

    return hexval


print(DataOf16Bit(number))


