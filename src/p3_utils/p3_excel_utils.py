# ---------------------------------------------------------------------------- +
#region p3_excel_files.py
""" Helpful functions concerning excel files, uses p3_utils. 

    is_excel_file_open() - Check if an excel file is open now.
"""
#endregion p3_excel_files.py
# ---------------------------------------------------------------------------- +
#region Imports
# Standard Package and Module Libraries
import logging, os
from pathlib import Path
from typing import Callable as function

# Third-party Package and Module Libraries
import win32com.client

# Local Package and Module Libraries
from p3_utils import out_msg, exc_msg, po, set_print_output, get_print_output
#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
_excel = None
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
#region Internal, private functions
# ---------------------------------------------------------------------------- +
#region shortcut alias functions
def _po(msg) -> None:
    po(msg)
def _om(func,msg ) -> None:
    out_msg(func,msg)
def _em(func,e ) -> None:
    exc_msg(func,e)
#endregion shortcut alias functions
# ---------------------------------------------------------------------------- +
#region _init_excel_files() function
def _init_excel_files() -> None:
    """ Privately initialize excel_files as a singleton. """
    global _excel
    if _excel is None:
        try:
            _excel = win32com.client.Dispatch("Excel.Application") 
            _om(_init_excel_files,"Excel application initialized.")
        except Exception as e:
            _om(_init_excel_files,f"Failed to initialize Excel: {e}") 
            raise
#endregion init_excel_files() function
# ---------------------------------------------------------------------------- +
#endregion Internal, private functions
# ---------------------------------------------------------------------------- +
#region Public functions
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
        _em(me,e)
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
        _om(me, f"Open workbooks({wb_count}):")
        for wb in excel.Workbooks:
            _om(me,f"  '{wb.Name}'")

        file_path = Path("C:\\Users\\ppain\\OneDrive\\budget\\boa\\data\\saved_BOAChecking2025.xlsx")
        if is_excel_file_open(file_path.name):
            _om(me,f"'{file_path.name}' is open.")
        else:
            # Open a specific Excel file
            workbook = excel.Workbooks.Open(file_path.name)

        # Perform your tasks here...

        # Close Excel (when you're done)
        workbook.Close(SaveChanges=False)  # Set to True if you want to save changes
        excel.Quit()
    except Exception as e:
        _om("__main__",e)
        _ = "pause"
    exit(1)
#endregion Local __main__ stand-alone