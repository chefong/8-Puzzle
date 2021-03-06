from math import sqrt, pow

# Counts and returns the number of misplaced tiles using the current state compared to the goal state
def countMisplacedTiles(current_state, goal_state):
  num_misplaced_tiles = 0

  for i in range(len(current_state)):
    for j in range(len(current_state[i])):
      current_state_tile = current_state[i][j]
      goal_state_tile = goal_state[i][j]

      if current_state_tile != goal_state_tile:
        num_misplaced_tiles += 1
    
  # Subtract 1 to ignore the blank space being counted
  return num_misplaced_tiles - 1

# Calculates and returns the sum of Euclidean distances between each current state tile and goal state tile
def euclideanDistance(current_state, goal_state):
  total_distance = 0

  # Create a mapping between tile number and indices n -> (x, y)
  current_state_mappings = {}
  goal_state_mappings = {}

  # Iterate through entire board and store a map between the tile number and indices
  for i in range(len(current_state)):
    for j in range(len(current_state[i])):
      current_state_tile = current_state[i][j]
      goal_state_tile = goal_state[i][j]

      indices = (i, j)
      current_state_mappings[current_state_tile] = indices
      goal_state_mappings[goal_state_tile] = indices
  
  # Calculate Euclidean distances for non-empty spaces
  del current_state_mappings['0']
  
  # Iterate through mappings and calculate the Euclidean distance between the current state index pair and goal state index pair
  for tile, indices in current_state_mappings.items():
    goal_state_indices = goal_state_mappings[tile]

    x1, y1 = indices
    x2, y2 = goal_state_indices
    distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    total_distance += distance
  
  return total_distance