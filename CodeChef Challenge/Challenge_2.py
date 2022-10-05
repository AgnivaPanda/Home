t = int(input(""))
while (t >= 1 and t <= 25) :
	a = int(input(""))
	if (a>= 0 and a<= 100) :
			for i in range (0 , a) :
				if(i == 0) :
					print(3 , end = " ")
				elif (i%2 == 0) :
					print(2*i , end = " ")
				elif (i%2 != 0) :
					print(i*i , end = " ")
			print("\n" , end = "")
	t = t - 1 