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
import traceback

# Third-party Package and Module Libraries

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
    Retrun a str with common simple output message for Exceptions.
    
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
#region exc_err_msg(func:function,e:Exception) -> str
def exc_err_msg(e : Exception) -> str:
    """
    Retrun common simple output message for Exceptions, no caller prefix.
    
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
#endregion exc_msg(func:function,e:Exception) -> str
# ---------------------------------------------------------------------------- +
#region fpfx(func : Callable) -> str) function
def fpfx(func : callable) -> str:
    """ Function PreFiX: Return a str name of function func and its module. """
    try:
        if func is not None and isinstance(func, function):
            mod_name = func.__globals__['__name__']
            func_name = func.__name__
            # Helpling out the test cases only.
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
#endregion Public functions
# ---------------------------------------------------------------------------- +