"""
p3_utils - A collection of utility functions for p3 projects.

Modules:
- p3_print_output_utils: Functions for logging and output formatting.
- p3_common_utils: General-purpose utility functions.
- p3_excel_utils: Functions for working with Excel files.

Usage:
    import p3_utils as p3u
    p3u.out_msg(...)
    p3u.is_excel_file_open(...)
"""

__version__ = "0.1.0"
__author__ = "Paul Painter"

from .p3_print_output_utils import (
    out_msg, 
    exc_msg, 
    po, 
    set_print_output, 
    get_print_output, 
    fpfx
)
from .p3_common_utils import (
    is_filename_only, 
    is_file_locked, 
    t_of, 
    v_of, 
    append_cause, 
    force_exception, 
    check_testcase 
)
from .p3_excel_utils import is_excel_file_open

# from .at_utils import * 

# ---------------------------------------------------------------------------- +
# Exported functions and classes from p3_utils package.
# The intent is for "import p3_utils as p3u" to import all of the functions and classes
__all__ = [
    "check_testcase",
    "v_of",
    "t_of",
    "is_filename_only",
    "append_cause",
    "fpfx",
    "out_msg",
    "exc_msg",
    "force_exception",
    "is_file_locked",
    "get_print_output",
    "po",
    "set_print_output",
    "is_excel_file_open"
]