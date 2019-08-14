def knap(arr,v,n,max_cap):
	result=0
	if n==0 or max_cap==0:
		result=0
	elif arr[n-1]>max_cap:
		result=knap(arr,v,n-1,max_cap)
	else:
		a=v[n-1]+knap(arr,v,n-1,max_cap-arr[n-1])
		b=knap(arr,v,n-1,max_cap)
		result=max(a,b)
	return result
	
p=knap([1,2,4,2,5],[5,3,5,3,2],5,10)
print(p)
