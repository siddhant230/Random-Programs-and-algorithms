def partition(arr,l,r):
	pivot=arr[r]
	i=l-1
	
	for j in range(l,r):
		if arr[j]<=pivot:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	
	arr[i+1],arr[r]=arr[r],arr[i+1]
	return i+1
			
			
def quick(arr,l,r):
	if l<r:
		pivot=partition(arr,l,r)
		print(pivot)
		quick(arr,l,pivot-1)
		quick(arr,pivot+1,r)
	

arr=[3,7,4,2,1,9,8,5]
quick(arr,0,len(arr)-1)
print(arr)
				
