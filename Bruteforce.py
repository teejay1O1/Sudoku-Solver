#sudoku=[[5,3,0,0,7,0,0,0,0,], [6,0,0,1,9,5,0,0,0,], [0,9,8,0,0,0,0,6,0,], [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6], [0,6,0,0,0,0,2,8,0,], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9]]
def block(row_,col_):
    vnum=row_//3
    hnum=col_//3
    choices=[]
    for i in [0,1,2]:
        for j in [0,1,2]:
            row=(vnum*3)+i
            col=(hnum*3)+j
            if row!=row_ or col!=col_ :
                choices.append((row,col))
    return choices


def isValid(x,y,n):
    global sudoku
    for i in range(9):
        if sudoku[i][y]== n or sudoku[x][i]==n :
            return False
    for i,j in block(x,y):
        if sudoku[i][j]==n :
            return False
    return True
    
def display():
    global sudoku
    for row in sudoku:
        print(row)

def solver():
    global sudoku
    for  i in range(9):
        for j in range(9):
            if sudoku[i][j]== 0 :
                for n in range(1,10):
                    if isValid(i,j,n):
                        sudoku[i][j]=n
                        solver()
                        sudoku[i][j]=0
                return None
    display()

#solver()