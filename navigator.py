from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
       
    def find_path(self, start : tuple, end : tuple) -> list:
        # IMPLEMENT FUNCTION HERE
        if self.navigator_maze[start[0]][start[1]] == 1:
            raise PathNotFoundException
        if self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException
        self.stack = Stack()
        self.visited = []
        
        for i in range(0, len(self.navigator_maze)):
            temp = []
            for j in range (0, len(self.navigator_maze[0])):
                temp.append(0)
            self.visited.append(temp)   #now our visited 2D array is completed
            
        self.stack.push([start])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
        while self.stack.size > 0:
            path = self.stack.top()  # Get the current path from the stack
            current_pos = path[-1]  # Current position is the last element in the path
            
            # Check if we've reached the end
            if current_pos == end:
                return path  # Path found
            
            self.stack.pop()  # Remove the current path from the stack to explore further
           
            
            x, y = current_pos
            self.visited[x][y] = 1
            
            # Explore neighbors
            for dx, dy in directions:
                next_pos = (x + dx, y + dy)
                
                # Check if the next position is within bounds and not a wall
                if (0 <= next_pos[0] < len(self.navigator_maze) and
                    0 <= next_pos[1] < len(self.navigator_maze[0]) and
                    self.navigator_maze[next_pos[0]][next_pos[1]] != 1 and
                    self.visited[next_pos[0]][next_pos[1]] != 1):
                    
                    # Create a new path with the next position and push it onto the stack
                    new_path = path + [next_pos]
                    self.stack.push(new_path)  # we are pushing the whole path onto the stack
        
        raise PathNotFoundException