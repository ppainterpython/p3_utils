# ---------------------------------------------------------------------------- +
#region p3_excel_files.py
""" Helpful functions concerning excel files."""
#endregion p3_excel_files.py
# ---------------------------------------------------------------------------- +
#region Imports
# Standard Package and Module Libraries
import psutil, shutil
from pathlib import Path
from typing import Callable as function
# Third-party Package and Module Libraries
import win32com.client
# Local Package and Module Libraries
from .p3_print_output_utils import out_msg, exc_msg, po, set_print_output, get_print_output
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
#region _refresh_test_excel_file(workbook_name : str = None) -> bool
def _refresh_test_excel_file() -> Path|None:
    """ Refresh a test excel workbook file. Internal to p3_excel_utils"""
    me = _refresh_test_excel_file
    global _excel
    try:
        _init_excel_files() # Always initialize first

        # Check for pristine test file availability.
        pristine_file = Path("tests/testdata/TestWorkbookPristine.xlsx").resolve()
        if not pristine_file.exists():
            _om(me,f"Pristine test workbook does NOT exist: '{pristine_file}'.")
            return None
        else:
            _om(me,f"Pristine test workbook does exist: '{pristine_file}'.")
        fresh_file = Path("tests/testdata/TestWorkbook.xlsx").resolve()
        if fresh_file.exists():
            _om(me,f"Removing existing test fresh workbook: '{fresh_file}'.")
            fresh_file.unlink()
        else:
            _om(me,f"Fresh test workbook does NOT exist: '{fresh_file}'.")
        shutil.copy(pristine_file,fresh_file)
        _om(me,f"Copied pristine test workbook to fresh test workbook: '{fresh_file}'.")
        return fresh_file
    except Exception as e:
        _em(me,e)
        raise
#endregion _refresh_test_excel_file(workbook_name : str = None) -> bool
# ---------------------------------------------------------------------------- +
# ---------------------------------------------------------------------------- +
#endregion Internal, private functions
# ---------------------------------------------------------------------------- +
#region Public functions
# ---------------------------------------------------------------------------- +
#region open_excel_file(workbook_name : str = None) -> bool
def open_excel_file(workbook_name : str = None) -> bool:
    """ Open an excel workbook file. """
    me = open_excel_file
    global _excel
    try:
        _init_excel_files() # Always initialize first
        if wb not in _excel.Workbooks:
            _om(me,f"'{workbook_name}' is not open.")
            wb = _excel.Workbooks.Open(workbook_name)
            _om(me,f"'{workbook_name}' opened.")
            return True
        else:
            _om(me,f"'{workbook_name}' is already open.")
            return False
        return False
    except Exception as e:
        _em(me,e)
        raise
#endregion open_excel_file(workbook_name : str = None) -> bool
# ---------------------------------------------------------------------------- +
#region close_excel_file(workbook_name : str = None) -> bool
def close_excel_file(workbook_name : str = None) -> bool:
    """ Close an excel workbook file  if open now. """
    me = close_excel_file
    global _excel
    try:
        _init_excel_files() # Always initialize first
        if workbook_name not in _excel.Workbooks:
            _om(me,f"'{workbook_name}' is not open.")
            return False
        return False
    except Exception as e:
        _em(me,e)
        raise
#endregion close_excel_file(workbook_name : str = None) -> bool
# ---------------------------------------------------------------------------- +
#region is_excel_file_open(workbook_name : str = None) -> bool
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
#endregion is_excel_file_open(workbook_name : str = None) -> bool
# ---------------------------------------------------------------------------- +
#region is_excel_running(workbook_name : str = None) -> bool
def is_excel_running(workbook_name : str = None) -> bool:
    """ Test if an excel application is running now. """
    me = is_excel_running
    global _excel
    try:
        for process in psutil.process_iter(attrs=["name"]):
                if "EXCEL.EXE" in process.info["name"]:
                    return True
        return False
    except Exception as e:
        _em(me,e)
        raise
#endregion is_excel_running(workbook_name : str = None) -> bool
# ---------------------------------------------------------------------------- +
#endregion Public functions
# ---------------------------------------------------------------------------- +
#region Local __main__ stand-alone
if __name__ == "__main__":
    try:
        me = __name__
        set_print_output(True)
        # is_excel_running()
        test_path : Path|None = _refresh_test_excel_file()
        wb_name = test_path.name
        if not is_excel_running():
            _om(me,f"Excel is NOT running.")
        open_excel_file(test_path)

        # Start Excel application
        # excel = win32com.client.Dispatch("Excel.Application")

        # Make Excel visible (optional, for debugging or interaction)
        # excel.Visible = True

        # wb_count = excel.Workbooks.Count
        # _om(me, f"Open workbooks({wb_count}):")
        # for wb in excel.Workbooks:
        #     _om(me,f"  '{wb.Name}'")

        # file_path = Path("C:\\Users\\ppain\\OneDrive\\budget\\boa\\data\\saved_BOAChecking2025.xlsx")
        # if is_excel_file_open(file_path.name):
        #     _om(me,f"'{file_path.name}' is open.")
        # else:
        #     # Open a specific Excel file
        #     workbook = excel.Workbooks.Open(file_path.name)

        # # Perform your tasks here...

        # # Close Excel (when you're done)
        # workbook.Close(SaveChanges=False)  # Set to True if you want to save changes
        # excel.Quit()
    except Exception as e:
        _om("__main__",e)
        _ = "pause"
    exit(1)
#endregion Local __main__ stand-alone