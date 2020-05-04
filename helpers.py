# Prints the board state in a nice format
def printState(board):
  for row in board:
    for tile in row:
      print(tile, end=" ")
    print()

# Locates and returns a pair of (row, col) indices where the blank space is found
def findEmptyIndices(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '0':
        return [i, j]

# Converts the 2D board state into a tuple
def tupifyState(board):
  return tuple(map(tuple, board))

# Message to print once the goal state is achieved
def printGoalMessage(num_nodes, max_num_frontier_nodes):
    print("Goal!!!\n")
    print("To solve this problem the search algorithm expanded a total of {} nodes.".format(num_nodes))
    print("The maximum number of nodes in the queue at any one time: {}.\n".format(max_num_frontier_nodes))