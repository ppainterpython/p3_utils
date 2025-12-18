# ---------------------------------------------------------------------------- +
#region p3_print_output_utils.py
# ---------------------------------------------------------------------------- +
""" Helpful output functions used by other p3 modules but not depending on p3. 

    out_msg() - Return a simple error message for an exception.
    exc_msg() - Return a simple exception message for an exception.
"""
#endregion p3_utils.py
# ---------------------------------------------------------------------------- +
#region Imports
# Standard Package and Module Libraries
from typing import Callable as function
from pathlib import Path
import traceback, io, sys

# Third-party Package and Module Libraries
from treelib import Tree

# Local Package and Module Libraries

#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
_print_output: bool = False
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
#region Public functions
# ---------------------------------------------------------------------------- +
#region get_print_output(print_errors: bool = False) -> None
def get_print_output() -> bool:
    """ Get the print_errors flag. """
    global _print_output
    return _print_output
#endregion get_print_output(print_errors: bool = False) -> None
# ---------------------------------------------------------------------------- +
#region set_print_output(print_errors: bool = False) -> None
def set_print_output(print_errors: bool = False) -> None:
    """ Set the print_errors flag. """
    global _print_output
    _po = _print_output = print_errors
#endregion set_print_output(print_errors: bool = False) -> None
# ---------------------------------------------------------------------------- +
#region po(msg:str) -> None Print Output based on "print_output" flag
def po(msg : str = "") -> None:
    if _print_output: print(msg)
#endregion po(msg:str) -> None Print Output based on "print_output" flag
# ---------------------------------------------------------------------------- +
#region first_n(msg:str, n:int) -> None Print first n characters of msg
def first_n(msg : str = "", n : int = 40) -> None:
    """Print first n characters of string."""
    if msg is None: return None
    delta = len(msg) - n
    if delta > 0:
        return f"{msg[:n]}...<{delta} more characters>"
    return msg
#endregion first_n(msg:str, n:int) -> None Print first n characters of msg
# ---------------------------------------------------------------------------- +
#region out_msg(func:function,msg : str = "no message") -> str
def out_msg(func:callable,msg : str = "no message") -> str:
    """
    Return a str with a prefixed by func info.
    
    Within a function, use for common output message style. 
    
    Args:
        func (function): The function or string for prefix.
        msg (str): The message content.
        
    Returns:
        str: Returns the prefixed message.    
    """
    try:
        if func is not None or isinstance(func, function) or isinstance(func, str):
            m = f"{fpfx(func)} '{msg}'"
        else : 
            fn = f"Invalid func param:'{str(func)}'"
            m = f"out_msg({fn}): '{msg}'"
        po(m)
        return m
    except Exception as e:
        et = type(e).__name__
        po(f"p3_utils.out_msg() Error:  {et}({str(e)})")
        raise
#endregion out_msg(func:function,msg : str = "no message") -> str
# ---------------------------------------------------------------------------- +
#region exc_msg(func:function,e:Exception) -> str
def exc_msg(func : callable, e : Exception) -> str:
    """
    Return str with common simple output message for Exceptions.
    
    Within a function, use to emit a message in except: blocks. 
    
    Args:
        func (function): The function where the exception occurred.
        e (Exception): The exception object.
        
    Returns:
        str: Returns the prefixed exception message.    
    """
    try:
        et = type(e).__name__
        if func is not None or isinstance(func, function) or isinstance(func, str):
            m = f"{fpfx(func)}{et}({str(e)})"
        else : 
            fn = f"Invalid func param:'{str(func)}'"
            m = f"exc_msg({fn}): '{str(e)}'"
        po(m)
        return m
    except Exception as e:
        po(f"p3_utils.exc_msg() Exception: {et}({str(e)})")
        raise
#endregion exc_msg(func:function,e:Exception) -> str
# ---------------------------------------------------------------------------- +
#region exc_err_msg(e:Exception) -> str
def exc_err_msg(e : Exception) -> str:
    """
    Return common simple output message for Exceptions.
    
    Within a function, use to log a message in except: blocks. 
    
    Args:
        e (Exception): The exception object.
        
    Returns:
        str: Returns the prefixed exception message.    
    """
    try:
        tb = traceback.extract_tb(e.__traceback__)
        filepath, line_number, function_name, text = tb[-1]
        filename = Path(filepath).name
        et = type(e).__name__
        m = f"{et}({str(e)}) at {function_name}() in {filename}:{line_number}"
        po(m)
        return m
    except Exception as e:
        po(f"p3_utils.exc_msg() Exception: {et}({str(e)})")
        raise
#endregion exc_err_msg(e:Exception) -> str
# ---------------------------------------------------------------------------- +
#region fpfx(func : Callable) -> str) function
def fpfx(func : callable) -> str:
    """ Function PreFiX: Return a str name of function func and its module. """
    try:
        if func is not None and isinstance(func, function):
            mod_name = func.__globals__['__name__']
            func_name = func.__name__
            # Helping out the test cases only.
            if func_name == "force_exception":
                1 / 0
            return f"{mod_name}.{func_name}():"
        elif isinstance(func, str):
            return f"{func}():"
        else: 
            return f"UnknownFunction({str(func)}):"
    except Exception as e:
        po(f"fpfx() Error: {str(e)}")
        raise
#endregion fpfx(func : Callable) -> str) function
# ---------------------------------------------------------------------------- +
#region dscr(_inst) -> str
def dscr(_inst) -> str:
    """Return a descriptor (dscr) of the object _inst."""
    try:
        if _inst is None: return "None"
        _id = hex(id(_inst))
        _cn = _inst.__class__.__name__
        return f"<instance '{_cn}':{_id}>"
    except Exception as e:
        return f"{type(e).__name__}()"
#endregion dscr(_inst) -> str
# ---------------------------------------------------------------------------- +
#region split_parts()
def split_parts(src: str, delimiter: str='.', size: int=3) -> list:
    # Split the source string by the delimiter
    parts = src.split(delimiter)
    
    # If the split result is shorter than the desired size, pad with empty strings
    result = parts[:size] + [''] * (size - len(parts))
    
    # If the split result is longer than the desired size, truncate it
    return result[:size]
#endregion split_parts()
# ---------------------------------------------------------------------------- +
#region    format_tree_view() function
def format_tree_view(tree_view:Tree=None) -> str:
    """Format a Tree object for console output."""
    try:
        if not isinstance(tree_view, Tree):
            raise TypeError("Invalid tree_view parameter: Expected a Tree object.")
        # Format the tree for console output
        original_stdout = sys.stdout  # Save the original stdout
        buffer = io.StringIO()
        sys.stdout = buffer  # Redirect stdout to capture tree output
        tree_view.show()
        sys.stdout = original_stdout  # Reset stdout
        return buffer.getvalue()
    except Exception as e:
        m = exc_err_msg(e)
        return m
#endregion format_tree_view() function
# ---------------------------------------------------------------------------- +
#endregion Public functions
# ---------------------------------------------------------------------------- +