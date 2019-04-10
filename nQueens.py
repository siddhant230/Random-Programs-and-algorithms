import numpy as np
b=0
while(b==0):
	size=int(input('enter size '))
	if size>8 or size<3:
		print('land chatte ho kya?? sahi value daalo 8 se kam aor 3 se jyaada')
		b=0
	else:
		b=1
board=np.chararray((size,size))
board[:]=''
queens=[b'Q' for x in range(size)]
arr=[]
def fillval(posx,posy,board):
	#fill horizontal and vertical
	for i in range(size):
		if board[posx][i]!=b'Q':
			board[posx][i]=b'x'
		if board[i][posy]!=b'Q':
			board[i][posy]=b'x'
	#fill diagonals
	for i in range(size):
		for j in range(size):
			if board[i][j]!=b'Q':
				if posx-posy==(i-j):
					board[i][j]=b'x'
				if posx+posy==(i+j):
					board[i][j]=b'x'
	return board
count=0
q=0
while queens!=[]:
	queens=[b'Q' for x in range(size)]
	for p in range(size):
		for s in range(size):
			if queens==[]:
				break
			m=queens.pop()
			board[p][s]=m
			board=fillval(p,s,board)
			for i in range(size):
				for j in range(size):
					if board[i][j]!=b'x' and board[i][j]!=b'Q':
						board[i][j]=queens.pop()
						board=fillval(i,j,board)
	
			for k in range(size):
				for m in range(size):
					if board[k][m]!='':
						count+=1					
					if board[k][m]==b'Q':
						q+=1
			if count==(size*size) and q!=size:
				count=0
				board=np.chararray((size,size))
				board[:]=''
				queens=[b'Q' for x in range(size)]
				arr=[]
			count=0
			q=0
fin=[]
for i in range(size):
	for j in range(size):
		if board[i][j]==b'x' or b'Q':
			if board[i][j]==b'x':
				board[i][j]='.'
			fin.append(board[i][j].decode("utf-8"))

for i in range(0,len(fin),size):
	print(fin[i:i+size])
