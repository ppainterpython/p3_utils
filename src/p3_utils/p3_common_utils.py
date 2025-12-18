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
import shutil, hashlib, sys, uuid
from pathlib import Path
from typing import Callable as function, Union
import importlib.util
import types

# Local Modules
from .p3_print_output_utils import *

#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
FORCE_EXCEPTION = "force_exception"
FORCE_EXCEPTION_MSG = "Forced exception for testing purposes."
#endregion Globals and Constants
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
#region has_property(obj,prop) -> bool
def has_property(obj:Union[object,dict], prop:str) -> bool:
    """p3_utils: Test whether obj has a property. Obj may be a class instance or a dict."""
    if isinstance(obj, dict):
        return prop in obj
    return hasattr(obj, prop)
#endregion has_property(obj,prop) -> bool
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
#region gen_hash_key(text: str, length:int=12) -> str
def gen_hash_key(text: str, length:int=12) -> str:
    """Generate a hash key from the input text."""
    # Create a SHA-256 hash of the input text
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    # Return the hexadecimal digest of the hash, truncated to the desired length
    return sha256.hexdigest()[:length]
#endregion gen_hash_key(text: str, length:int=12) -> str
# ---------------------------------------------------------------------------- +
#region gen_unique_hex_id()
def gen_unique_hex_id() -> str:
    """Generate a unique hexadecimal identifier based on random data."""
    # Generate 16 random bytes
    hex_string = uuid.uuid4().hex[:8]
    return hex_string
#endregion gen_unique_hex_id() -> str
# ---------------------------------------------------------------------------- +
#region impor_modeule_from_path()
def import_module_from_path(module_name: str, module_path: Path) -> types.ModuleType:
    """Import a module from a given file path."""
    try:
        if not module_path.exists():
            raise FileNotFoundError(f"Module path does not exist: {module_path}")
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec is None:
            raise ImportError(f"Could not load spec for module '{module_name}' from '{module_path}'")
        module = importlib.util.module_from_spec(spec)
        # Register in sys.modules BEFORE exec_module
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error importing module '{module_name}' from '{module_path}': {e}")
        raise
#endregion import_module_from_path()
# ---------------------------------------------------------------------------- +