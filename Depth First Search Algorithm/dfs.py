"""
Helper functions and values for use with other files in this project

"""

offset = {
    "right": (0,1),
    "left": (0,-1),
    "up": (-1,0),
    "down": (1,0)
}

class Stack:
    """
    Stack
    """
    def __init__(self):
        """
        Initialize function
        """
        self.items = []

    def is_empty(self):
        """
        to check whether stack is empty
        """
        #return len(self.items) == 0
        return not self.items

    def push(self, item):
        """
        To push the data in the stack
        """
        self.items.append(item)

    def pop(self):
        """
        To remove and return the data from the stack
        """
        return self.items.pop()

    def peek(self):
        """
        To check the top data and return from the stack
        """
        return self.items[-1]

    def size(self):
        """
        to check the size of the stack
        """
        return len(self.items)

    def __str__(self):
        """
        Ito change the string retun of the stack
        """
        return str(self.items)

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

def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze)
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"

def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up","right","down","left"]:
            row_offset, col_offset = offset[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour]=current_cell
    return None

if __name__ == "__main__":
    # Test 1
    # maze = [[0]*3 for row in range(3)]
    # start_pos = (0,0)
    # goal_pos = (2,2)
    # result = dfs(maze, start_pos, goal_pos)
    # assert result == [(0,0),(1,0),(2,0),(2,1),(2,2)]

    # Test 2
    maze = read_maze("/workspaces/Data-Structure-and-Algorithm/2D List Data Structure/modest_maze.txt")
    start_pos = (0,0)
    goal_pos = (3,3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
    print(result)