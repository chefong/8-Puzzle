from helpers import *
from heapq import *
from math import sqrt, pow
from queue import PriorityQueue
from copy import deepcopy

class Node:
  def __init__(self, board, g_n=0):
    self.state = board
    self.g_n = g_n
    self.heuristic = self.euclideanDistance

  # Counts and returns the number of misplaced tiles using the current state compared to the goal state
  def countMisplacedTiles(self, goal_state):
    num_misplaced_tiles = 0

    for i in range(len(self.state)):
      for j in range(len(self.state[i])):
        current_state_tile = self.state[i][j]
        goal_state_tile = goal_state[i][j]

        if current_state_tile != goal_state_tile:
          num_misplaced_tiles += 1

    return num_misplaced_tiles
  
  # Calculates and returns the sum of Euclidean distances between each current state tile and goal state tile
  def euclideanDistance(self, goal_state):
    total_distance = 0

    # Create a mapping between tile number and indices n -> (x, y)
    current_state_mappings = {}
    goal_state_mappings = {}

    for i in range(len(self.state)):
      for j in range(len(self.state[i])):
        current_state_tile = self.state[i][j]
        goal_state_tile = goal_state[i][j]

        indices = (i, j)
        current_state_mappings[current_state_tile] = indices
        goal_state_mappings[goal_state_tile] = indices
    
    for tile, indices in current_state_mappings.items():
      goal_state_indices = goal_state_mappings[tile]

      x1, y1 = indices
      x2, y2 = goal_state_indices
      distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

      total_distance += distance
    
    return total_distance
        
  # Returns a list of next possible Nodes depending on the current state
  def getPossibleStates(self):
    possible_states = []
    next_g_n = self.g_n + 1
    empty_row_index, empty_col_index = findEmptyIndices(self.state)

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
    self.explored_set = set()
    self.nodes_expanded = 0
    self.max_num_frontier_nodes = 0

  # Choose which search algorithm to use
  def solve(self):
    # self.uniformCostSearch()
    self.aStarSearch()

  def uniformCostSearch(self):
    current_node = Node(self.initial_state)
    num_nodes = 1
    
    print("Expanding state")
    current_node.printState()
    print()

    if current_node.state == self.goal_state:
      printGoalMessage(num_nodes, self.max_num_frontier_nodes)
      return

    # 'num_nodes' is also used as the alternate comparator for Python's PriorityQueue class
    element = (current_node.g_n, num_nodes, current_node)
    self.frontier.put(element)

    tupled_state = tupifyState(current_node.state)
    self.explored_set.add(tupled_state)

    while not self.frontier.empty():
      # Check and update if we've had the largest number of nodes in the frontier
      self.max_num_frontier_nodes = max(self.max_num_frontier_nodes, self.frontier.qsize())

      top = self.frontier.get()
      current_node = top[2]

      # Convert our board state to a tuple in order to add it to the explored set
      # (2D lists are not hashable)
      tupled_state = tupifyState(current_node.state)
      self.explored_set.add(tupled_state)
      
      print("The best state to expand with g(n) = {} is...".format(current_node.g_n))
      current_node.printState()
      print("Expanding this node...\n")

      possible_states = current_node.getPossibleStates()
      for node in possible_states:
        num_nodes += 1
        tupled_state = tupifyState(node.state)

        # If one of our possible next states is our goal state, we can stop!
        if node.state == self.goal_state:
          printGoalMessage(num_nodes, self.max_num_frontier_nodes)
          return

        # Add to the frontier if we haven't seen this state yet
        if tupled_state not in self.explored_set:
          element = (node.g_n, num_nodes, node)
          self.frontier.put(element)

  # f(n) = g(n) + h(n)
  def aStarSearch(self):
    current_node = Node(self.initial_state)
    num_nodes = 1
    
    print("Expanding state")
    current_node.printState()
    print()

    if current_node.state == self.goal_state:
      printGoalMessage(num_nodes, self.max_num_frontier_nodes)
      return
    
    # Calculate our f(n) = g(n) + h(n)
    h_n = current_node.heuristic(self.goal_state)
    f_n = current_node.g_n + h_n

    element = (f_n, num_nodes, current_node)
    self.frontier.put(element)

    tupled_state = tupifyState(current_node.state)
    self.explored_set.add(tupled_state)

    while not self.frontier.empty():
      # Check and update if we've had the largest number of nodes in the frontier
      self.max_num_frontier_nodes = max(self.max_num_frontier_nodes, self.frontier.qsize())

      top = self.frontier.get()
      current_h_n = top[0]
      current_node = top[2]

      tupled_state = tupifyState(current_node.state)
      self.explored_set.add(tupled_state)

      print("The best state to expand with g(n) = {} and h(n) = {} is...".format(current_node.g_n, current_h_n))
      current_node.printState()
      print("Expanding this node...\n")

      possible_states = current_node.getPossibleStates()
      for node in possible_states:
        num_nodes += 1

        # If one of our possible next states is our goal state, we can stop!
        if node.state == self.goal_state:
          printGoalMessage(num_nodes, self.max_num_frontier_nodes)
          return

        # Convert node's state to tuple to check if it was previously explored
        tupled_state = tupifyState(node.state)

        # Add to the frontier if we haven't seen this state yet
        if tupled_state not in self.explored_set:
          h_n = node.heuristic(self.goal_state)
          f_n = node.g_n + h_n

          element = (f_n, num_nodes, node)
          self.frontier.put(element)
      
given_board = [
  [1, 2, 3],
  [4, 8, 0],
  [7, 6, 5]
]

goal_state = [
  [1,2,3],
  [4,5,6],
  [7,8,0]
]

problem = Problem(given_board, goal_state)
problem.solve()