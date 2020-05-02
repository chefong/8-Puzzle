from defaultPuzzles import *
from helpers import printState
from classes import Problem

# Prompt user to select puzzle difficulty and return the corresponding puzzle
def defaultPuzzle():
  print("Choose one of the default puzzles below.")

  print("(1) Solved")
  printState(solved_puzzle)
  print()

  print("(2) Easy")
  printState(easy_puzzle)
  print()

  print("(3) Medium")
  printState(medium_puzzle)
  print()

  print("(4) Hard")
  printState(hard_puzzle)
  print()

  initial_state_selection = input("Enter your selection: ")
  if initial_state_selection == '1':
    return solved_puzzle
  elif initial_state_selection == '2':
    return easy_puzzle
  elif initial_state_selection == '3':
    return medium_puzzle
  elif initial_state_selection == '4':
    return hard_puzzle

# Prompt user to enter values for each puzzle row
def customPuzzle():
  print("Enter your puzzle, use a zero to represent the blank space.")

  first_row = input("Enter the first row, use space or tabs between numbers: ")
  second_row = input("Enter the second row, use space or tabs between numbers: ")
  third_row = input("Enter the third row, use space or tabs between numbers: ")

  first_row_tiles = first_row.split()
  second_row_tiles = second_row.split()
  third_row_tiles = third_row.split()

  return [first_row_tiles, second_row_tiles, third_row_tiles]

# Prompt user to select which search algorithm to perform
def chooseSearchAlgorithm():
  search_algorithm_message = "Enter your choice of algorithm.\n"
  uniform_cost_message = "(1) Uniform Cost Search\n"
  a_star_misplaced_tile_message = "(2) A* with the Misplaced Tile heuristic\n"
  a_star_euclidean_message = "(3) A* with the Euclidean distance heuristic\n"

  search_algorithm_selection = input(search_algorithm_message + uniform_cost_message + a_star_misplaced_tile_message + a_star_euclidean_message)

  return search_algorithm_selection

if __name__ == '__main__':
  initial_state = []

  student_id = "861267345"
  welcome_message = "Welcome to {} 8 puzzle solver.\n".format(student_id)
  choose_puzzle_message = "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n"

  puzzle_selection = input(welcome_message + choose_puzzle_message)
  if puzzle_selection == '1':
    initial_state = defaultPuzzle()
  elif puzzle_selection == '2':
    initial_state = customPuzzle()
  
  # Create an instance of Problem using the user selected initial state
  problem = Problem(initial_state)
  
  # Prompt which search algorithm to perfom
  search_algorithm_selection = chooseSearchAlgorithm()

  # Solve the puzzle!
  problem.solve(search_algorithm_selection)