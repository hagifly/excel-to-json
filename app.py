import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess


def run_conversion(input_file, output_file, format):
    try:
        # Construct the command to run convert.py
        command = ["python", "convert.py", input_file]
        if output_file:
            command.append(output_file)
        if format:
            command.extend(["--format", format])
        
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", f"Conversion completed successfully.\nOutput: {output_file or 'Generated based on input file'}")
        else:
            messagebox.showerror("Error", f"Conversion failed:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

def browse_file(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def browse_output(entry_widget):
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("JSONL files", "*.jsonl")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def start_conversion(input_entry, output_entry, format_var):
    input_file = input_entry.get()
    output_file = output_entry.get()
    format = format_var.get()

    if not input_file:
        messagebox.showwarning("Input Error", "Please select an input file.")
        return
    
    run_conversion(input_file, output_file, format)


# Create the GUI
def main():
    root = tk.Tk()
    root.title("Excel to JSON/JSONL Converter")
    
    # Input file
    tk.Label(root, text="Input Excel File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    input_entry = tk.Entry(root, width=40)
    input_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=lambda: browse_file(input_entry)).grid(row=0, column=2, padx=10, pady=10)
    
    # Output file
    tk.Label(root, text="Output File (optional):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    output_entry = tk.Entry(root, width=40)
    output_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=lambda: browse_output(output_entry)).grid(row=1, column=2, padx=10, pady=10)
    
    # Format selection
    tk.Label(root, text="Output Format:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    format_var = tk.StringVar(value="json")
    tk.Radiobutton(root, text="JSON", variable=format_var, value="json").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(root, text="JSONL", variable=format_var, value="jsonl").grid(row=2, column=1, sticky="e")
    
    # Convert button
    tk.Button(root, text="Convert", command=lambda: start_conversion(input_entry, output_entry, format_var)).grid(row=3, column=0, columnspan=3, pady=20)
    
    root.mainloop()


if __name__ == "__main__":
    main()
