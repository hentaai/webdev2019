def main():
	s = 109
	sm = -109
	v = input()
	t = input()

	v = int(v);
	t = int(t)

	n = v*t 

	if v > 0:
		if n < s:
			print(str(n))
		elif n > s and n < 2*s:
			print(str(n-s))
		else:
			print(str(n-s*2))
	else:
		if n > sm:
			print(str(n-sm))
		elif n < sm and n > sm:
			print(str(n-sm*2))
		else:
			print(str(n-sm*3))



if __name__ == '__main__':
	main()