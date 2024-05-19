import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
from docx import Document

class DOCXtoDOTConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DOCX to DOT")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="DOCX to DOT", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose DOCX Files", command=self.choose_files)
        self.btn_choose_file.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.convert_files, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.btn_open_folder = ttk.Button(self.master, text="Open Output Folder", command=self.open_output_folder, state=tk.DISABLED)
        self.btn_open_folder.pack(pady=5)

        self.success_label = tk.Label(self.master, text="", fg="green", wraplength=380)
        self.success_label.pack(pady=5)

        self.failure_label = tk.Label(self.master, text="", fg="red", wraplength=380)
        self.failure_label.pack(pady=5)

        self.selected_files = None

    def choose_files(self):
        # Choose multiple DOCX files
        self.selected_files = filedialog.askopenfilenames(filetypes=[("Word files", "*.docx")])
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_files(self):
        conversion_successful = False
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
                doc = Document(selected_file)
                with open(os.path.join(self.output_directory, dot_output_name), "w", encoding="utf-8") as dot_file:
                    for paragraph in doc.paragraphs:
                        dot_file.write(paragraph.text + "\n")

                # Display success message
                success_message = f"Conversion successful: {docx_basename} converted to {dot_output_name}."
                self.success_label.config(text=success_message)
                conversion_successful = True

            except Exception as e:
                # Display failure message
                error_message = f"Failed to convert {docx_basename}: {str(e)}"
                self.failure_label.config(text=error_message)

        # Enable open output folder button if at least one conversion was successful
        if conversion_successful:
            self.btn_open_folder.config(state=tk.NORMAL)
        self.reset_ui()

    def open_output_folder(self):
        # Open the output folder in the file explorer
        subprocess.Popen(["explorer", self.output_directory])

    def reset_ui(self):
        # Reset UI components
        self.selected_files = None
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = DOCXtoDOTConverterUI(root)
    root.mainloop()