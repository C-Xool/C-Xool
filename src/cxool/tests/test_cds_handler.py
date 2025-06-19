import os
import sys

import pytest
import cdsapi

from cxool.cds_handler import CDSHandler
from cxool.cxool_cli import CXoolArgumentParser


"""
This test checks that the CDSHandler class in your cxool.cds_handler module correctly sets its default data storage path when no specific path is given.
"""
def test_CDS_credentials():
    c = cdsapi.Client()


def test_default_data_storage_path():
    handler = CDSHandler()
    expected_path = os.path.abspath("./_data")
    assert handler.data_storage == expected_path


def test_default_data_merging_path(monkeypatch):
    testing_args = ["-a", "grid.nc", "-b", "1983-10-25", "-c", "1983-10-27", "--data-subfolder", "merged_path"]
    monkeypatch.setattr(sys, "argv", ["cxool"] + testing_args)
    parser = CXoolArgumentParser()
    args = parser.args
    assert args.data_subfolder == "merged_path"


