class CrosswordCSP:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.words = []

    def add_word(self, word, row, col, direction):
        self.words.append((word, row, col, direction))

    def is_valid_placement(self, word, row, col, direction):
        # Check if word fits within the grid boundaries
        if direction == 'across':
            if col + len(word) > self.grid_size:
                return False
        elif direction == 'down':
            if row + len(word) > self.grid_size:
                return False

        # Check if word intersects with existing words
        for i, letter in enumerate(word):
            if direction == 'across':
                if self.grid[row][col + i] != ' ' and self.grid[row][col + i] != letter:
                    return False
            elif direction == 'down':
                if self.grid[row + i][col] != ' ' and self.grid[row + i][col] != letter:
                    return False
        return True

    def place_word(self, word, row, col, direction):
        for i, letter in enumerate(word):
            if direction == 'across':
                self.grid[row][col + i] = letter
            elif direction == 'down':
                self.grid[row + i][col] = letter

    def solve(self):
        self.backtrack(0)

    def backtrack(self, index):
        if index == len(self.words):
            return True

        word, row, col, direction = self.words[index]
        if direction == 'across':
            for c in range(self.grid_size - len(word) + 1):
                if self.is_valid_placement(word, row, c, direction):
                    self.place_word(word, row, c, direction)
                    if self.backtrack(index + 1):
                        return True
                    self.place_word(word, row, c, direction)  # Backtrack
            return False
        elif direction == 'down':
            for r in range(self.grid_size - len(word) + 1):
                if self.is_valid_placement(word, r, col, direction):
                    self.place_word(word, r, col, direction)
                    if self.backtrack(index + 1):
                        return True
                    self.place_word(word, r, col, direction)  # Backtrack
            return False

    def print_solution(self):
        for row in self.grid:
            print(' '.join(row))


# Example usage
if __name__ == '__main__':
    crossword = CrosswordCSP(5)
    crossword.add_word('hello', 1, 1, 'across')
    crossword.add_word('world', 1, 3, 'down')
    crossword.solve()
    crossword.print_solution()
