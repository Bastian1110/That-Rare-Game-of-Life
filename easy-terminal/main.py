import os
from time import sleep

class TermGameOfLife:
    def __init__(self, dim: int, initial_state: list[tuple[int, int]]):
        self.grid = [[0] * dim for _ in range(dim)]
        self.dim = dim
        for cell in initial_state:
            self.grid[cell[1]][cell[0]] = 1

    def step(self):
        new_grid = [[0] * self.dim for _ in range(self.dim)]
        for y in range(self.dim):
            for x in range(self.dim):
                neighbors = self._get_neighbors(x, y)
                if self.grid[y][x] == 1 and (neighbors == 2 or neighbors == 3):
                    new_grid[y][x] = 1
                elif self.grid[y][x] == 0 and neighbors == 3:
                    new_grid[y][x] = 1
        self.grid = new_grid

    def _get_neighbors(self, x, y):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        neighbors = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.dim and 0 <= ny < self.dim:
                neighbors += self.grid[ny][nx]
        return neighbors

    def run(self, steps=100, delay=0.2):
        for _ in range(steps):
            os.system('cls' if os.name == 'nt' else 'clear')  
            self.print()
            self.step()
            sleep(delay)

    def print(self):
        grid_string = ""
        for row in self.grid:
            grid_string += "".join(["■ " if cell else "  " for cell in row]) + "\n"
        print(grid_string, flush=True)

if __name__ == "__main__":
    config = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    gof = TermGameOfLife(30, config)
    gof.run()
