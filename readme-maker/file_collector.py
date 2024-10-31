import os
from fnmatch import fnmatch

def is_ignored(path, ignore_patterns):
    return any(fnmatch(path, pattern) for pattern in ignore_patterns)

def collect_files_content(file_types, ignore_patterns, truncate_limit=1000):
    files_content = ""
    for root, dirs, files in os.walk(".."):
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), ignore_patterns)]
        for file in files:
            file_path = os.path.join(root, file).lstrip("./")
            if is_ignored(file_path, ignore_patterns) or not any(file.endswith(ext.strip("*")) for ext in file_types):
                continue
            try:
                with open(file_path, "r") as f:
                    content = f.read(truncate_limit) if os.path.getsize(file_path) > truncate_limit else f.read()
                    files_content += f"\n\n### File: {file_path}\n{content}... (truncated)" if len(content) == truncate_limit else content
            except (FileNotFoundError, IsADirectoryError):
                continue
    return files_content