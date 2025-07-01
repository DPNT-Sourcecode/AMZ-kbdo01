import math

class Main:
    def __init__(self, width=None, height=None, entry_column=1, magic_number=0.5, dead_end_behaviour="CREATE_EXIT"):
        self.width = width
        self.height = height
        self.entry_column = entry_column
        self.magic_number = magic_number
        self.dead_end_behaviour = dead_end_behaviour
        self._maze_lines = []
        self.current_line_char_count = 0

    def print_expr(self, expression):
        text = f"{expression:.2f}".rstrip('0').rstrip('.') if isinstance(expression, (int, float)) else str(expression)
        if not self._maze_lines:
            self._maze_lines.append("")
        self._maze_lines[-1] += text
        self.current_line_char_count += len(text)

    def println(self):
        self._maze_lines.append("")
        self.current_line_char_count = 0

    def tab(self, num_spaces):
        return ' ' * max(0, round(num_spaces - self.current_line_char_count))

    def as_int(self, variable):
        return int(round(variable))

    def round_down_to_int(self, variable):
        return math.floor(variable)

    def random(self, positive_int):
        return self.magic_number

    def generate_maze(self):
        self._maze_lines = []
        self.current_line_char_count = 0
        self._run_maze_logic()
        return "\n".join(line for line in self._maze_lines if line.strip() != "")

    def _run_maze_logic(self):
        H = self.width or int(input("Width: "))
        V = self.height or int(input("Height: "))
        entry_col = self.entry_column or 1
        dead_end_behaviour = self.dead_end_behaviour

        # Initialize maze arrays
        W = [[0] * (V + 2) for _ in range(H + 2)]
        VEC = [[0] * (V + 2) for _ in range(H + 2)]

        # Draw top border
        self.print_expr(".")
        for i in range(1, H + 1):
            self.print_expr("--" if i == entry_col else "  ")
            self.print_expr(".")
        self.println()

        # Maze generation (simple DFS for demonstration)
        stack = [(entry_col, 1)]
        visited = set()
        dead_end_on_last_row = None

        while stack:
            r, s = stack[-1]
            visited.add((r, s))
            VEC[r][s] = 1
            # Find unvisited neighbors
            neighbors = []
            for dr, ds in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, ns = r+dr, s+ds
                if 1 <= nr <= H and 1 <= ns <= V and (nr, ns) not in visited:
                    neighbors.append((nr, ns))
            if neighbors:
                stack.append(neighbors[0])
            else:
                # Dead end
                if r == H and dead_end_behaviour == "CREATE_TREASURE" and dead_end_on_last_row is None:
                    VEC[r][s] = 4  # Treasure chest
                    dead_end_on_last_row = (r, s)
                elif r == H and dead_end_behaviour == "CREATE_EXIT" and dead_end_on_last_row is None:
                    VEC[r][s] = 3  # Exit
                    dead_end_on_last_row = (r, s)
                stack.pop()

        # If no dead end on last row, place exit randomly (legacy behaviour)
        if dead_end_on_last_row is None:
            exit_col = int(self.random(1) * H + 1)
            VEC[exit_col][V] = 3

        # If treasure chest was placed, but random exit is in same column, remove chest
        if dead_end_on_last_row and dead_end_behaviour == "CREATE_TREASURE":
            if VEC[dead_end_on_last_row[0]][V] == 3:
                VEC[dead_end_on_last_row[0]][dead_end_on_last_row[1]] = 3

        # Render maze
        for j in range(1, V + 1):
            # Draw vertical walls and cells
            self.print_expr("I")
            for i in range(1, H + 1):
                cell = VEC[i][j]
                self.print_expr("<>" if cell == 4 else "  ")
                self.print_expr("I")
            self.println()
            # Draw bottom walls
            for i in range(1, H + 1):
                self.print_expr(":--" if VEC[i][j] == 3 else ":  ")
            self.print_expr(".")
            self.println()

    def run(self):
        print(self.generate_maze())

if __name__ == "__main__":
    # Example: Main(width=4, height=3, entry_column=1, dead_end_behaviour="CREATE_TREASURE").run()
    # For interactive use, just call Main().run()
    Main().run()



