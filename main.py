from classes import Problem

if __name__ == '__main__':
  initial_state = []

  student_id = "861267345"
  welcome_message = "Welcome to {} 8 puzzle solver.\n".format(student_id)
  choose_puzzle_message = "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.\n"

  puzzle_selection = input(welcome_message + choose_puzzle_message)
  if puzzle_selection == '1':
    pass
  elif puzzle_selection == '2':
    print("Enter your puzzle, use a zero to represent the blank space.")

    first_row = input("Enter the first row, use space or tabs between numbers: ")
    second_row = input("Enter the second row, use space or tabs between numbers: ")
    third_row = input("Enter the third row, use space or tabs between numbers: ")

    first_row_tiles = first_row.split()
    second_row_tiles = second_row.split()
    third_row_tiles = third_row.split()

    initial_state = [first_row_tiles, second_row_tiles, third_row_tiles]
  
  # Create an instance of Problem using the user selected initial state
  problem = Problem(initial_state)
  
  search_algorithm_message = "Enter your choice of algorithm.\n"
  uniform_cost_message = "(1) Uniform Cost Search\n"
  a_star_misplaced_tile_message = "(2) A* with the Misplaced Tile heuristic\n"
  a_star_euclidean_message = "(3) A* with the Euclidean distance heuristic\n"

  search_algorithm_selection = input(search_algorithm_message + uniform_cost_message + a_star_misplaced_tile_message + a_star_euclidean_message)
  if search_algorithm_selection == '1':
    problem.solve("uniform cost")
  elif search_algorithm_selection == '2':
    problem.solve("a* misplaced tile")
  elif search_algorithm_selection == '3':
    problem.solve("a* euclidean distance")