N = 12
a, b = 0, 1
s = 0

while b < N:
	t = a + b
	a = b
	b = t
	if b < N and b % 2 == 0:
		s += b

print(s)