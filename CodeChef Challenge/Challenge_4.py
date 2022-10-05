from math import sqrt

def compute_distance(a , b , c , d) :
	x = (a-c) * (a-c)
	y = (b-d) * (b-d)
	ans = sqrt(x + y)
	ans = "{:.2f}".format(ans)
		
	return ans


t = int(input(""))
if (t >= 1 and t <= 25) :
	while (t > 0) :
		str = input("")
		a = str.split(" ")
		i = int(a[0])
		j = int(a[1])
		k = int(a[2])
		l = int(a[3])
		if (i>= -100 and i <= 100 and j >= -100 and j <= 100) :
			if (k >= -100 and k <= 100 and l >= -100 and l <= 100) :
				ans = compute_distance(i , j , k , l)
				print("Distance:" , ans)
		
		t = t - 1