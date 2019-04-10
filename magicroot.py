a=64
x=1
n=0
prev=9999
while(n<30):
	m=a/x
	y=(x+m)/2
	n+=1
	x=y
	if prev==y:
		break
	prev=y
	print(y)
