import warnings


def pytest_configure():
    warnings.filterwarnings("ignore", message="numpy.ndarray size changed")
