t = int(input(""))
if (t >= 1 and t <= 25):
    while (t > 0):
        a = input("")
        a = a.lower()
        l = len(a)
        if (l >= 2 and l <= 100):
            b = ""
            i = -1
            while (i >= -l):
                b = b + a[i]
                i = i - 1
            if (a == b):
                print("It is a palindrome")
            else:
                print("It is not a palindrome")

        t = t - 1