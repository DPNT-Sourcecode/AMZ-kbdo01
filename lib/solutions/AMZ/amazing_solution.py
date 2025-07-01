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

        # Always check for ENTRY_COLUMN first, then LEGACY_RANDOM_MAGIC_NUMBER, then DEAD_END_ON_LAST_ROW_BEHAVIOUR
        entry_column = ""
        magic_number = ""
        dead_end_behaviour = ""

        if isinstance(maze_generation_options, dict):
            if "ENTRY_COLUMN" in maze_generation_options and maze_generation_options["ENTRY_COLUMN"] is not None:
                entry_column = str(maze_generation_options["ENTRY_COLUMN"])
            if "LEGACY_RANDOM_MAGIC_NUMBER" in maze_generation_options and maze_generation_options["LEGACY_RANDOM_MAGIC_NUMBER"] is not None:
                magic_number = str(maze_generation_options["LEGACY_RANDOM_MAGIC_NUMBER"])
            if "DEAD_END_ON_LAST_ROW_BEHAVIOUR" in maze_generation_options and maze_generation_options["DEAD_END_ON_LAST_ROW_BEHAVIOUR"] is not None:
                dead_end_behaviour_str = str(maze_generation_options["DEAD_END_ON_LAST_ROW_BEHAVIOUR"])

        # Add ENTRY_COLUMN (or blank line)
        input_data += f"{entry_column}\n"
        # Add LEGACY_RANDOM_MAGIC_NUMBER (or blank line)
        input_data += f"{magic_number}\n"
        # Add DEAD_END_ON_LAST_ROW_BEHAVIOUR (or blank line)
        if dead_end_behaviour_str == "CREATE_TREASURE":
            input_data += f"1\n"
        elif dead_end_behaviour_str == "CREATE_EXIT":
            input_data += f"0\n"
        else:
            input_data += f"\n"

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
    # Example usage with DEAD_END_ON_LAST_ROW_BEHAVIOUR as a map key
    #result = AmazingSolution().amazing_maze(3, 4, { "ENTRY_COLUMN": "1", "DEAD_END_ON_LAST_ROW_BEHAVIOUR": "CREATE_TREASURE" })  # Example
    result = AmazingSolution().amazing_maze(3, 4, { "ENTRY_COLUMN": "1", "DEAD_END_ON_LAST_ROW_BEHAVIOUR": "CREATE_EXIT" })  # Example
    #result = AmazingSolution().amazing_maze(2, 2, { "LEGACY_RANDOM_MAGIC_NUMBER": "0.5" })  # Example
    print(result)