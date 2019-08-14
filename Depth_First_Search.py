from collections import defaultdict
d=defaultdict(list)
x=[[1,2],[2,3],[2,5],[5,4],[5,6]]
#x=[[1,2],[1,3],[2,6],[3,4],[3,5]]
tbr=x[:]
val=[100,200,100,500,100,600]
#val=[1,2,3,4,5,6]
print(val)
for i in x:
	k=i[0]
	v=i[1]
	d[k].append(v)
	d[v].append(k)
fin={}
l=d.keys()
for i,j in zip(l,val):
	fin[i]=j
visited=['f']*len(val)
v=visited[:]
print(d)
print(visited)