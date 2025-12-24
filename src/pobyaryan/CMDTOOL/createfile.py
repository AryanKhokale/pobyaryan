import os
from pathlib import Path


class CREATE_FILE_TOOL:

    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir or os.getcwd())


    def create_file(self, file_path, content=""):
        full_path = self.base_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"File created: {full_path}"