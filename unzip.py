import argparse
from zipfile import ZipFile
from asammdf import MDF
from pathlib import Path
import os

databases = {
    "CAN": [("datavis/JacobsDBC.dbc", 0)],
}

def process_files(file_list, output_directory):
    try:
        # Concatenate the MDF files
        conc = MDF.concatenate([str(f) for f in file_list], direct_timestamp_continuation=True)
        # Extract bus logging
        filter = conc.extract_bus_logging(database_files=databases)
        # Export to CSV
        csv_output_path = output_directory / "resample.csv"
        filter.export('csv', str(csv_output_path), add_units=True, single_time_base=True, raster=0.02)
        print(f"Exported CSV to: {csv_output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main(input_path):
    path = Path(input_path)

    # Check if the input is a ZIP file or a directory
    if path.suffix == '.zip':
        parent_dir = path.parent
        modified_dir_name = f"{parent_dir.name}-mf4"
        directory = parent_dir / modified_dir_name
        print(directory)
        directory.mkdir(parents=True, exist_ok=True)

        # Unzip the file
        with ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(directory)
            extracted_files = zip_ref.namelist()
        
        # Construct file paths for processing
        zip_path = directory / Path(extracted_files[0]).parent
        file_list = sorted(directory / Path(i) for i in extracted_files)
        print(zip_path)
        output_directory = directory.parent / "csv"
        print(output_directory)
        output_directory.mkdir(parents=True, exist_ok=True)

    elif path.is_dir():
        # Use existing MF4 files within the directory
        print(path)
        file_list = sorted(path.glob('*.MF4'))
        print(file_list)
        output_directory = path.parent / "csv"
        output_directory.mkdir(parents=True, exist_ok=True)

    else:
        print("The input path is neither a zip file nor a directory of .mf4 files.")
        return

    # Process files
    process_files(file_list, output_directory)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process MF4 files from a directory or a zip file.')
    parser.add_argument('--path', type=str, default='logs/24-04-24-jacobs-test-folder/00000041',
                        help='Path to the zip file or directory containing .mf4 files')
    args = parser.parse_args()
    main(args.path)
