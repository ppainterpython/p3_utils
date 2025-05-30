"""
p3_utils - A collection of utility functions for p3 projects.

Modules:
- p3_print_output_utils: Functions for logging and output formatting.
- p3_common_utils: General-purpose utility functions.
- p3_excel_utils: Functions for working with Excel files.

"""

__version__ = "0.1.0"
__author__ = "Paul Painter"

from .p3_print_output_utils import (
    get_print_output, 
    set_print_output, 
    po, 
    first_n,
    out_msg, 
    exc_msg, 
    exc_err_msg,
    fpfx,
    dscr
)
from .p3_common_utils import (
    FORCE_EXCEPTION,
    FORCE_EXCEPTION_MSG,
    is_filename_only, 
    append_cause, 
    force_exception, 
    t_of, 
    v_of, 
    check_testcase,
    is_file_locked
)
from .p3_excel_utils import (
    is_excel_file_open
)
from .p3_helper_utils import (
    # ISO 8601 Format helpers
    ATU_DEFAULT_DURATION,
    ATU_DEFAULT_DURATION_MINUTES,
    ATU_DEFAULT_DURATION_SECONDS,
    iso_date_string,
    iso_date_only_string,
    iso_date,
    confirm_iso_date,
    validate_iso_date_string,
    now_iso_date,
    now_iso_date_string,
    iso_date_approx,
    to_int,
    to_float,
    # Timestamp helper functions
    validate_start,
    validate_stop,
    increase_time,
    decrease_time,
    calculate_duration,
    default_duration,
    default_start_time,
    default_stop_time,
    current_timestamp,
    timestamp_str_or_default,
    stop_str_or_default,
    # Parameter validation functions
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
    # basic utility functions
    # uri parsing functions
    file_uri_to_path,
    path_to_file_uri,
    # ptid functions 
    get_pid,
    get_tid,
    ptid,
    # at_env_info functions
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
    # is_running_in_pytest,
    is_running_in_pytest,
    # Timer functions
    start_timer,
    stop_timer
) 

# ---------------------------------------------------------------------------- +
# Exported functions and classes from p3_utils package.
# The intent is for "import p3_utils as p3u" to import all of the functions and classes
__all__ = [
    # pr_print_output_utils
    "get_print_output",
    "set_print_output",
    "po",
    "first_n",
    "out_msg",
    "exc_msg",
    "exc_err_msg",
    "fpfx",
    "dscr",
    # p3_common_utils
    FORCE_EXCEPTION,
    FORCE_EXCEPTION_MSG,
    "is_filename_only",
    "append_cause",
    "force_exception",
    "t_of",
    "v_of",
    "check_testcase",
    "is_file_locked",
    # p3_excel_utils
    "is_excel_file_open",
    # p3_helper_utils - 8601 Format helpers
    "ATU_DEFAULT_DURATION",
    "ATU_DEFAULT_DURATION_MINUTES",
    "ATU_DEFAULT_DURATION_SECONDS",
    "iso_date_string",
    "iso_date_only_string",
    "iso_date",
    "confirm_iso_date",
    "validate_iso_date_string",
    "now_iso_date",
    "now_iso_date_string",
    "iso_date_approx",
    "to_int",
    "to_float",
    # p3_helper_utils - Timestamp helper functions
    "validate_start",
    "validate_stop",
    "increase_time",
    "decrease_time",
    "calculate_duration",
    "default_duration",
    "default_start_time",
    "default_stop_time",
    "current_timestamp",
    "timestamp_str_or_default",
    "stop_str_or_default",
    # p3_helper_utils - Parameter validation functions
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
    # p3_helper_utils - basic utility functions
    # p3_helper_utils - uri parsing functions
    "file_uri_to_path",
    "path_to_file_uri",
    # p3_helper_utils - ptid functions
    "get_pid",
    "get_tid",
    "ptid",
    # p3_helper_utils - at_env_info functions
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
    # p3_helper_utils - is_running_in_pytest,
    "is_running_in_pytest",
    # p3_helper_utils - Timer functions
    "start_timer",
    "stop_timer",
]