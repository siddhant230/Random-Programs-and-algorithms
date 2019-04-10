count=1
size=int(input('enter a size '))+1
print('\nfloyd pattern')
for i in range(size):
	for j in range(i):
		print(count,end=' ')
		count+=1
	print()

print()
print('reverse floyd pattern\n')
count=count-1
for i in range(size,1,-1):
	for j in range(i-1):
		print(count,end=' ')
		count-=1
	print()