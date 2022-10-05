def dec_to_binary(a, l1, count):
    if (count < 8):
        l1.append(a % 2)
        count += 1
        a = a // 2
        dec_to_binary(a, l1, count)
    lb = 0
    ub = 7
    while (lb < ub):
        temp = l1[lb]
        l1[lb] = l1[ub]
        l1[ub] = temp
        lb += 1
        ub -= 1

    return l1


t = int(input(""))
if (t >= 1 and t <= 25):
    while (t > 0):
        a = int(input(""))
        if (a >= 0 and a <= 255):
            count = 0
            l1 = []
            res = dec_to_binary(a, l1, count)
            for i in res:
                print(i, end="")
            print("\n", end="")
        t = t - 1