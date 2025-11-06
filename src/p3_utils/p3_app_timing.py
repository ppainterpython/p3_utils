# ---------------------------------------------------------------------------- +
#region p3_app_timing.py
"""
Helper functions for timing application run time.
"""
#endregion p3_app_timing.py
# ---------------------------------------------------------------------------- +
#region Imports
# ---------------------------------------------------------------------------- +
# python standard library modules and packages
import time

# third-party modules and packages

# local modules and packages
#endregion Imports
# ---------------------------------------------------------------------------- +
#region Globals and Constants
APP_START_TIME: float = time.time()
#endregion Globals and Constants
# ---------------------------------------------------------------------------- +
#region timer functions
def start_timer() -> float:
    """p3_utils: Start a timer and return the raw time as a float."""
    return time.time()
def elapsed_timer(start_time: float) -> float:
    """p3_utils: Return elapsed time in float seconds from provided start_time."""
    if not isinstance(start_time, (int, float)):
        t = type(start_time).__name__
        raise TypeError(f"start_time must be type:int|float, not type: {t}")
    return time.time() - float(start_time)
def elapsed_timer_str(start_time: float) -> str:
    """p3_utils: Return elapsed time in float seconds from provided start_time."""
    if not isinstance(start_time, (int, float)):
        t = type(start_time).__name__
        raise TypeError(f"start_time must be type:int|float, not type: {t}")
    return f"{elapsed_timer(start_time):6f} seconds"
def stop_timer(start_time: float) -> str:
    """p3_utils: Return elapsed time str in seconds from provided start_time."""
    return elapsed_timer_str(start_time)
#endregion timer functions
# ---------------------------------------------------------------------------- +
