# ---------------------------------------------------------------------------- +
#region p3_excel_files.py
""" Helpful functions concerning excel files, uses p3_utils. 

    is_excel_file_open() - Check if an excel file is open now.
    get_print_output() - Get the print_output flag.
    set_print_output() - Set the print_output flag.
"""
#endregion p3_excel_files.py
# ---------------------------------------------------------------------------- +
#region Imports
# Standard Module Libraries
import logging, os
from pathlib import Path
from typing import Callable as function

# Third-party Libraries
import win32com.client

# Local Modules
import p3_utils as p3u
#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
_excel = None
_print_output: bool = False
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
#region Internal, private functions
#region _init_excel_files() function
def _init_excel_files() -> None:
    """ Privately initialize excel_files as a singleton. """
    global _excel
    if _excel is None:
        try:
            _excel = win32com.client.Dispatch("Excel.Application") 
            print("Excel application initialized.") if _print_output else None
        except Exception as e:
            print(f"Failed to initialize Excel: {e}") if _print_output else None
            raise
#endregion init_excel_files() function
# ---------------------------------------------------------------------------- +
#region _exc() function
def _exc(func: function, e : Exception = None) -> str:
    """ Simple common messaging for Exceptions. """
    global _print_output
    if _print_output:
        try:
            m = p3u.exc_msg(func, e)
            print(p3u.exc_msg(func, e))
        except Exception as e:
            et = type(e).__name__
            print(f"p3_excel_files._exc(): ({et}):({str(e)})")
            raise
#endregion init_excel_files() function
# ---------------------------------------------------------------------------- +
#region _exc(func: function, msg : str = None) -> str
def _err(func: function, msg : str = None) -> str:
    """ Simple common messaging for Exceptions. """
    global _print_output
    m = None
    if _print_output:
        try:
            m = p3u.err_msg(func, msg)
            print(m)
        except Exception as e:
            et = type(e).__name__
            print(f"p3_excel_files._err(): ({et}):({str(e)})")
            raise
    return m
#endregion _err(func: function, msg : str = None) -> str
# ---------------------------------------------------------------------------- +
#region _msg() function
def _msg(func: function, msg : str = None) -> str:
    """ Simple common wrapper for messaging. """
    global _print_output
    m = None
    if _print_output:
        try:
            m = f"{p3u.fpfx(func)}{msg}"
            print(m)
        except Exception as e:
            et = type(e).__name__
            print(f"p3_excel_files._msg(): Exception: ({et}):({str(e)})")
            raise
    return m
#endregion init_excel_files() function
# ---------------------------------------------------------------------------- +
#endregion Internal, private functions
# ---------------------------------------------------------------------------- +
#region Public functions
#region get_print_output(print_errors: bool = False) -> None
def get_print_output(print_errors: bool = False) -> None:
    """ Get the print_errors flag. """
    global _print_output
    _print_output = print_errors
#endregion get_print_output(print_errors: bool = False) -> None
# ---------------------------------------------------------------------------- +
#region set_print_output(print_errors: bool = False) -> None
def set_print_output(print_errors: bool = False) -> None:
    """ Set the print_errors flag. """
    global _print_output
    _print_output = print_errors
#endregion set_print_output(print_errors: bool = False) -> None
# ---------------------------------------------------------------------------- +
#region _init_excel_files(workbook_name : str = None) -> bool
def is_excel_file_open(workbook_name : str = None) -> bool:
    """ Test if an excel file is open now. """
    me = is_excel_file_open
    global _excel
    try:
        _init_excel_files()
        for wb in _excel.Workbooks:
            if wb.name == workbook_name:
                return True
        return False
    except Exception as e:
        _exc(me,e)
        raise
#endregion init_excel_files(workbook_name : str = None) -> bool
# ---------------------------------------------------------------------------- +
#endregion Public functions
# ---------------------------------------------------------------------------- +
#region Local __main__ stand-alone
if __name__ == "__main__":
    try:
        me = __name__
        set_print_output(True)
        # Start Excel application
        excel = win32com.client.Dispatch("Excel.Application")

        # Make Excel visible (optional, for debugging or interaction)
        # excel.Visible = True

        wb_count = excel.Workbooks.Count
        _msg(me, f"Open workbooks({wb_count}):")
        for wb in excel.Workbooks:
            _msg(me,f"  '{wb.Name}'")

        file_path = Path("C:\\Users\\ppain\\OneDrive\\budget\\boa\\data\\saved_BOAChecking2025.xlsx")
        if is_excel_file_open(file_path.name):
            _msg(me,f"'{file_path.name}' is open.")
        else:
            # Open a specific Excel file
            workbook = excel.Workbooks.Open(file_path.name)

        # Perform your tasks here...

        # Close Excel (when you're done)
        workbook.Close(SaveChanges=False)  # Set to True if you want to save changes
        excel.Quit()
    except Exception as e:
        print(p3u.exc_msg("__main__",e))
        _ = "pause"
    exit(1)
#endregion Local __main__ stand-alone