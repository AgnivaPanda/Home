def check (a) :
	v = False
	i = 1
	while (i < len(a)):
		o = ord(a[i])
		if (o>= 65 and o <= 90) :
			v = True
		elif (o >= 97 and o <= 122) :
			v = True
		elif (o == 32) :
			v = True
		else :
			v = False
			break
		i += 1
	return v

t = int(input(""))
if (t >= 1 and t <= 25) :
	while (t >0) : 
		a = input("")
		if (check(a)) :
			l1 = a.split(" ")
			l = len(l1)
			i = 0
			while (i < l) :
				count = 0
				for item in l1[i] :
					if(item != '@') :
						count = count+1

				if (i < l-1) :
					print(count , end = " ")
				elif(i == l-1) :
					print(count)
				i = i + 1
			
		t = t - 1