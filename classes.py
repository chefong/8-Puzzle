from helpers import *
from heuristics import *
from queue import PriorityQueue
from copy import deepcopy

class Node:
  def __init__(self, board, g_n=0):
    self.state = board
    self.g_n = g_n
        
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
      for tile in row:
        print(tile, end=" ")
      print()

class Problem:
  def __init__(self, initial_state):
    self.initial_state = initial_state
    self.frontier = PriorityQueue()
    self.explored_set = set()
    self.nodes_expanded = 0
    self.max_num_frontier_nodes = 0
    self.goal_state = [
      ['1','2','3'],
      ['4','5','6'],
      ['7','8','0']
    ]

  # Choose which search algorithm to use
  def solve(self, search_type):
    if search_type == "uniform cost":
      print("Searching with uniform cost...\n")
      self.uniformCostSearch()
    elif search_type == "a* misplaced tile":
      print("Searching with A* misplaced tile...\n")
      self.aStarSearch(countMisplacedTiles)
    elif search_type == "a* euclidean distance":
      print("Searching with A* Euclidean distance...\n")
      self.aStarSearch(euclideanDistance)

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
  def aStarSearch(self, heuristic):
    current_node = Node(self.initial_state)
    num_nodes = 1
    
    print("Expanding state")
    current_node.printState()
    print()

    if current_node.state == self.goal_state:
      printGoalMessage(num_nodes, self.max_num_frontier_nodes)
      return
    
    # Calculate our f(n) = g(n) + h(n)
    h_n = heuristic(current_node.state, self.goal_state)
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
          h_n = heuristic(node.state, self.goal_state)
          f_n = node.g_n + h_n

          element = (f_n, num_nodes, node)
          self.frontier.put(element)