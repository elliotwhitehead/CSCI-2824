def ParityParty(num):
    list = []
    if(num % 2):
        list.append(1)
        list.append(int((num-1)/2))
    else:
        list.append(0)
        list.append(int(num/2))
    
    return list