def soln(board, N):
    finalProd = []
    for i in range(N):
        rowList = []
        for j in range(N):
            rowList.append(board[i][j])
        finalProd.append(rowList)
    return finalProd

def isSafe(board, row, col, N):
	# Since we are starting from column 0,
	# we only need to check for values which will trouble us from the left.
	for i in range(col):
		if board[row][i] == 1:
			return False

	# -1 of third argumrnt indicates that its reducing the 
	# values of rows andd columns, 
	# thus checking values to the left of the cursor
	# here, i and j are both reduced to check the upper left diagonal.
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Here, i is increased and j is decreased 
	# to check the lower left diagonal. 
	# Since we go down, and the row number is increased.
	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True

def solveNQUtil(board, col, N):
	# If we reach the end of 
	# matrix, return true,thus saying this is solvalable,
	# and the solution is ready. 
	if col >= N:
		return True

	# Consider this column and try placing
	# this queen in all rows one by one
	# Rows are increased one by one to place 
	# queens only in a selected row at a time.
	for i in range(N):

		if isSafe(board, i, col, N):
			# Place this queen in board[i][col]
			board[i][col] = 1

			# The number of columns is incremented here
			# and this function is caleed again with the 
			# incremented number of colummns
			if solveNQUtil(board, col + 1, N) == True:
				return True

			# If placing queen in board[i][col]
			# doesn't lead to a solution, then remove 
			# queen from board[i][col]
			# Backtracking
			board[i][col] = 0

	# if the queen can not be placed in any row in
	# this column col then return false
	# thus, solution is not available for this number of rows and columns
	return False

def makeBoard(n):
    lst=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        lst.append(l)
    return lst

def solveNQ(N):
    board=makeBoard(N)
    if solveNQUtil(board, 0, N) == False:
        return False
    nqueenList=soln(board, N)
    return nqueenList

