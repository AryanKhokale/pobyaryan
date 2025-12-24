import os
from pathlib import Path


class DELETE_PATH_TOOL:

    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir or os.getcwd())
        

    def delete_path(self, path_str):
        full_path = self.base_dir / path_str
        if full_path.is_dir():
            os.rmdir(full_path)
            return f"Folder deleted: {full_path}"
        elif full_path.is_file():
            os.remove(full_path)
            return f"File deleted: {full_path}"
        else:
            return f"Path not found: {full_path}"