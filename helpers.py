def findEmptyIndices(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        return [i, j]

def tupifyState(board):
  return tuple(map(tuple, board))

def printGoalMessage(num_nodes, max_num_frontier_nodes):
    print("Goal!!!\n")
    print("To solve this problem the search algorithm expanded a total of {} nodes.".format(num_nodes))
    print("The maximum number of nodes in the queue at any one time: {}.".format(max_num_frontier_nodes))