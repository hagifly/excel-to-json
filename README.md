# Excel to JSON/JSONL Converter

This project includes a script to convert Excel files (`.xlsx`) to JSON or JSONL formats. Additionally, a desktop application is provided for ease of use.

## Features
- Convert Excel files to JSON format with pretty indentation.
- Convert Excel files to JSONL format, where each line is a JSON object.
- Automatic output file naming if not explicitly provided.
- Default output format is JSON.
- GUI for user-friendly interaction.

## Requirements

Make sure you have the following Python libraries installed:

- `pandas`
- `openpyxl`
- `tkinter` (comes pre-installed with Python on most platforms)

You can install the necessary dependencies using pip:

```bash
pip install pandas openpyxl
```

## Usage

### Command-Line Interface

Run the script `convert.py` from the command line:

```bash
python convert.py <input_file> [output_file] [--format {json,jsonl}]
```

#### Arguments
- `<input_file>` (required):
  - The path to the Excel file you want to convert. This argument is mandatory.
- `[output_file]` (optional):
  - The desired name of the output file. If omitted, the script will generate the output file name by replacing the `.xlsx` extension with `.json` or `.jsonl` based on the format.
- `[--format {json,jsonl}]` (optional):
  - Specifies the output format. Default is `json`.

#### Examples

##### Convert an Excel file to JSON (default format):
```bash
python convert.py data.xlsx
```
- **Input:** `data.xlsx`
- **Output:** `data.json`

##### Convert an Excel file to JSONL format:
```bash
python convert.py data.xlsx --format jsonl
```
- **Input:** `data.xlsx`
- **Output:** `data.jsonl`

##### Convert an Excel file to JSON and specify the output file name:
```bash
python convert.py data.xlsx custom_output.json
```
- **Input:** `data.xlsx`
- **Output:** `custom_output.json`

### Graphical User Interface

A user-friendly GUI is available via the `app.py` script. Run it as follows:

```bash
python app.py
```

#### Features
- **Input File Selection**: Use a file dialog to select an Excel file.
- **Output File Specification**: Optionally specify the output file name using a save dialog.
- **Format Selection**: Choose between JSON and JSONL formats.
- **Conversion Execution**: Start the conversion with a single button click.

### Requirements for GUI
- Ensure `convert.py` and `app.py` are in the same directory.
- Run the GUI script using Python.

## Creating Executables

You can create standalone executables for both Windows (`.exe`) and macOS (`.app`) platforms.

### Windows: Create `.exe`
1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Create the executable:
   ```bash
   pyinstaller --onefile --windowed app.py
   ```
   - `--onefile`: Combines all dependencies into a single file.
   - `--windowed`: Hides the console window (useful for GUI apps).
3. The `.exe` file will be available in the `dist` directory.

### macOS: Create `.app`
1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Create the application bundle:
   ```bash
   pyinstaller --onefile --windowed app.py
   ```
3. The `.app` file will be available in the `dist` directory.

#### Note on macOS Distribution
If you want to distribute the `.app` file, you may need to sign and notarize it to avoid issues with macOS Gatekeeper:
- **Sign the application:**
  ```bash
  codesign --deep --force --verify --verbose --sign "Developer ID Application: Your Name (Team ID)" dist/app.app
  ```
- **Notarize the application:**
  ```bash
  xcrun altool --notarize-app --primary-bundle-id "com.example.app" --username "your_email" --password "your_password" --file dist/app.app
  ```

## Error Handling
For both CLI and GUI, appropriate error messages will be displayed for common issues, such as:
- Missing input file.
- Incorrect file path or unsupported file format.
- Missing required Python libraries.

## License
This project is open-source and free to use.


