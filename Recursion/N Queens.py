def solveNQueens(n):
        board = [['.'*n] for _ in range(n)]
        cols, diags, antiDiags, result = set(), set(), set(), []
          
        def solve(board, row):
            if row >= n:
                result.append(board[:])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diags or (row + col) in antiDiags:
                    continue
                    
                cols.add(col)
                diags.add(row - col)
                antiDiags.add(row + col)
                board[row] = '.'*col + 'Q' + '.'*(n-col-1)

                solve(board, row + 1)

                cols.remove(col)
                diags.remove(row - col)
                antiDiags.remove(row + col)
                board[row] = '.'*n

        solve(board, 0)
        return result

print(solveNQueens(4))