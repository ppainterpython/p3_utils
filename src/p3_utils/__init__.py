"""
p3_utils - A collection of utility functions for p3 projects.

Modules:
- p3_print_output_utils: Functions for logging and output formatting.
- p3_common_utils: General-purpose utility functions.
- p3_excel_utils: Functions for working with Excel files.
- p3_helper_utils: Helper functions for various tasks, including date handling, parameter validation, and environment info.
- p3_utils: Main module that imports and exposes all utility functions and classes.

"""
__version__ = "0.1.0"
__author__ = "Paul Painter"

from .p3_app_timing import (
    start_timer,
    stop_timer,
    elapsed_timer,
    elapsed_timer_str,
    APP_START_TIME
)
from .p3_file_helpers import (
    copy_backup,
    find_folder,
    is_file_locked,
    is_filename_only, 
    is_valid_path
) 
from .p3_print_output_utils import (
    get_print_output, 
    set_print_output, 
    po, 
    first_n,
    out_msg, 
    exc_msg, 
    exc_err_msg,
    fpfx,
    dscr,
    split_parts,
    format_tree_view
)
from .p3_common_utils import (
    FORCE_EXCEPTION,
    FORCE_EXCEPTION_MSG,
    append_cause, 
    force_exception, 
    t_of, 
    v_of, 
    has_property,
    check_testcase,
    gen_hash_key,
    gen_unique_hex_id,
    import_module_from_path
)
from .p3_excel_utils import (
    is_excel_file_open, 
    open_excel_workbooks,
    WI_NAME, WI_ABS_PATH, WI_FOLDER, WI_AUTHOR,
    WORKBOOK_INFO_COLLECTION, WORKBOOK_INFO
)

from .p3_helper_utils import (
    #region
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
    is_non_empty_dict,
    is_non_empty_str,
    is_not_non_empty_str,
    str_empty,
    str_notempty,
    str_or_none,
    str_or_default,
    is_folder_in_path,
    # basic utility functions
    # uri parsing functions
    verify_url_file_path,
    verify_file_path_for_load,
    verify_file_path_for_save,
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
    #endregion
)

# ---------------------------------------------------------------------------- +
# Exported functions and classes from p3_utils package.
# The intent is for "import p3_utils as p3u" to import all of the functions and classes
__all__ = [
    # p3_app_timing
    "start_timer",
    "stop_timer",
    "elapsed_timer",
    "elapsed_timer_str",
    "APP_START_TIME",
    # p3_file_helpers
    "copy_backup",
    "find_folder",
    "is_file_locked",
    "is_filename_only",
    "is_valid_path",
    # p3_print_output_utils
    "get_print_output",
    "set_print_output",
    "po",
    "first_n",
    "out_msg",
    "exc_msg",
    "exc_err_msg",
    "fpfx",
    "dscr",
    "split_parts",
    "format_tree_view",
    # p3_common_utils
    FORCE_EXCEPTION,
    FORCE_EXCEPTION_MSG,
    "append_cause",
    "force_exception",
    "t_of",
    "v_of",
    "has_property",
    "check_testcase",
    "gen_hash_key",
    "gen_unique_hex_id",
    "import_module_from_path",
    # p3_excel_utils
    "WI_NAME",
    "WI_ABS_PATH",
    "WI_FOLDER",
    "WI_AUTHOR",
    "WORKBOOK_INFO_COLLECTION",
    "WORKBOOK_INFO",
    "is_excel_file_open",
    "open_excel_workbooks",
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
    "is_non_empty_dict",
    "is_non_empty_str",
    "is_not_non_empty_str",
    "str_empty",
    "str_notempty",
    "str_or_none",
    "str_or_default",
    "is_folder_in_path",
    # p3_helper_utils - basic utility functions
    # p3_helper_utils - uri parsing functions
    "verify_url_file_path",
    "verify_file_path_for_load",
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
]