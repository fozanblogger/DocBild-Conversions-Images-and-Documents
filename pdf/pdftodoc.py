import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
import fitz  # PyMuPDF library
from docx import Document
from docx.shared import Inches
import io  # Import the io module

class PDFtoDOCConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF to DOC")  # Updated title
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="PDF to DOC", font=("Helvetica", 16, "bold"))  # Updated label
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose PDF Files", command=self.choose_files)
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
        # Choose multiple PDF files
        self.selected_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_files(self):
        for selected_file in self.selected_files:
            try:
                # Get the base name of the selected PDF file
                pdf_basename = os.path.basename(selected_file)
                pdf_name, _ = os.path.splitext(pdf_basename)
                doc_output_name = f"{pdf_name}.doc"

                # Check if the output file already exists
                output_file = os.path.join(self.output_directory, doc_output_name)
                if os.path.exists(output_file):
                    # If the output file exists, generate a new filename with an incremental number
                    count = 1
                    while True:
                        new_name = f"{pdf_name} ({count}).doc"
                        new_path = os.path.join(self.output_directory, new_name)
                        if not os.path.exists(new_path):
                            doc_output_name = new_name
                            break
                        count += 1

                # Convert PDF to DOC using PyMuPDF and python-docx
                doc = Document()
                pdf_document = fitz.open(selected_file)
                for page_number in range(len(pdf_document)):
                    page = pdf_document.load_page(page_number)
                    text = page.get_text()
                    doc.add_paragraph(text)

                doc.save(os.path.join(self.output_directory, doc_output_name))

                # Display success message
                success_message = f"Conversion successful: {pdf_basename} converted to {doc_output_name}."
                self.success_label.config(text=success_message)

            except Exception as e:
                # Display failure message
                error_message = f"Failed to convert {pdf_basename}: {str(e)}"
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
    app = PDFtoDOCConverterUI(root)
    root.mainloop()
