#N-Queens

# Time complexity -> N! since for each new row it is 1 less space to place atleast
# Space Complexity -> O(N) coming from the set and queens column position per row
# Logic -> for each row place the queen a each column, then recurse to next row and based on earlier placements validate
# and do the queen placement in current row and continue untill you found all the possible placements 


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queenDiagonalTracker = set()
        queenAntDiagonalTracker = set()
        queenColumnTracker = set()

        columnPositionPerRow = [0]*n

        def helper(row):
            if row == n:
                convertAndAddToResult()
                return
            for j in range(n):
                if noCoflict(row, j):
                    columnPositionPerRow[row] = j
                    queenDiagonalTracker.add(row-j)
                    queenAntDiagonalTracker.add(row+j)
                    queenColumnTracker.add(j)
                    helper(row+1)
                    queenDiagonalTracker.remove(row-j)
                    queenAntDiagonalTracker.remove(row+j)
                    queenColumnTracker.remove(j)
                    columnPositionPerRow[row] = 0

        def noCoflict(row, j):
            # check top
            if j in queenColumnTracker: return False

            #check diagonal
            if (row-j) in queenDiagonalTracker: return False

            #check antiDiagonal
            if (row+j) in queenAntDiagonalTracker: return False

            return True
        
        def convertAndAddToResult():
            tmp = []
            for i in range(n):
                column = columnPositionPerRow[i]
                tmp.append("."*(column) + "Q" + "."*(n-column-1))
                # tmp.append("".join(tmpResult[i]))

            result.append(tmp)

        helper(0)
        return result