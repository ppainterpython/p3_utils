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
TEST_TEXT_FILE = "./tests/testdata/testtextfile.txt"
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
    exptd = 'test_p3_utils.test_func(): '
    assert result == exptd, f"Expected '{exptd}' but got '{result}'"

    # Test with an invalid function
    result = p3u.fpfx(None)
    assert result == f"InvalidFunction(None): ", \
        f"Expected {result} to be InvalidFunction(None): "
    # Test with forced exception
    with pytest.raises(ZeroDivisionError) as excinfo:
        result = p3u.fpfx(p3u.force_exception)
    exp_msg = "division by zero"
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
#region test_is_file_locked_when_not_open() happy path
def test_is_file_locked_when_not_open():
    temp_file = Path(TEST_TEXT_FILE)
    assert temp_file.exists(), f"Temp test file isn't there? '{str(temp_file)}'"
    # Test when the file is not locked when it isn't open
    result = p3u.is_file_locked(temp_file)
    assert result is False, f"Expected False but got {result}"
#endregion test_is_file_locked() function
# ---------------------------------------------------------------------------- +
#region test_is_file_locked_when_open() function
def test_is_file_locked_when_open():
    temp_file = Path(TEST_TEXT_FILE)
    assert temp_file.exists(), f"Temp test file isn't there? '{str(temp_file)}'"
    # Test when the file is locked
    with open(temp_file, 'a') as locked_file:
        result = p3u.is_file_locked(temp_file)
        assert result is True, f"Expected True but got {result}"
#endregion test_is_file_locked_when_open() function
# ---------------------------------------------------------------------------- +
#region test_is_file_locketest_is_file_locked_when_nonexistantd() function
def test_is_file_locked_when_nonexistant():
    # Test with a non-existent file, errors = 'forgive' the default
    non_existent_file =  "tests/testdata/non_existent_file.txt"
    result = p3u.is_file_locked(non_existent_file)
    assert result is False, f"Expected False but got {result}"
#endregion test_is_file_locked_when_nonexistant() function
# ---------------------------------------------------------------------------- +
#region test_is_file_locked_with_invalid_path_type() function
def test_is_file_locked_with_invalid_path_type():
    # Test with an invalid file path type with errors = 'forgive' the default
    result = p3u.is_file_locked(None)
    assert not result, f"Expected False but got {result}"
    # Test with an invalid file path type with errors = 'strict'
    # This should raise a TypeError exception since the path is None
    exptd = "p3_utils.p3_common_utils.is_file_locked(): 'Invalid file_path: type='NoneType', value='None''"
    with pytest.raises(TypeError) as excinfo:
        result = p3u.is_file_locked(None, errors='strict')
    assert exptd == str(excinfo.value), \
        f"Expected '{exptd}' but got {str(excinfo.value)}"

    # Test with an invalid file path type with errors = 'forgive' the default
    result = p3u.is_file_locked(1234)
    assert not result, f"Expected False but got {result}"
    # This should raise a TypeError exception since the path is 123
    exptd = "p3_utils.p3_common_utils.is_file_locked(): 'Invalid file_path: type='int', value='123''"
    with pytest.raises(TypeError) as excinfo:
        result = p3u.is_file_locked(123, errors='strict')

    assert exptd == str(excinfo.value), \
        f"Expected '{exptd}' but got {str(excinfo.value)}"
#endregion test_is_file_locked_with_invalid_path_type() function
# ---------------------------------------------------------------------------- +
#endregion Tests for is_file_locked() function
# ---------------------------------------------------------------------------- +
#region Tests for out_msg() function
# ---------------------------------------------------------------------------- +
#region test_out_msg() function
def test_out_msg():
    # Test with a valid function and message
    def test_func():
        pass

    # Test happy path, valid function and message
    exptd = "test_p3_utils.test_func(): 'Test error message'"
    result = p3u.out_msg(test_func, "Test error message")
    assert result == exptd, \
        f"Expected {result} to be {p3u.fpfx(test_func)} 'Test error message'"

    # Test with func as a string name, included in return msg
    exptd = "out_msg(funcy): 'Test exception message'"
    result = p3u.out_msg("funcy", "Test exception message")
    assert result == exptd, \
        f"Expected {result} to be {p3u.fpfx(test_func)} 'Test exception message'"

    # Test with an invalid function
    exptd = "out_msg(Invalid func param:'None'): 'Test error message'"
    result = p3u.out_msg(None, "Test error message")
    assert result == exptd, \
        f"Expected '{result}' to be '{exptd}'"
#endregion test_out_msg() function
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