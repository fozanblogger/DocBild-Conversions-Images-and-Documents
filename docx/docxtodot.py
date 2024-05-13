import tkinter as tk
from tkinter import filedialog, ttk
import os
from docx import Document
import subprocess
import threading

class DOCXtoDOTConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DOCX to DOT")  # Updated title
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="DOCX to DOT", font=("Helvetica", 16, "bold"))  # Updated label
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose DOCX Files", command=self.choose_files)
        self.btn_choose_file.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.convert_files, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.success_label = tk.Label(self.master, text="", fg="green", wraplength=380)  # Adjust wrap length as needed
        self.success_label.pack(pady=5)

        self.failure_label = tk.Label(self.master, text="", fg="red", wraplength=380)  # Adjust wrap length as needed
        self.failure_label.pack(pady=5)

        self.selected_files = None

    def choose_files(self):
        # Choose multiple DOCX files
        self.selected_files = filedialog.askopenfilenames(filetypes=[("Word files", "*.docx")])
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_files(self):
        # Disable the convert button to prevent multiple conversions
        self.btn_convert.config(state=tk.DISABLED)

        # Start a new thread for conversion
        conversion_thread = threading.Thread(target=self.perform_conversion)
        conversion_thread.start()

    def perform_conversion(self):
        for selected_file in self.selected_files:
            try:
                # Get the base name of the selected DOCX file
                docx_basename = os.path.basename(selected_file)
                docx_name, _ = os.path.splitext(docx_basename)
                dot_output_name = f"{docx_name}.dot"

                # Check if the output file already exists
                output_file = os.path.join(self.output_directory, dot_output_name)
                if os.path.exists(output_file):
                    # If the output file exists, generate a new filename with an incremental number
                    count = 1
                    while True:
                        new_name = f"{docx_name} ({count}).dot"
                        new_path = os.path.join(self.output_directory, new_name)
                        if not os.path.exists(new_path):
                            dot_output_name = new_name
                            break
                        count += 1

                # Convert DOCX to DOT
                docx = Document(selected_file)
                docx.save(os.path.join(self.output_directory, dot_output_name))

                # Display success message
                success_message = f"Conversion successful: {docx_basename} converted to {dot_output_name}."
                self.success_label.config(text=success_message)

            except Exception as e:
                # Display failure message
                error_message = f"Failed to convert {docx_basename}: {str(e)}"
                self.failure_label.config(text=error_message)

        # Enable open output folder button and reset UI
        self.btn_open_folder.config(state=tk.NORMAL)
        self.reset_ui()

    def reset_ui(self):
        # Reset UI components
        self.selected_files = None
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0
        self.btn_open_folder.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = DOCXtoDOTConverterUI(root)
    root.mainloop()
