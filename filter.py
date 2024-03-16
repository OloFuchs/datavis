from asammdf import MDF
import numpy as np

databases = {
    "CAN": [("logs/AmigaDBC.dbc", 0)],
}

with MDF("logs/00000001.MF4") as mdf_file:
    extracted = mdf_file.extract_bus_logging(database_files=databases)
    cut = extracted.cut(start = 20, stop = 60, whence=1)
    cut.export('csv',"csv/extracted.csv", add_units = True,)