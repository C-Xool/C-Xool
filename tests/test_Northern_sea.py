"""
Example: Minimal C-Xool run
This script shows how to run C-Xool from the command line using real options,
with a specified grid, time interval, and list of ERA5 variables.
 Authors:
     Carlos Argáez, Simon Klüpfel, María Eugenia Allenda Aranda, Christian Mario Appendini
     To report bugs, questions, critics or just greetings, please use:
         cargaezg@iingen.unam.mx
"""

import sys
import xarray as xr
import numpy as np
from cxool.cxool_cli import main


sys.argv = [
    "cxool",
    "--grid-name",
    "nordseedeu10km_grid.nc",
    "--interval=6",
    "--initialdate",
    "1993-12-31",
    "--finaldate",
    "1994-01-01",
    "--vars-to-interp",
    "msl",
    "wind",
    "--final-interpolated-file",
    "forcing_Deu_NorthernSea.nc",
]

def test_differences():
    main()
    with xr.open_dataset("reference_Deu_NS.nc") as refe:
        with xr.open_dataset("forcing_Deu_NorthernSea.nc") as forcing:
            diff = refe["Pair"] - forcing["Pair"]
            assert np.abs(diff.values).sum() <= 1e-5
            diff = refe["Pair"] - forcing["Pair"] 
            assert np.abs(diff.values).sum() <= 1e-5
            diff = refe["Pair"] - forcing["Pair"]
            assert np.abs(diff.values).sum() <= 1e-5
 


