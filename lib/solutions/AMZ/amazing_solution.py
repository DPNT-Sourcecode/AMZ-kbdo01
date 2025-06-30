import subprocess
import sys
import os

class AmazingSolution:

    def amazing_maze(self, rows, columns, maze_generation_options):
        """
        Invokes the legacy amazing.py script, passing columns and rows to its stdin.
        """
        script_path = os.path.join(os.path.dirname(__file__), "amazing.py")
        # Prepare the input as required: columns first, then rows, each on a new line
        input_data = f"{columns}\n{rows}\n"
        # Run the script and pass the input
        result = subprocess.run(
            [sys.executable, script_path],
            input=input_data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # Optionally, you can return result.stdout.decode() if you want the output
        return result.returncode

