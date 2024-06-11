class flames:
    input1 = input("enter the name1:")
    input2 = input("enter the name2:")
    input1 = input1.lower()
    input2 = input2.lower()
    input1 = list(input1)
    input2 = list(input2)
    for i in input1:
        if i in input2:
            input1.remove(i)
            input2.remove(i)
    count = len(input1) + len(input2)
    print(count)
    flames = ["Friends","Love","Affection","Marriage","Enemy","Siblings"]
    while len(flames) > 1:
        c = count % len(flames)
        sc = c - 1
        if sc >= 0:
            left = flames[:sc]
            right = flames[sc+1:]
            flames = right + left
        else:
            flames = flames[:len(flames)-1]
    print(flames)
flames()

