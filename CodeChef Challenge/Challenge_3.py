t = int(input(""))
if (t >= 1 and t <= 25):
    while (t > 0):
        a = int(input(""))
        if (a >= 1 and a <= 100):
            while (a > 0):
                b = 1
                while (b <= a):
                    if (b % 5 == 0):
                        print("#", end="")
                    else:
                        print("*", end="")
                    b = b + 1
                print("\n", end="")
                a = a - 1

        t = t - 1