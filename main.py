number = 15

def DataOf16Bit(number):
    anslist = []
    hexdictionary = {'f':15,'e':14,'d':13,'c':12,'b':11,'a':10}
    while number != 0:
        for hexletter, value in hexdictionary.items():
            remainder = number % value
            solution = number / value
            if solution >= 1:
                anslist.append(hexletter)
                number -= value
            elif number == 0:
                break
            else:
                anslist.append(number)
                number -= number
            
    
    return anslist

print(DataOf16Bit(number))


