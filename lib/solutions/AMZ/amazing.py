import math

def amazing_maze(rows, columns, options):
    DEAD_END_ON_LAST_ROW_BEHAVIOUR = options.get("DEAD_END_ON_LAST_ROW_BEHAVIOUR", "CREATE_EXIT")
    ENTRY_COLUMN = int(options.get("ENTRY_COLUMN", 1))
    # Legacy random number generator stub (always 0.5 for deterministic output)
    def legacy_random():
        return 0.5

    # 1-indexed for legacy compatibility
    H, V = columns, rows
    W = [[0] * (V + 2) for _ in range(H + 2)]
    VEC = [[0] * (V + 2) for _ in range(H + 2)]
    output = []
    line = ""

    def print_expr(expr):
        nonlocal line
        line += str(expr)

    def println():
        nonlocal line
        output.append(line.rstrip())
        line = ""

    # Draw top border
    line += "."
    for i in range(1, H + 1):
        if i == ENTRY_COLUMN:
            line += "--"
        else:
            line += "  "
        line += "."
    println()

    # Maze generation variables
    C = 1
    X = ENTRY_COLUMN
    W[X][1] = C
    C += 1
    R, S = X, 1

    # Maze generation algorithm (simplified for this round's requirements)
    # We'll use a simple DFS to fill the maze, marking dead ends
    stack = [(R, S)]
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
            nr, ns = neighbors[0]
            stack.append((nr, ns))
        else:
            # Dead end
            if r == H and DEAD_END_ON_LAST_ROW_BEHAVIOUR == "CREATE_TREASURE" and dead_end_on_last_row is None:
                VEC[r][s] = 4  # Treasure chest
                dead_end_on_last_row = (r, s)
            elif r == H and DEAD_END_ON_LAST_ROW_BEHAVIOUR == "CREATE_EXIT" and dead_end_on_last_row is None:
                VEC[r][s] = 3  # Exit
                dead_end_on_last_row = (r, s)
            stack.pop()

    # If no dead end on last row, place exit randomly (legacy behaviour)
    if dead_end_on_last_row is None:
        exit_col = int(legacy_random() * H + 1)
        VEC[exit_col][V] = 3

    # If treasure chest was placed, but random exit is in same column, remove chest
    if dead_end_on_last_row and DEAD_END_ON_LAST_ROW_BEHAVIOUR == "CREATE_TREASURE":
        exit_col = None
        if VEC[dead_end_on_last_row[0]][V] == 3:
            # Remove the treasure chest
            VEC[dead_end_on_last_row[0]][dead_end_on_last_row[1]] = 3

    # Render maze
    for j in range(1, V + 1):
        # Draw vertical walls and cells
        line = ""
        for i in range(1, H + 1):
            if i == 1:
                line += "I"
            cell = VEC[i][j]
            if cell == 4:
                line += "<>"
            else:
                line += "  "
            line += "I"
        println()
        # Draw bottom walls
        line = ""
        for i in range(1, H + 1):
            if VEC[i][j] == 3:
                line += ":--"
            else:
                line += ":  "
        line += "."
        println()

    return "\n".join(output)

# Example usage:
if __name__ == "__main__":
    # For manual testing
    rows = 3
    columns = 4
    options = {"ENTRY_COLUMN": "1", "DEAD_END_ON_LAST_ROW_BEHAVIOUR": "CREATE_TREASURE"}
    print(amazing_maze(rows, columns, options))


