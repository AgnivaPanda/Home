from functools import reduce

def generate_AP(a , d , n) :
	l = []
	i = 0
	while (i < n) :
		c = a + (i * d)
		l.append(c)
		i = i + 1
	
	for item in l :
		print(item , end = " ")
		
	i = 0
	while (i < len(l)) :
		l[i] = l[i] * l[i]
		i = i + 1
	return l

t = int(input(""))
if (t >= 1 and t <= 25) :
	while (t > 0) : 
		x = input("")
		l = x.split(" ")
		a = int(l[0])
		d = int(l[1])
		n = int(l[2])
		if (a >= 1 and a <= 100) :
			if (d >= 1 and d <= 100) :
				if (n >= 1 and n <= 100) :
					x = generate_AP(a , d , n) 
					print("\n" , end = "")
					
					for i in x :
						print(i , end = " ")
					
					print("\n" , end = "")
					
					print(reduce(lambda a , b: a + b , x ))
		
		t = t - 1
	