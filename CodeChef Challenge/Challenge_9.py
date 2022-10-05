def get_top (l1) :
	i = 0
	while (i < len(l1)) :
		j = 0
		while (j < len(l1) - 1) :
			if (ord(l1[j+1][0]) < ord(l1[j][0])) :
				temp = l1[j+1]
				l1[j+1] = l1[j]
				l1[j] = temp
			elif (ord(l1[j+1][0]) == ord(l1[j][0])) :
				if(ord(l1[j+1][1]) < ord(l1[j][1])) :
					temp = l1[j+1]
					l1[j+1] = l1[j]
					l1[j] = temp
			j = j + 1
		i = i + 1 
	for i in l1 :
		print(i , end = " ")
	print("\n" , end = "")


t = int(input(""))
if (t >= 1 and t <= 25) :
	while (t > 0) :
		n = int(input(""))
		score = []
		name = []
		l1 = []
		if (n >= 2 and n<= 100) :
			i = 0
			while (i < n) :
				a = input("")
				l = a.split(" ")
				name.append(l[0])
				score.append(float(l[1]))
				i += 1
				
			maxima = score[0]
			j = 1
			index = 0
			while (j < len(score)) :
				if(score[j] > maxima) :
					maxima = score[j]
					index = j
				elif (score[j] == maxima) :
					l1 = []
					l1.append(j)
				j += 1
			l1.append(index)
		
		l2 = []
		i = 0
		while (i < len(l1)):
			l2.append(name[l1[i]])
			i += 1
		get_top(l2)
		
		t -= 1