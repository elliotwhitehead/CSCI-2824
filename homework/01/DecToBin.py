def DecToBin(num):
    bin_num = []
    if(num):
        while(num):
            bin_num.append(int(num % 2))
            num = int(num / 2)
        bin_num.reverse()
        return bin_num
    # case for DecToBin(0)
    else:
        bin_num.append(0)
    return bin_num