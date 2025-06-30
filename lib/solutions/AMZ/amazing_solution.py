import subprocess
import sys
import os

class AmazingSolution:

    def amazing_maze(self, rows, columns, maze_generation_options):
        """
        Invokes the legacy amazing.py script, passing columns and rows to its stdin.
        Captures the ASCII maze from stdout and returns it as a string (excluding any legacy prompt).
        Only returns the lines after the last blank line in the output.
        """
        script_path = os.path.join(os.path.dirname(__file__), "amazing.py")
        input_data = f"{columns}\n{rows}\n"
        # Ensure maze_generation_options is a map and check for ENTRY_COLUMN
        if isinstance(maze_generation_options, dict) and "ENTRY_COLUMN" in maze_generation_options:
            entry_column = maze_generation_options["ENTRY_COLUMN"]
            if entry_column is not None:
                input_data += f"{entry_column}\n"
        result = subprocess.run(
            [sys.executable, script_path],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode()
        lines = output.splitlines()
        # Find the index of the last blank line
        last_blank_idx = len(lines) - 1
        while last_blank_idx >= 0 and lines[last_blank_idx].strip() == "":
            last_blank_idx -= 1
        # Now go backwards to find the previous blank line
        prev_blank_idx = last_blank_idx
        while prev_blank_idx >= 0 and lines[prev_blank_idx].strip() != "":
            prev_blank_idx -= 1
        # The maze is the lines after the last blank line before the end
        maze_lines = lines[prev_blank_idx + 1:]
        maze = "\n".join(maze_lines)
        return maze

if __name__ == "__main__":
    # Example usage with ENTRY_COLUMN as a map key
    result = AmazingSolution().amazing_maze(5, 5, { "ENTRY_COLUMN": "1" })  # Example usage
    print(result)