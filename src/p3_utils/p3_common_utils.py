# ---------------------------------------------------------------------------- +
#region p3_utils.py
# ---------------------------------------------------------------------------- +
""" Helpful functions not dependent on any other p3 modules. 

    is_filename_only() - Check if a path is a filename only, no parent folders.
    append_cause() - Append the cause chain of an exception to the message.
    fpfx() - Return a prefix for the function name and its module.
    force_exception() - Force an exception to test exception handling.
    t_of() - Return the type of an object as a string.
    v_of() - Return the value of an object as a string.
    check_testcase() - Raise test case exception if var = p3l.FORCE_EXCEPTION.
    is_file_locked() - Check if a file is locked by another process.

    Explanation:
    ------------
    These functions are intended to be helpful and low overhead. So, some
    support the convention of a keyword argument 'errors' to select the action
    to take on error. The default is 'forgive' which means to try to continue
    the mission of the function. The 'strict' mode raises an error if the
    function cannot continue. The 'forgive' mode is the default and is used
    throughout the p3_utils module. The 'strict' mode is used in the test cases
    to force an exception to be raised.

    Our goal is 100% test coverage, as painful as that is to accomplish. 
    Designing code to be testable A principle applied to the p3_utils module. 
"""
#endregion p3_utils.py
# ---------------------------------------------------------------------------- +
#region Imports
# Standard Module Libraries
import shutil
from pathlib import Path
from typing import Callable as function

# Local Modules
from .p3_print_output_utils import *

#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
FORCE_EXCEPTION = "force_exception"
FORCE_EXCEPTION_MSG = "Forced exception for testing purposes."
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
#region is_filename_only(path_str: str = None) -> bool
def is_filename_only(path_str: str = None) -> bool:
    """p3_utils: Check path_str as name of file only, no parent. """
    # Validate input
    if path_str is None or not isinstance(path_str, str) or len(path_str.strip()) == 0:
        raise TypeError(f"Invalid path_str: type='{type(path_str).__name__}', value='{path_str}'")
    
    path = Path(path_str)
    # Check if the path has no parent folders    
    return path.parent == Path('.')
#endregion is_filename_only(path_str: str = None) -> bool
# ---------------------------------------------------------------------------- +
#region append_cause(msg:str = None, e:Exception=None, depth:int=0) -> str
def append_cause(msg:str = None, e:Exception=None, depth:int=0) -> str:
    """p3_utils: Trace and exception chain appending the causes """
    # If the exception has a cause, append the chain up to depth
    exc = e
    msg = ""
    t1 = t2 = True
    while t1 or t2:
        msg += f"Exception({depth}): {str(exc)}"
        msg += f" >>> " if depth > 0 else ""
        t1 = exc.__cause__ is not None and exc != exc.__cause__ 
        t2 = exc.__context__ is not None and exc != exc.__context__
        exc = exc.__cause__ or exc.__context__
        depth -= 1 if depth > 0 else 0
    return msg 
#endregion append_cause(msg:str = None, e:Exception=None, depth:int=0) -> str
# ---------------------------------------------------------------------------- +
#region force_exception(func, e:Exception=None
def force_exception(func, e:Exception=None) -> str:
    """p3_utils: Raise exception e from func as caller, default ZeroDivisionError. """
    func = force_exception if func is None else func
    dm = f"testcase: Default Exception Test for func:{func.__name__}()"
    e = ZeroDivisionError(dm) if e is None else e
    raise e
#endregion fpfx(func, e:Exception=None
# ---------------------------------------------------------------------------- +
#region t_of(obj) -> str
def t_of(obj) -> str:
    """p3_utils: Return type of obj as string."""
    return f"type({type(obj).__name__})"
#endregion t_of() function
# ---------------------------------------------------------------------------- +
#region v_of(obj) -> str
def v_of(obj) -> str:
    """p3_utils: Return value of obj as string."""
    return f"value = '{str(obj)}'"
#endregion v_of(obj) -> str
# ---------------------------------------------------------------------------- +
#region check_testcase(func, var : str, exc : str = "ZeroDivisionError") -> str
def check_testcase(func, var : str, exc : str = "ZeroDivisionError") -> str:
    """p3_utils: Raise test case exception exc if var = p3l.FORCE_EXCEPTION. 
    
    Used in functions and methods to enable test cases to force an exception
    to test exception handling.

    Args:
        func (function): The function calling for the check.
        var (str): The variable to be checked as equal to prl.FORCE_EXCEPTION.
        exc (str): The exception class name to be raised.

    Returns:
        str: A short string explaining why no exception was raised.

    Raises:
        Exception: of the class name passed in the exc argument

    """
    # Validate input
    if var is None or not isinstance(var, str) or len(var.strip()) == 0:
        return F"param 'var' is not a non-empty string {v_of(var)}."
    if var != FORCE_EXCEPTION:
        return F"param 'var' is not equal to p3l.FORCE_EXCEPTION {v_of(var)}."
    if exc is None or not isinstance(var, str) or len(var.strip()) == 0:
        return F"param 'exc' is not a non-empty string {v_of(exc)}."
    func_valid = True if func is not None and isinstance(func, function) else False
    func_name = func.__name__ if func_valid else "unknownFunction"
    try:
        import builtins
        try:
            exc_class = getattr(builtins,exc)
            if exc_class is None or not isinstance(exc_class, type):
                return f"param 'exc' {v_of(exc)} is not a valid exception class name."
            dm = f"testcase: {exc} Exception Test for func:{func_name}()"
            te = exc_class(dm)
            raise te
        except AttributeError as e:
            return f"param 'exc' {v_of(exc)} error retrieving from builtins: str{e}."
    except Exception as e:
        if e == te:
            raise e
        return f"Error creating {exc}(), msg = '{str(e)}'"
#endregion check_testcase(func, var : str, exc : str = "ZeroDivisionError") -> str
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
#endregion Public functions
# ---------------------------------------------------------------------------- +
#region Local __main__ stand-alone
if __name__ == "__main__":
    try:
        me = __name__
        set_print_output(True)
    except Exception as e:
        print(exc_msg("__main__",e))
        _ = "pause"
    exit(0)
#endregion Local __main__ stand-alone