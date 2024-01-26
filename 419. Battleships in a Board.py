class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        column = len(board[0])
        battle_ships = 0

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= column or board[r][c] != 'X':
                return

            board[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(column):
                if board[r][c] == 'X':
                    dfs(r, c)
                    battle_ships += 1

        return battle_ships