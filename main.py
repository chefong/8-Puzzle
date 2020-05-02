from queue import PriorityQueue
from copy import deepcopy

class Node:
  def __init__(self, board, g_n=0):
    self.state = board
    self.g_n = g_n

  def findEmptyIndex(self):
    for i in range(len(self.state)):
      for j in range(len(self.state[i])):
        if self.state[i][j] == 0:
          return [i, j]
  
  # Returns an array of next possible states (Nodes) with the current state
  def getPossibleStates(self):
    possible_states = []
    next_g_n = self.g_n + 1
    empty_row_index, empty_col_index = self.findEmptyIndex()

    num_rows = len(self.state)
    num_cols = len(self.state[0])

    # Can we move up?
    if empty_row_index > 0:
      next_state = deepcopy(self.state)
      up_row_index = empty_row_index - 1
      next_state[empty_row_index][empty_col_index], next_state[up_row_index][empty_col_index] = next_state[up_row_index][empty_col_index], next_state[empty_row_index][empty_col_index]
      
      node = Node(next_state, next_g_n)
      possible_states.append(node)

    # Can we move down?
    if empty_row_index < num_rows - 1:
      next_state = deepcopy(self.state)
      down_row_index = empty_row_index + 1
      next_state[empty_row_index][empty_col_index], next_state[down_row_index][empty_col_index] = next_state[down_row_index][empty_col_index], next_state[empty_row_index][empty_col_index]

      node = Node(next_state, next_g_n)
      possible_states.append(node)

    # Can we move left?
    if empty_col_index > 0:
      next_state = deepcopy(self.state)
      left_col_index = empty_col_index - 1
      next_state[empty_row_index][empty_col_index], next_state[empty_row_index][left_col_index] = next_state[empty_row_index][left_col_index], next_state[empty_row_index][empty_col_index]

      node = Node(next_state, next_g_n)
      possible_states.append(node)

    # Can we move right?
    if empty_col_index < num_cols - 1:
      next_state = deepcopy(self.state)
      right_col_index = empty_col_index + 1
      next_state[empty_row_index][empty_col_index], next_state[empty_row_index][right_col_index] = next_state[empty_row_index][right_col_index], next_state[empty_row_index][empty_col_index]

      node = Node(next_state, next_g_n)
      possible_states.append(node)

    return possible_states

  def printState(self):
    for row in self.state:
      print(row)

class Problem:
  def __init__(self, initial_state, goal_state):
    self.initial_state = initial_state
    self.goal_state = goal_state
    self.frontier = PriorityQueue()
    self.nodes_expanded = 0
    self.max_num_frontier_nodes = 0

  # Choose which search algorithm to use
  def solve(self):
    self.uniformCostSearch()

  def uniformCostSearch(self):
    node = Node(self.initial_state)
    
    print("Expanding state")
    node.printState()
    print()

    self.frontier.put((node.g_n, node))

    while not self.frontier.empty():
      node_g_n, node = self.frontier.get()
      
      # Stop and print results once we've found our goal state
      if node.state == self.goal_state:
        print("Goal!!!")
        return
      
      print("The best state to expand with g(n) = {} is...".format(node.g_n))
      node.printState()
      print("Expanding this node...\n")

      possible_states = node.getPossibleStates()
      
given_board = [
  [4,0,2],
  [8,1,3],
  [5,7,6]
]

goal_state = [
  [1,2,3],
  [4,5,6],
  [7,8,0]
]

problem = Problem(given_board, goal_state)
problem.solve()