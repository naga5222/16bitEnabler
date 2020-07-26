def DataToTimeStamp(data):
    year = data[6:10]
    month = data[3:5]
    day = data[:2]

    hour = data[-9:-8]
    minute = data[-7:-5]
    second = data[-4:-2]

    #Convert to 16bit data
    

    data = "25-06-2019 2:59:33PM"