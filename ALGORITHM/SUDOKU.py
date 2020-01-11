board= [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

def solve(board):
    pos=check_empty(board)
    if not pos:
        return True
    else:
        row,col=pos

    for i in range(1,10):
        if check_valid(row,col,i)==True:
            board[row][col]=i

            if solve(board):
                return True
            #reset if all failed then backtrack
            board[row][col]=0
    return False

def check_valid(row,col,num):
    #check complete same row
    for i in range(len(board)):
        if board[row][i]==num and i!=col:
            return False
    ##check the same column
    for j in range(len(board[0])):
        if board[j][col]==num and j!=row:
            return False
    #check the box
    rx=row//3
    cy=col//3
    for r in range(rx*3,(rx*3)+3):
        for c in range(cy*3,(cy*3)+3):
            if num==board[r][c] and (r,c)!=(row,col):
                return False
    return True

def check_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    return None

def printer(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('|',end=' ')
            print(board[i][j],end=' ')
        print()
        if (i+1)%3==0 and i!=0:
            print('______________________')



printer(board)
solve(board)
print('===================================================')
printer(board)
