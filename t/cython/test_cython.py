import os
class test_Cython:
    """Ensure Cython is enabled, and Cython modules were compiled
    Only to be run in cython environment to ensure cython tests are actually
    testing Faust with Cython enabled"""
    def test_cython_enabled(self):
        try:
            from Cython.Build import cythonize
        except ImportError:
            USE_CYTHON = False
        else:
            USE_CYTHON = os.environ.get('USE_CYTHON', True)


        if os.environ.get('NO_CYTHON'):
            USE_CYTHON = False

        assert USE_CYTHON == True

    def test_import(self):
        from faust._cython.windows import HoppingWindow
        hopping = HoppingWindow(60, 60)
        # No assert, just check that we could import and init
        # without exception
