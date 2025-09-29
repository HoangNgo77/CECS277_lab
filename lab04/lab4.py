"""
Author: Phan Ngo - Lucas Seitz
Date: 2025-09-16
Description: CECS 277, Lab 4
Maze Solver: Reads a maze from a text file into a 2D list, finds the start ('s'),
and lets the user move (1/2/3/4) until reaching the finish ('f').
No globals. Only required functions are implemented: read_maze, find_start, display_maze.
"""
import check_input

def read_maze():
    filename = "maze.txt"
    try:
        # r - read - defauit value. Open file for reading error if the file does not exist
        # with ... as file: the file close automatically, even if an error occours
        with open(filename, 'r') as file:
            maze = []                           # start with an empty list maze
            for line in file:
                #list(): convert the string into a list of single characters.
                # rstrip(default)-remove witespace character(spaces, tab, newline) from the end of string but keep space inside the line
                row = list(line.rstrip('\n'))   
                maze.append(row)
        return maze
    # Throw message if file does not exits
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    # Thorw message if any unexpected proplem - permission errors
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def find_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 's':
                return [row, col]
    return None  # Return None if start position not found


def display_maze(maze, loc):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if [row, col] == loc:
                print('X', end='')
            else:
                print(maze[row][col], end='')
        print()  # New line after each row


def main():
    print("-MAZE Solver-")

    # Read the maze from file
    maze = read_maze()
    if maze is None:
        print("Failed to load maze. Exiting...")
        return
    
    # Find the starting position
    start_location = find_start(maze)
    if start_location is None:
        print("Error: No starting position ('s') found in the maze.")
        return
    
    # Initialize user location to start position
    user_location = start_location.copy()
    
    # Display initial maze
    display_maze(maze, user_location)
    
    # Main game loop
    while True:
        print("\nOptions:")
        print("1. Go North (Up)")
        print("2. Go South (Down)") 
        print("3. Go East (Right)")
        print("4. Go West (Left)")
        
        move = check_input.get_int_range("Enter your choice: ", 1, 4)
        
        # if move == 'q':
        #     print("Thanks for playing!")
        #     break
        
        # Calculate new position based on move
        new_row = user_location[0]
        new_col = user_location[1]
        
        if move == 1:  # Move up
            new_row -= 1
        elif move == 2:  # Move down
            new_row += 1
        elif move == 3:  # Move left
            new_col += 1
        elif move == 4:  # Move right
            new_col -= 1
        else:
            print("Invalid move. Please use 1,2,3,4.")
            continue
        
        #- just in case if the maze don't have boder in  * + Check if new position is within maze bounds
        if (new_row < 0 or new_row >= len(maze) or 
            new_col < 0 or new_col >= len(maze[new_row])):
            print("You cannot move outside the maze!")
            continue
        
        # Check if new position is a wall
        if maze[new_row][new_col] == '*':
            print("You cannot move there!")
            display_maze(maze, user_location)
            continue
        
        # Update user location
        user_location[0] = new_row
        user_location[1] = new_col
        
        # Check if user reached the finish
        if maze[new_row][new_col] == 'f':
            display_maze(maze, user_location)
            print("\nCONGRATULATIONS! You have solved the maze.")
            break
        
        # Display the updated maze
        display_maze(maze, user_location)


if __name__ == "__main__":
    main()