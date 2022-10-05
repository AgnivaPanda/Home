def add  (m , n , name , num) :
	i = 0
	while (i < len(name)) :
		if (name[i] == m) :
			num[i] = num[i] + n
			print("UPDATED Item" , name[i])
			print("\n" , end = "")
			return 0
		i = i + 1
	name.append(m)
	num.append(n)
	print("ADDED Item" , m)
	return 0


def delete (m , n , name , num) :
	i = 0
	while (i < len(name)) :
		if (name[i] == m) :
			if (num[i] >= n) :
				num[i] = num[i] - n
				print("DELETED Item" , m)
				return 0
			elif (num[i] < n) :
				print(f"Item {m} could not be DELETED")
				return 0
				
		i = i + 1
	print(f"Item {m} does not exist")
	return 0

def total(num) :
	sum = 0
	for i in num :
		sum = sum + i
	print("Total Items in Inventory:" , sum)

t = int(input(""))
if (t >= 1 and t <= 25) :
	while (t >0) :
		n = int(input(""))
		name = []
		num = []
		if (n >= 1 and n<= 100) :
			while (n >0) :
				str = input("")
				x = str.split(" ")
				name.append(x[0])
				num.append(int(x[1]))
				n = n - 1
			
			m = int(input(""))
			
			if (m>= 1 and m <= 100) :
				while (m > 0) :
					str1 = input("")
					y = str1.split(" ")
					if (y[0] == "ADD") :
						if (int(y[2]) >= 1 and int(y[2]) <= 100) :
							add(y[1] , int(y[2]) , name , num)
					elif (y[0] == "DELETE") :
						if (int(y[2]) >= 1 and int(y[2]) <= 100):
							delete(y[1] , int(y[2]) , name , num)
					
					m = m - 1
		total(num)
		t = t - 1
