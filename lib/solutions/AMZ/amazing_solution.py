import subprocess
import sys
import os

class AmazingSolution:

    def amazing_maze(self, rows, columns, maze_generation_options):
        """
        Invokes the legacy amazing.py script, passing columns and rows to its stdin.
        Captures the ASCII maze from stdout and returns it as a string (excluding any legacy prompt).
        """
        script_path = os.path.join(os.path.dirname(__file__), "amazing.py")
        input_data = f"{columns}\n{rows}\n"
        result = subprocess.run(
            [sys.executable, script_path],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode()
        # Remove any legacy prompt if present (e.g., trailing input prompts)
        # This assumes the maze is the first part of the output, and any prompt is after a newline
        maze = output.strip()
        return maze
if __name__ == "__main__":
    result = AmazingSolution().amazing_maze(5, 5, None)  # Example usage
    print(f"Script executed with return code: {result}")

