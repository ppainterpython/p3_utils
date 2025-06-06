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
THIS_APP_NAME = "Test_p3_excel_files"
#endregion Globals
# ---------------------------------------------------------------------------- +
#region Tests for is_filename_only() function
# ---------------------------------------------------------------------------- +
#region test_open_excel_workbooks() function
def test_open_excel_workbooks():
    try:
        success, result = p3u.open_excel_workbooks() # loaded excel workbook collection
        if success:
            assert result is not None
            assert isinstance(result, dict)
            for key, value in result.items():
                assert isinstance(key, str)
                assert isinstance(value, dict)
                assert value[p3u.WI_NAME] is not None
                assert value[p3u.WI_ABS_PATH] is not None
                assert value[p3u.WI_FOLDER] is not None
                assert value[p3u.WI_AUTHOR] is not None
        else:
            pytest.fail(result)
    except Exception as e:
        pytest.fail(f"test_open_excel_workbooks() failed: {str(e)}")
#endregion test_is_excel_file_open() function
# ---------------------------------------------------------------------------- +
