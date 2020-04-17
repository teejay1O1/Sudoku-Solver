class Solution:
    # @param A : list of list of chars
    # @return nothing
    def block(self,row_,col_):
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
        
    def isValid(self,row,col,A,num):
        if num in A[row]:
            return False
        elif num in [A[i][col] for i in range(9)]:
            return False
        else:
            for i,j in self.block(row,col):
                if A[i][j]==num:
                    return False
        return True
        
    def sudoku(self,A,row,col):
        if row==8 and col==8:
            self.ans=["".join(row) for row in A]
            return 0 
        
        if col<8:
            if A[row][col]!=".":
                self.sudoku(A,row,col+1)
            else:
                for num in self.choices:
                    if self.ans==None and self.isValid(row,col,A,num) :
                        A[row][col]=num
                        self.sudoku(A,row,col+1)
        elif row<=8:
            if A[row][col]!=".":
                self.sudoku(A,row+1,0)
            else:    
                for num in self.choices:
                    if self.ans==None and self.isValid(row,col,A,num) :
                        A[row][col]=num
                        self.sudoku(A,row+1,0)
                   
            
    def solveSudoku(self, A):
        self.ans=None
        self.choices=[str(i) for i in range(1,10)]
        A=[[i for i in row] for row in A]
        self.sudoku(A,0,0)
        A=self.ans