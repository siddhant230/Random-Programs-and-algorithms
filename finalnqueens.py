import numpy as np
size=int(input('enter size '))
board=np.zeros((size,size),dtype=int)
queens=[9 for x in range(size)]
arr=[]
def fillval(posx,posy,board):
	#fill horizontal and vertical
	for i in range(size):
		if board[posx][i]!=9:
			board[posx][i]=1	
		if board[i][posy]!=9:
			board[i][posy]=1
	#fill diagonals
	for i in range(size):
		for j in range(size):
			if board[i][j]!=9:
				if posx-posy==(i-j):
					board[i][j]=1
				if posx+posy==(i+j):
					board[i][j]=1
	return board
count=0
q=0
while queens!=[]:
	queens=[9 for x in range(size)]
	for p in range(size):
		for s in range(size):
			if queens==[]:
				break
			board[p][s]=queens.pop()
			board=fillval(p,s,board)
			for i in range(size):
				for j in range(size):
					if board[i][j]!=1 and board[i][j]!=9:
						board[i][j]=queens.pop()
						board=fillval(i,j,board)			
			for k in range(size):
				for m in range(size):
					if board[k][m]!=0:
						count+=1					
					if board[k][m]==9:
						q+=1
			if count==(size*size) and q!=size:
				count=0
				board=np.zeros((size,size),dtype=int)
				queens=[9 for x in range(size)]
				arr=[]
			count=0			
			q=0
print(board)