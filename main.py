from heapq import *
from copy import deepcopy
from helpers import *

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
    self.frontier = []
    self.explored_set = set()
    self.nodes_expanded = 0
    self.max_num_frontier_nodes = 0

  # Choose which search algorithm to use
  def solve(self):
    self.uniformCostSearch()

  def uniformCostSearch(self):
    count = 0
    current_node = Node(self.initial_state)
    
    print("Expanding state")
    current_node.printState()
    print('\n')

    triple = (current_node.g_n, count, current_node)
    heappush(self.frontier, triple)

    tupled_state = tupifyBoard(current_node.state)
    self.explored_set.add(tupled_state)

    while len(self.frontier) > 0:
      self.max_num_frontier_nodes = max(self.max_num_frontier_nodes, len(self.frontier))

      top = heappop(self.frontier)
      current_node_g_n = top[0]
      current_node = top[2]

      # Stop and print results once we've found our goal state
      # if current_node.state == self.goal_state:
      #   print("Goal!!!")
      #   return

      tupled_state = tupifyBoard(current_node.state)
      self.explored_set.add(tupled_state)
      
      print("The best state to expand with g(n) = {} is...".format(current_node_g_n))
      current_node.printState()
      print("Expanding this node...\n")

      possible_states = current_node.getPossibleStates()
      for node in possible_states:
        count += 1
        tupled_state = tupifyBoard(node.state)

        if node.state == self.goal_state:
          print("Goal!!!")
          return

        if tupled_state not in self.explored_set:
          triple = (node.g_n, count, node)
          heappush(self.frontier, triple)
      
given_board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 0, 8]
]

goal_state = [
  [1,2,3],
  [4,5,6],
  [7,8,0]
]

problem = Problem(given_board, goal_state)
problem.solve()