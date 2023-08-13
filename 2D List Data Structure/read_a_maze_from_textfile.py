"""
Reading a maze from a text file
"""

def read_maze(file_name):
    """
    Read a maze stored in a text file and return ta 2d list containing the maze representation.
    """
    try:
        with open(file_name) as file_h:
            maze = [[char for char in line.strip("\n")] for line in file_h]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is rectangular.")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with file you have selected.")
        raise SystemExit

if __name__ == "__main__":
    maze = read_maze("/workspaces/Data-Structure-and-Algorithm/2D List Data Structure/modest_maze.txt")
    for row in maze:
        print(row)
