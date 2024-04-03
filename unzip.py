from zipfile import ZipFile
from asammdf import MDF
from pathlib import Path
import os

databases = {
    "CAN": [("datavis/AmigaDBC.dbc", 0)],
}

# Specify the path to your .zip file
zip_file = Path('logs/24-03-03-jacobs-cultivation/24-04-03-jacobs-cultivation-20240403T203621Z-001.zip')

# Specify the directory where you want to extract the files
# directory = Path('logs/24-03-03-jacobs-cultivation/')
directory = zip_file.parent

csv_directory = directory + 'csv/'

if not os.path.exists(directory):
    os.makedirs(directory)

if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

# Unzip the file
with ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory)

print(f"Files extracted to: {directory}")

print(zip_ref.namelist())

file_list = [f"{directory}{i}" for i in zip_ref.namelist()]

try: 
    conc = MDF.concatenate(file_list,direct_timestamp_continuation=True)
except Exception as e:
    print(f"An error occurred: {e}")

filter = conc.extract_bus_logging(database_files=databases)

filter.export('csv',directory+"csv/resample.csv",add_units = True,single_time_base = True, raster = .02)