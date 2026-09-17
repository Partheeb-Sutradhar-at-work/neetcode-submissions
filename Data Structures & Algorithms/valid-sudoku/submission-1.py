class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashmap = set()
            for x in row:
                if x in hashmap and x != ".":
                    return False
                hashmap.add(x)
        
            
        for col in range(9):
            hashmap = set()
            for row in range(9):
                if board[row][col] in hashmap and board[row][col] != ".":
                    return False
                hashmap.add(board[row][col])

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                hashmap = set()
                for i in range(3):
                    for j in range(3):
                        if board[box_row+i][box_col+j] in hashmap and board[box_row+i][box_col+j] != ".":
                            return False
                        hashmap.add(board[box_row+i][box_col+j])





            
    

        return True

            


        