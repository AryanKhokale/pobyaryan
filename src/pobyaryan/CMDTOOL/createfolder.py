import os
from pathlib import Path


class CREATE_FOLDER_TOOL:

    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir or os.getcwd())

    def create_folder(self, folder_name):
        path = self.base_dir / folder_name
        path.mkdir(parents=True, exist_ok=True)
        return f"Folder created: {path}"