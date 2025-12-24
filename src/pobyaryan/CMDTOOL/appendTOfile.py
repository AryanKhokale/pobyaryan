import os
from pathlib import Path


class APPPEND_TO_FILE_TOOL:

    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir or os.getcwd())


    def append_to_file(self, file_path, content):
        full_path = self.base_dir / file_path
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(content)
        return f"Content appended to: {full_path}"