t = int(input())
for i in range(t):
	s = input()
	s = s + 'z'
	ans = 10 ** 20
	n = 0
	for i in range( len(s)):
		if s[i].isalpha():
			if i != 0 and s[i - 1].isdigit():
				ans = min(ans, n)
				n = 0
		else:
			n = n * 10 + int(s[i])
	print(ans)
