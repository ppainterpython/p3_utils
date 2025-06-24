# ---------------------------------------------------------------------------- +
#region p3_file_helpers.py
"""
#region p3_file_helpers: common, pesky file operations.

"""
#endregion #region p3_file_helpers.py
# ---------------------------------------------------------------------------- +
#region Imports
# ---------------------------------------------------------------------------- +
# python standard library modules and packages
import shutil
from pathlib import Path, PurePath
from typing import List, Any, Type

# third-party modules and packages

# local modules and packages
#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
def copy_backup(src_path: Path, dst_folder: Path) -> list[Path]:
    try:
        if not dst_folder.exists():
            dst_folder.mkdir(parents=True, exist_ok=True)

        # Match files if src_path is a glob
        matched_files = list(src_path.parent.glob(src_path.name)) if "*" in src_path.name else [src_path]

        copied_paths = []

        for file in matched_files:
            if not file.is_file():
                continue  # skip directories or invalid files

            original_stem = file.stem
            suffix = file.suffix

            # Find the next available versioned filename
            version = 1
            while True:
                new_name = f"{original_stem}_v{version}{suffix}"
                dst_path = dst_folder / new_name
                if not dst_path.exists():
                    break
                version += 1

            shutil.copy2(file, dst_path)
            copied_paths.append(dst_path)

        return copied_paths
    except Exception as e:
        m = p3u.exc_err_msg(e)
        print(m)
        raise 
# ---------------------------------------------------------------------------- +
