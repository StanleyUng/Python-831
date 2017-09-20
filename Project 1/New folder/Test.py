def convert(x): 
    if (str(x).isdigit()):
        return int(x)
    else:
        return x

with open("nums.txt", "r") as ins:
    for line in ins:
        num = list(map(convert, list(line)))
        print(num)

        if (num[0] == '$'):
            print('$$$$$')
            index = 1
            while(num[index] == '*'):
                index = index + 1
                print("*")
            if(num[index] != 0 or num[index] == 0 and num[index + 1] == '.'): # No an * anymore
                print("af")
            else:
                print("invalid")




        else:
            print('ripperino')