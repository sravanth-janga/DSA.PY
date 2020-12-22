import sys  
sys.path .append('..')


# dp classes 
class MatrixChain:
    ''' 
    This is the implementation of matrixchain multiplication problem.
    There  if an option to customize the recurrence relation of the problem.
    You can pass any valid function defination which takes arr,M,i,j,k as it's arguments.
        arr : an array of integers
        M : n*n matrix
        i,j,k : integers.

    Note :
            results are dependant on the recurrence relation, be cautious when defining the recurrence relation !

    '''
    def recurrence(self,arr,M,i,j,k):
        return M[i][k]+M[k+1][j]+(arr[i]*arr[j]*arr[k])  
    
    def solve(self,arr,n,f=None):
        self.arr = arr 
        self.M = [[0 for _ in range(n)] for __ in range(n)]
        if f:
            self.rec = f 
        else:
            self.rec = self.recurrence 
        
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = l+i-1
                self.M[i][j] = float('inf')
                for k in range(i,j):
                    self.M[i][j] = min(self.M[i][j],self.rec(self.arr,self.M,i,j,k))
        return self.M[0][n-1]


'''   
# driver code
# You can find the problem here : https://leetcode.com/problems/minimum-cost-tree-from-leaf-values
# This is a variant of the matrix-chain multipication problem.
# I've defined a custom recurrence relation function according to the setting of the problem.
def recur(arr,M,i,j,k):
    return M[i][k]+M[k+1][j]+max(arr[i:k+1])*max(arr[k+1:j+1])
arr = [6,2,4,10,2,15,10,10]
n = len(arr)
s = MatrixChain()
print(s.solve(arr, n, recur)) '''
