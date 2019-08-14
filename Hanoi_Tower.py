def hanoi(s,d,e,n):
	if n<=0:
		return 
	else:
		hanoi(s,e,d,n-1)
		print(s,'=>',d)
		hanoi(e,d,s,n-1)

hanoi('a','c','b',3)