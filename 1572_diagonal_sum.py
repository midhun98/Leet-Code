class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        row = 0
        row2 = -1
        total = 0
        for  i in mat:
            total += i[row] + i[row2]
            row += 1
            row2 -= 1
            
#        find the midpoint in the case of odd square matrix
   
        if len(mat)%2 ==1:
            mid = len(mat)//2
            value = mat[mid][mid]
            return total-value
        
        return total



#We are calculating the sum of the diagonal elements just by using a single for loop.

#In case of a square matrix with even number of columns this for loop would work fine. 

#But in the case of odd square matrix we need to remove the mid point. So we find the mid value of the matrix using the if condition 
#and subtract it from our total
