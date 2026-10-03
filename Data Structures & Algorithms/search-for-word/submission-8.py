class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    # use index pointer
        def help(i, j, ind, s):

            # use index to track your position in the word.
            # this is so you don't have to pass in substrings to every call.
            if (i,j) in s:
                return False

            if not board[i][j] == word[ind]:
                return False

            if ind == len(word) - 1:
                return True
            s.add((i,j))

            if i-1 >= 0 and help(i-1,j,ind+1,s):
                return True
            if i+1 < len(board) and help(i+1,j,ind+1,s):
                return True
            if j-1 >= 0 and help(i,j-1,ind+1,s):
                return True
            if j+1 < len(board[0]) and help(i,j+1,ind+1,s):
                return True

            # very important: undo the choice, so other potential strings can use it. 
            # remove it from the set after testing all four neighbor directions and CONFIRMING that none of them complete the word.
            # remove it from the set so another part of the board is allowed to use it later.  
            s.remove((i,j))   
         
        for i in range(len(board)):
            for j in range(len(board[0])):
                s = set()
                if (help(i,j,0,s)):
                    return True

        return False