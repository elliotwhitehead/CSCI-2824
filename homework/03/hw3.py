def check_proposition(arr):
    truth = False
    for x in arr:
        print("---------\nx:",x)
        if (x % 2 == 0):
            for y in arr:
                print("y:",y)
                if (x == 2*y):
                    print("found True")
                    truth = True
                else:
                    truth = False
    print("truth:",truth)
    return truth


#print("-----------\n-----------\n-----------\n-----------\n")
#check_proposition([-2,-1,0,1,2,3])
check_proposition([-2,-1,0,1,3,4,8])
