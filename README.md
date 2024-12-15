# Excel to JSON/JSONL Converter

This script allows you to convert Excel files (`.xlsx`) to JSON or JSONL formats. You can specify the desired output format and file name, or let the script generate the output file name automatically based on the input file.

## Features
- Convert Excel files to JSON format with pretty indentation.
- Convert Excel files to JSONL format, where each line is a JSON object.
- Automatic output file naming if not explicitly provided.
- Default output format is JSON.

## Requirements

Make sure you have the following Python libraries installed:

- `pandas`
- `openpyxl`

You can install these dependencies using pip:

```bash
pip install pandas openpyxl
```

## Usage

To run the script, use the following command:

```bash
python convert.py <input_file> [output_file] [--format {json,jsonl}]
```

### Detailed Explanation of Arguments
- `<input_file>` (required):
  - The path to the Excel file you want to convert. This argument is mandatory.
- `[output_file]` (optional):
  - The desired name of the output file. If omitted, the script will generate the output file name by replacing the `.xlsx` extension with `.json` or `.jsonl` based on the format.
- `[--format {json,jsonl}]` (optional):
  - Specifies the output format. Default is `json`.

### Examples of Usage

#### 1. Convert an Excel file to JSON (default format):
```bash
python convert.py data.xlsx
```
- **Input:** `data.xlsx`
- **Output:** `data.json`

#### 2. Convert an Excel file to JSONL format:
```bash
python convert.py data.xlsx --format jsonl
```
- **Input:** `data.xlsx`
- **Output:** `data.jsonl`

#### 3. Convert an Excel file to JSON and specify the output file name:
```bash
python convert.py data.xlsx custom_output.json
```
- **Input:** `data.xlsx`
- **Output:** `custom_output.json`

#### 4. Convert an Excel file to JSONL and specify the output file name:
```bash
python convert.py data.xlsx custom_output.jsonl --format jsonl
```
- **Input:** `data.xlsx`
- **Output:** `custom_output.jsonl`

## Error Handling
If an error occurs during conversion, an appropriate error message will be displayed in the terminal. Common issues include:
- Missing input file.
- Incorrect file path or unsupported file format.
- Missing required Python libraries.

## License
This project is open-source and free to use.


