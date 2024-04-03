from asammdf import MDF
import numpy as np

databases = {
    "CAN": [("datavis/AmigaDBC.dbc", 0)],
}

folder = "logs/strawberry_0326/"

with MDF(folder+"00000001.MF4") as mdf_file:
    extracted = mdf_file.extract_bus_logging(database_files=databases)
    # extracted = extracted.cut(start = 250, stop = 1500, whence=1)
    extracted.export('csv',folder+"csv/resample.csv",add_units = True,single_time_base = True, raster = .02)
    # extracted.export('csv',"logs/strawberry_0320/csv/extracted.csv", add_units = True,)
    