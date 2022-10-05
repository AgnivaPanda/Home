t = int(input(""))
if (t >= 1 and t <= 25) :
	while (t > 0) :
		l = int(input(""))
		if (l >= 8 and l <= 50) :
			a = input("")
			list1 = a.split(" ")
			i = 0
			while (i < l) :
				list1[i] = int(list1[i])
				i = i + 1
				
			x = -1 
			while (x >= -l) :
				print(list1[x] , end = " ") 
				x = x - 1
			print("\n" , end = "")
			
			i = 0
			while (i < l) :
				if(i != 0 and i%3 == 0) :
					print(list1[i] + 3 , end = " ")
				i = i + 1
			print("\n" , end = "")
					
			i = 0
			while (i < l) :
				if(i != 0 and i%5 == 0) :
					print(list1[i]-7 , end = " ")
				i = i + 1
			print("\n" , end="")
			
			sum = 0
			j = 3
			while (j <= 7) :
				sum = sum + list1[j]
				j = j + 1
				
			print(sum , end = "\n")
			
		t = t - 1