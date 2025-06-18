import sys

import pytest

from cxool.cxool_cli import CXoolArgumentParser

"""
This test checks that your command-line argument parser (CXoolArgumentParser) correctly interprets and stores input when given the minimum required arguments.
"""


def test_parser_minimal_arguments(monkeypatch):
    testing_args = ["-a", "grid.nc", "-b", "1983-10-25", "-c", "1983-10-27"]
    monkeypatch.setattr(sys, "argv", ["cxool"] + testing_args)
    parser = CXoolArgumentParser()
    args = parser.args
    assert args.grid_name == "grid.nc"
    assert args.initialdate == "1983-10-25"
    assert args.finaldate == "1983-10-27"
