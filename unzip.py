from zipfile import ZipFile
from asammdf import MDF
from pathlib import Path

databases = {
    "CAN": [("datavis/AmigaDBC.dbc", 0)],
}

# Specify the path to your .zip file
zip_file = Path('logs/24-04-08-santa-maria/24-04-08-santa-maria-20240410T163826Z-001.zip')

# Specify the directory where you want to extract the files
directory = zip_file.parent

csv_directory = directory / 'csv'

# Ensure the directories exist
directory.mkdir(parents=True, exist_ok=True)
csv_directory.mkdir(parents=True, exist_ok=True)

# Unzip the file
with ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory)
    # Get the list of extracted file names
    extracted_files = zip_ref.namelist()

print(f"Files extracted to: {directory}")

# Correctly construct file paths
file_list = sorted([directory / Path(i) for i in extracted_files])

try: 
    # Concatenate the MDF files
    conc = MDF.concatenate([str(f) for f in file_list], direct_timestamp_continuation=True)
    # Extract bus logging
    filter = conc.extract_bus_logging(database_files=databases)
    # Export to CSV
    csv_output_path = csv_directory / "resample.csv"
    filter.export('csv', str(csv_output_path), add_units=True, single_time_base=True, raster=0.02)
    print(f"Exported CSV to: {csv_output_path}")
except Exception as e:
    print(f"An error occurred: {e}")
