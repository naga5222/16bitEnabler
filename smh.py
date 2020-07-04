data = "25-06-2019 2:59:33PM"
number = 420555888

def DataToTimeStamp(data):
    year = data[6:10]
    month = data[3:5]
    day = data[:2]

    hour = data[-9:-8]
    minute = data[-7:-5]
    second = data[-4:-2]

    #Convert to 16bit data

def DataOf16Bit(number):
    anslist = []
    hexdictionary = {a:10,b:11,c:12,d:13,e:14,f:15}
    for i in hexdictionary:
            solution = number / hexdictionary[i]
            while solution >= 1:
                anslist.append(i)
                solution - 1 
    if remainder != 0:
        pass
    else:
        pass

DataToTimeStamp(data)


