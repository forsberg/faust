import os
import pytest

class test_Cython:
    """Test that we can import Cython modules when run with Cython enabled
    This test is here to ensure we get a clear indication if e.g. Travis
    fails to correctly install Cython and build our modules"""

    @pytest.mark.skipif(os.environ.get("NO_CYTHON"))
    def test_import(self):
        from faust._cython.windows import HoppingWindow
        hopping = HoppingWindow(60, 60)
        # No assert, just check that we could import and init
        # without exception
