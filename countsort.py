def counting_sort(alist, largest):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1
 
    # Find the last index for each element
    print(c)
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    print(c)
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
    print(c)
 
    result = [None]*len(alist)
    print(result)
 
    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    print('############')
    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1
        print(result)
        print(c)
        print('#############')
 
    return result
 
 
#alist = input('Enter the list of (nonnegative) numbers: ').split()
alist=[1,4,1,2,-6,7,5,2]
alist = [int(x) for x in alist]
k = max(alist)
sorted_list = counting_sort(alist, k)
print('Sorted list: ', end='')
print(sorted_list)
