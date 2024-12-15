import pandas as pd
import json
import argparse
import os


def xlsx_to_json(input_file, output_file):
    """
    Convert an Excel file to JSON format.
    :param input_file: Path to the input Excel file
    :param output_file: Path to the output JSON file
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_file)

        # Convert DataFrame to JSON and save to file
        df.to_json(output_file, orient="records", indent=4, force_ascii=False)
        print(f"Excel file has been successfully converted to JSON: {output_file}")
    except Exception as e:
        print(f"An error occurred while converting to JSON: {e}")


def xlsx_to_jsonl(input_file, output_file):
    """
    Convert an Excel file to JSONL format.
    :param input_file: Path to the input Excel file
    :param output_file: Path to the output JSONL file
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_file)

        # Convert DataFrame to JSONL and save to file
        with open(output_file, "w", encoding="utf-8") as f:
            for record in df.to_dict(orient="records"):
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"Excel file has been successfully converted to JSONL: {output_file}")
    except Exception as e:
        print(f"An error occurred while converting to JSONL: {e}")


def main():
    parser = argparse.ArgumentParser(description="Convert Excel files to JSON or JSONL format.")
    parser.add_argument("input_file", help="Path to the input Excel file.")
    parser.add_argument("output_file", nargs="?", help="Path to the output file. If not specified, it will be generated based on the input file.")
    parser.add_argument(
        "--format", choices=["json", "jsonl"], default="json",
        help="Specify the output format: 'json' for JSON or 'jsonl' for JSONL. Default is 'json'."
    )

    args = parser.parse_args()

    # Set default output file if not provided
    if not args.output_file:
        base, _ = os.path.splitext(args.input_file)
        args.output_file = f"{base}.{args.format}"

    if args.format == "json":
        xlsx_to_json(args.input_file, args.output_file)
    elif args.format == "jsonl":
        xlsx_to_jsonl(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
