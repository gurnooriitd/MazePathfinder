import random

n, m = 100, 100
grid = [[random.choice([0, 1]) for _ in range(m)] for _ in range(n)]

# Ensure start and end points are passable
grid[0][0] = 0
grid[99][99] = 0

# Optionally print or save the grid to a file
with open('100x100_grid.txt', 'w') as f:
    f.write(f'{n} {m}\n')
    f.write('0 0\n99 99\n')
    for row in grid:
        f.write(' '.join(map(str, row)) + '\n')
