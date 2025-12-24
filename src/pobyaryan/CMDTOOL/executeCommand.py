import os
import subprocess
from pathlib import Path


class EXECUTE_COMMAND_TOOL:
    
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir or os.getcwd())

    def execute_command(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            return f"Output:\n{result.stdout}\nErrors:\n{result.stderr}"
        except Exception as e:
            return f"Execution failed: {str(e)}"