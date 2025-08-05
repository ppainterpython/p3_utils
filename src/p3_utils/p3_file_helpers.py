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
from typing import List, Any, Type, Union

# third-party modules and packages
from .p3_common_utils import *
from .p3_helper_utils import is_not_obj_of_type, str_notempty
# local modules and packages
#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
#region find_folder()
def find_folder(folder_name: str, start_dir: Path = None):
    if start_dir is None:
        start_dir = Path.home()
    for path in start_dir.rglob(folder_name):
        if path.is_dir():
            return path  # Return the first match
    return None
#endregion find_folder()
# ---------------------------------------------------------------------------- +
#region copy_backup()
def copy_backup(src_path: Path, dst_folder: Union[Path,str]) -> list[Path]:
    """
    Create a backup copy of the specified file or directory.

    Args:
        src_path (Path): The source file or directory to back up.
        dst_folder (Path): The destination folder where the backup will be stored.

    Returns:
        list[Path]: A list of paths to the copied files.
    """
    try:
        copied_paths = []
        is_not_obj_of_type("src_path", src_path, Path,raise_error=True)
        if not src_path.exists(): return copied_paths

        if isinstance(dst_folder, str) and str_notempty(dst_folder):
            parent_path = src_path.parent
            dst_folder = parent_path / dst_folder
        if not dst_folder.exists():
            dst_folder.mkdir(parents=True, exist_ok=True)

        # Match files if src_path is a glob
        matched_files = list(src_path.parent.glob(src_path.name)) if "*" in src_path.name else [src_path]

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
        m = exc_err_msg(e)
        print(m)
        return copied_paths 
#endregion copy_backup()
# ---------------------------------------------------------------------------- +
#region is_file_locked(file_path : str =  None) -> bool
def is_file_locked(file_path : str|Path =  None, errors : str = 'forgive') -> bool:
    """p3_utils: Is a file locked by another process? """
    try:
        me = is_file_locked
        test_path : Path = None
        # Validate file_path is non-zero length str or Path object
        if (file_path is None or 
            not isinstance(file_path, Path) or
            (isinstance(file_path, str) and 
            len(file_path.name) <= 0)):
            # file_path is None or not a Path obj, or a non-zero length str
            if errors == 'strict':
                # 'strict' mode, raise error file_path not a str or Path object
                m = out_msg(me, f"Invalid file_path: type=" 
                                f"'{type(file_path).__name__}', value='{file_path}'")
                raise TypeError(m)
            return False # add errors support here
        elif isinstance(file_path, str) and len(file_path.strip()) > 0:
            # convert str file_path to Path obj
            test_path = Path(file_path)
        else:
            # file_path is a Path object
            test_path = file_path
        # Validate the test_path is reachable
        if not test_path.is_absolute():
            # Resolve the path before checking if it exists
            test_path = test_path.resolve()
        # Check if the file exists
        if not test_path.exists():
            # Non-existing file cannot be locked, but error?
            return False            
            # file_path is not a str or Path object
            # TODO: support error param for selecting what to do about errors
            # 'forgive' mode, default, try to forgive and continue the mission 
            # if errors == 'forgive': return False
            # if errors == 'strict':
            #     # 'strict' mode, raise error file_path not a str or Path object
            #     m = out_msg(me, f"Invalid file_path: type=" 
            #                     f"'{type(file_path).__name__}', value='{file_path}'")
            #     raise TypeError(m)
        # To check a lock, attempt to rename the file
        temp_path = test_path.with_suffix(test_path.suffix + ".temp")
        if temp_path.exists():
            # If the temp file already exists, remove it
            temp_path.unlink()
        backup_path = test_path.with_suffix(test_path.suffix + ".bak")
        if backup_path.exists():
            # If the backup file already exists, remove it
            backup_path.unlink()
        # copy the original file to a backup
        shutil.copy(test_path,backup_path)  
        # rename test_path to temp_path
        # This will raise a PermissionError if the file is locked
        test_path.rename(temp_path)  # Rename to temp
        # must not be locked, so undo the rename
        temp_path.rename(test_path)  # Rename back to original
        return False  # File is not locked - Happy Path
    except TypeError as e:
        po(str(e))
        if errors == 'strict':
            raise
        return False
    except PermissionError as e:
        po(str(e))
        if errors == 'strict':
            raise
        return True   # File is locked - Happy Path
    except FileNotFoundError as e:
        po(str(e))
        if errors == 'strict':
            raise
        return False
    except Exception as e:
        po(str(e))
        if errors == 'strict':
            raise
        return False
#endregion is_file_locked(file_path : str =  None) -> bool
# ---------------------------------------------------------------------------- +
#region is_filename_only(path_str: str = None) -> bool
def is_filename_only(path_str: str = None) -> bool:
    """p3_utils: Check path_str as name of file only, no parent. """
    # Validate input
    if (path_str is None or not isinstance(path_str, str) or 
        len(path_str.strip()) == 0):
        raise TypeError(f"Invalid path_str: type='{type(path_str).__name__}', "
                        f"value='{path_str}'")
    path = Path(path_str)
    # Check if the path has no parent folders    
    return path.parent == Path('.')
#endregion is_filename_only(path_str: str = None) -> bool
# ---------------------------------------------------------------------------- +
#region is_valid_path(value_name:str,value:Path,test:bool = True,raise_error:bool=True) -> bool
def is_valid_path(value_name:str,value:Path,test:bool = True,raise_error:bool=True) -> bool:
    """p3_utils: Check if a Path object is valid."""
    # Validate input
    if value_name is None or not isinstance(value_name, str) or len(value_name.strip()) == 0:
        value_name = "not-provided"
    if value is None or not isinstance(value, Path):
        if raise_error:
            raise TypeError(f"Invalid {value_name}: type='{type(value).__name__}', value='{value}'")
        return False
    if test and not value.exists():
        if raise_error:
            raise FileNotFoundError(f"{value_name} does not exist: {value}")
        return False
    return True
#endregion is_valid_path(value_name:str,value:Path,test:bool = True,raise_error:bool=True) -> bool
