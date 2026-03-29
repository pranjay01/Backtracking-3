#Word Search

# Time comlexity -> O(MxNx4^L) as for each index position in matrix we are checking the word by recrusion
# Space Complexity -> O(L) recusrive stack and set
# Logic -> iterate over each matrix, once you find 1st character, then see if word can be formed using DFS and using
# Backtrack for managing the visited items

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(0,-1), (-1,0), (0,1), (1,0)]
        visitedIndexes = set()
        m = len(board)
        n = len(board[0])
        wordLength = len(word)

        def helper(wordIndex, row, column):
            if wordIndex == wordLength:
                return True
            charToCheck = word[wordIndex]
            for r, c in dir: 
                if r+row>=0 and r+row<m and c+column >= 0 and c+column < n and (r+row,c+column) not in visitedIndexes and charToCheck == board[r+row][c+column]:
                    visitedIndexes.add((r+row,c+column))
                    if helper(wordIndex+1, r+row,c+column):
                        return True
                    visitedIndexes.remove((r+row,c+column))

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visitedIndexes.add((i,j))
                    if helper(1, i, j):
                        return True
                    visitedIndexes.remove((i,j))
        return False