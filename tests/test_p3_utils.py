# ---------------------------------------------------------------------------- +
# test_p3_utils.py
# ---------------------------------------------------------------------------- +
#region imports
# python standard libraries
import pytest, os
from pathlib import Path

# third-party libraries
import inspect

# local libraries
import p3_utils as p3u
#endregion imports
# ---------------------------------------------------------------------------- +
#region Globals
THIS_APP_NAME = "Test_p3_utils"

#endregion Globals
# ---------------------------------------------------------------------------- +
#region Tests for is_filename_only() function
# ---------------------------------------------------------------------------- +
#region test_is_filename_only() function
def test_is_filename_only():
    # Test with a valid filename
    result = p3u.is_filename_only("test_file.txt")
    assert result is True, f"Expected True but got {result}"

    # Test with a path that has parent directories
    result = p3u.is_filename_only("/path/to/test_file.txt")
    assert result is False, f"Expected False but got {result}"

    # Test with an empty string
    with pytest.raises(TypeError) as excinfo:
        result = p3u.is_filename_only("")
    assert str(excinfo.value) == "Invalid path_str: type='str', value=''", \
     f"Expected TypeError but got {str(excinfo.value)}"

    # Test with None
    with pytest.raises(TypeError) as excinfo:   
        result = p3u.is_filename_only(None)
    assert str(excinfo.value) == "Invalid path_str: type='NoneType', value='None'", \
        f"Expected TypeError but got {str(excinfo.value)}"
#endregion test_is_filename_only() function
# ---------------------------------------------------------------------------- +
#endregion Tests for is_filename_only() function
# ---------------------------------------------------------------------------- +
#region Tests for fpfx() function
# ---------------------------------------------------------------------------- +
#region test_fpfx() function
def test_fpfx():
    # Test with a valid function
    def test_func():
        pass

    result = p3u.fpfx(test_func)
    assert result == f"{test_func.__module__}.{test_func.__name__}(): ", f"Expected {result} to be {test_func.__module__}.{test_func.__name__}(): "

    # Test with an invalid function
    result = p3u.fpfx(None)
    assert result == f"InvalidFunction(None): ", \
        f"Expected {result} to be InvalidFunction(None): "
    # Test with forced exception
    e = ZeroDivisionError("testcase: test_fpfx()")
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = p3u.fpfx(p3u.force_exception)
    exp_msg = f"testcase: Default Exception Test for func:force_exception()"
    assert exp_msg in str(excinfo.value), \
        f"Expected Exception msg to be '{exp_msg}' but got '{str(excinfo.value)}'"
#endregion test_fpfx() function
# ---------------------------------------------------------------------------- +
#endregion Tests for fpfx() function
# ---------------------------------------------------------------------------- +
#region Tests for append_cause() function
# ---------------------------------------------------------------------------- +
#region test_append_cause() function
def test_append_cause():
    # Test with a chain of valid exceptions
    depth = 4
    def recurse_exception_func(depth:int = 4, e:Exception = None):
        try:
            ee = TypeError(f"TypeError: Func-{depth}:")
            ee = ValueError(f"ValueError: Func-{depth}:") if depth % 2 else ee
            if depth == 0:
                raise ee # base level, stops recursion
            else:
                recurse_exception_func(depth - 1, ee)
        except Exception as e:
            raise ee from e # chains exceptions back up the stack
    try:
        recurse_exception_func(depth)
    except Exception as e:
        result = p3u.append_cause("test_append_cause():", e, depth)
        em = "TypeError: Func-4: >>> "
        assert em in result, f"Expected '{em}' in {result}"
        em = "ValueError: Func-3: >>> "
        assert em in result, f"Expected '{em}' in {result}"
#endregion test_append_cause() function
#endregion Tests for append_cause() function
# ---------------------------------------------------------------------------- +
#region Tests for is_file_locked() function
# ---------------------------------------------------------------------------- +
#region test_is_file_locked() function
def test_is_file_locked(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text("Temporary file content")

    # Test when the file is not locked
    result = p3u.is_file_locked(temp_file)
    assert result is False, f"Expected False but got {result}"

    # Test when the file is locked
    with open(temp_file, 'a') as locked_file:
        result = p3u.is_file_locked(temp_file)
        assert result is True, f"Expected True but got {result}"

    # Test with a non-existent file
    non_existent_file = tmp_path / "non_existent_file.txt"
    result = p3u.is_file_locked(non_existent_file)
    assert result is False, f"Expected False but got {result}"

    # Test with an invalid file path
    with pytest.raises(Exception) as excinfo:
        result = p3u.is_file_locked(None)
    assert "An unexpected error occurred" in str(excinfo.value), \
        f"Expected an exception but got {str(excinfo.value)}"
#endregion test_is_file_locked() function
# ---------------------------------------------------------------------------- +
#endregion Tests for is_file_locked() function
# ---------------------------------------------------------------------------- +
#region Tests for err_msg() function
# ---------------------------------------------------------------------------- +
#region test_err_msg() function
def test_err_msg():
    # Test with a valid function and message
    def test_func():
        pass

    # Test happy path, valid function and message
    exptd = "test_p3_utils.test_func(): 'Test error message'"
    result = p3u.err_msg(test_func, "Test error message")
    assert result == exptd, \
        f"Expected {result} to be {p3u.fpfx(test_func)} 'Test error message'"

    # Test with func as a string name, included in return msg
    exptd = "err_msg(funcy): 'Test exception message'"
    result = p3u.err_msg("funcy", "Test exception message")
    assert result == exptd, \
        f"Expected {result} to be {p3u.fpfx(test_func)} 'Test exception message'"

    # Test with an invalid function
    exptd = "err_msg(Invalid func param:'None'): 'Test error message'"
    result = p3u.err_msg(None, "Test error message")
    assert result == exptd, \
        f"Expected '{result}' to be '{exptd}'"
#endregion test_err_msg() function
# ---------------------------------------------------------------------------- +
#region test_exc_msg() function
def test_exc_msg():
    # Test with a valid function and message
    def test_func():
        raise ValueError("Test exception")

    # Test with a valid function and exception    
    result = None
    try:
        test_func()
    except ValueError as e:
        result = p3u.exc_msg(test_func, e)

    exptd = 'test_p3_utils.test_func(): ValueError(Test exception)'
    assert result == exptd, \
        f"Expected '{result}' to be '{exptd}'"

    # Test with func as a string name, included in return msg
    exptd = 'exc_msg(funcy):(Test exception)'
    try:
        test_func()
    except ValueError as e:
        result = p3u.exc_msg("funcy", e)
    assert result == exptd, \
        f"Expected {result} to be {p3u.fpfx(test_func)} 'Test exception message'"

    # Test with func=None
    try:
        test_func()
    except ValueError as e:
        result = p3u.exc_msg(None, e)
    exptd = f"exc_msg(Invalid func param:'None'):(Test exception)"
    assert result == exptd, \
        f"Expected '{result}' to be '{exptd}'"
#endregion test_exc_msg() function
# ---------------------------------------------------------------------------- +