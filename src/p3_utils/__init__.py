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
    exc_err_msg,
    po, 
    set_print_output, 
    get_print_output, 
    fpfx
)
from .p3_common_utils import (
    FORCE_EXCEPTION,
    FORCE_EXCEPTION_MSG,
    is_filename_only, 
    is_file_locked, 
    t_of, 
    v_of, 
    append_cause, 
    force_exception, 
    check_testcase 
)
from .p3_excel_utils import is_excel_file_open

from .p3_helper_utils import (
    ATU_DEFAULT_DURATION,
    ATU_DEFAULT_DURATION_MINUTES,
    ATU_DEFAULT_DURATION_SECONDS,
    iso_date_string,
    iso_date,
    confirm_iso_date,
    validate_iso_date_string,
    now_iso_date,
    now_iso_date_string,
    iso_date_approx,
    to_int,
    to_float,
    validate_start,
    validate_stop,
    increase_time,
    decrease_time,
    calculate_duration,
    default_duration,
    default_start_time,
    default_stop_time,
    current_timestamp,
    is_object_or_none,
    is_not_object_or_none,
    is_obj_of_type,
    is_not_obj_of_type,
    is_str_or_none,
    is_not_str_or_none,
    is_non_empty_str,
    str_empty,
    str_notempty,
    str_or_none,
    str_or_default,
    is_folder_in_path,
    timestamp_str_or_default,
    stop_str_or_default,
    is_folder_in_path,
    file_uri_to_path,
    path_to_file_uri,
    get_pid,
    get_tid,
    ptid,
    ATU_CALLER_NAME,
    ATU_APP_FILE_NAME,
    ATU_CALL_MODE,
    ATU_VSCODE_DEBUG_MODE,
    ATU_VSCODE_PYTEST_MODE,
    ATU_PYTEST_DEBUG_VSCODE,
    ATU_PYTEST_MODE,
    ATU_PYTHON_SYS_PATH,
    ATU_APP_FULL_PATH,
    ATU_APP_CWD,
    at_env_info,
    is_running_in_pytest,
    start_timer,
    stop_timer
) 

# ---------------------------------------------------------------------------- +
# Exported functions and classes from p3_utils package.
# The intent is for "import p3_utils as p3u" to import all of the functions and classes
__all__ = [
    "ATU_DEFAULT_DURATION",
    "ATU_DEFAULT_DURATION_MINUTES",
    "ATU_DEFAULT_DURATION_SECONDS",
    "iso_date_string",
    "iso_date",
    "confirm_iso_date",
    "validate_iso_date_string",
    "now_iso_date",
    "now_iso_date_string",
    "iso_date_approx",
    "to_int",
    "to_float",
    "validate_start",
    "validate_stop",
    "increase_time",
    "decrease_time",
    "calculate_duration",
    "default_duration",
    "default_start_time",
    "default_stop_time",
    "current_timestamp",
    "is_object_or_none",
    "is_not_object_or_none",
    "is_obj_of_type",
    "is_not_obj_of_type",
    "is_str_or_none",
    "is_not_str_or_none",
    "is_non_empty_str",
    "str_empty",
    "str_notempty",
    "str_or_none",
    "str_or_default",
    "is_folder_in_path",
    "timestamp_str_or_default",
    "stop_str_or_default",
    "file_uri_to_path",
    "path_to_file_uri",
    "get_pid",
    "get_tid",
    "ptid",
    FORCE_EXCEPTION,
    FORCE_EXCEPTION_MSG,
    "check_testcase",
    "v_of",
    "t_of",
    "is_filename_only",
    "append_cause",
    "fpfx",
    "out_msg",
    "exc_msg",
    "exc_err_msg",
    "force_exception",
    "is_file_locked",
    "get_print_output",
    "po",
    "set_print_output",
    "is_excel_file_open",
    "ATU_CALLER_NAME",
    "ATU_APP_FILE_NAME",
    "ATU_CALL_MODE",
    "ATU_VSCODE_DEBUG_MODE",
    "ATU_VSCODE_PYTEST_MODE",
    "ATU_PYTEST_DEBUG_VSCODE",
    "ATU_PYTEST_MODE",
    "ATU_PYTHON_SYS_PATH",
    "ATU_APP_FULL_PATH",
    "ATU_APP_CWD",
    "at_env_info",
    "is_running_in_pytest",
    "start_timer",
    "stop_timer",
]