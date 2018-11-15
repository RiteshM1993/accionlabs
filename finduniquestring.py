from collections import Counter

def unique():

    string1 = input("enter string1:")
    string2=input("enter string2:")
    string3  = string1 + string2
    list1=[]
    for i in string3:
        if string3.count(i)>1:
            continue
        else:
            list1.append(i)
        str1=''.join(list1)
    print(str1)


unique()