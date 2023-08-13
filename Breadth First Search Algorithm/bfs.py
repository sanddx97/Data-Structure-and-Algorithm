"""
BFS
"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        """
        """
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
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

def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up","right","down","left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0]+row_offset, current_cell[1]+col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour]=current_cell
    return None



