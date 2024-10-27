
# Maze Pathfinder

A Python project to determine the feasibility of paths within a maze. Given a grid-based maze with obstacles, the program checks if a path exists from a start to an end point. This project was developed under the guidance of Prof. Parag Singla at IIT Delhi.

## Project Overview

This project implements a pathfinding algorithm to navigate a maze. The maze is represented as a grid, where empty cells are accessible paths and blocked cells are obstacles. Using stack-based traversal methods, the algorithm checks whether a route from the start to the end point exists.

## Features

- **Efficient Path Verification:** Determines if a navigable route exists between two points in the maze.
- **Modular Design:** Each file has a dedicated role, making the project easily understandable and extensible.
- **Custom Exception Handling:** Manages edge cases and errors encountered during traversal.

## Files

- **exception.py**: Defines custom exceptions for handling edge cases and errors in maze traversal.
- **main.py**: The main entry point of the program. Loads the maze configuration and initiates the pathfinding process.
- **maze.py**: Defines the structure and functionality for creating and managing the maze.
- **navigator.py**: Contains the logic to traverse the maze, checking for possible paths.
- **stack.py**: Implements a stack data structure to aid in managing paths during traversal.

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed. This project has no external dependencies, so Python alone is sufficient to run the code.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MazePathfinder.git
   cd MazePathfinder
   ```

### Running the Program

To run the maze pathfinder, use:
   ```bash
   python main.py
   ```

**Input Format:**
1. Define the maze dimensions (rows and columns).
2. Specify the start and end coordinates in `(x, y)` format.
3. Input the maze layout as a grid of `0`s and `1`s:
   - `0` indicates an empty cell (path).
   - `1` indicates an obstacle.

Example:
```
5 5          # Maze dimensions (rows x columns)
0 0 4 4      # Start (0,0) and End (4,4)
0 0 0 1 0
1 1 0 1 0
0 0 0 0 0
1 1 1 1 0
0 0 0 0 0
```

### Expected Output

The program will output whether a path exists, with possible paths displayed in the console.

## Contributing

If you wish to contribute, feel free to fork this repository, make your changes, and submit a pull request.

## Credits

Developed by Gurnoor Singh, under the supervision of Prof. Parag Singla, IIT Delhi.

## License

This project is open-source and available under the MIT License.
