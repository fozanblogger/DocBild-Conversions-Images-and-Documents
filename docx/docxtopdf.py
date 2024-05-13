import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
from docx import Document
import io  # Import the io module
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph

class DOCXtoPDFConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DOCX to PDF")  # Updated title
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="DOCX to PDF", font=("Helvetica", 16, "bold"))  # Updated label
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose DOCX File", command=self.choose_file)
        self.btn_choose_file.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.convert_file, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.btn_open_folder = ttk.Button(self.master, text="Open Output Folder", command=self.open_output_folder, state=tk.DISABLED)
        self.btn_open_folder.pack(pady=5)

        self.success_label = tk.Label(self.master, text="", fg="green", wraplength=380)  # Adjust wrap length as needed
        self.success_label.pack(pady=5)

        self.failure_label = tk.Label(self.master, text="", fg="red", wraplength=380)  # Adjust wrap length as needed
        self.failure_label.pack(pady=5)

        self.selected_file = None

    def choose_file(self):
        # Choose DOCX file
        self.selected_file = filedialog.askopenfilename(filetypes=[("DOCX files", "*.docx")])
        if self.selected_file:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_file(self):
        try:
            # Convert DOCX to PDF using reportlab
            docx_filename = os.path.basename(self.selected_file)
            pdf_output_name = docx_filename.replace(".docx", ".pdf")
            pdf_output_path = os.path.join(self.output_directory, pdf_output_name)
            
            # Handle duplicate names by appending "(01)", "(02)", etc.
            file_exists = os.path.exists(pdf_output_path)
            counter = 1
            while file_exists:
                pdf_output_path = os.path.join(self.output_directory, f"{os.path.splitext(pdf_output_name)[0]} ({counter}).pdf")
                counter += 1
                file_exists = os.path.exists(pdf_output_path)

            doc = SimpleDocTemplate(pdf_output_path, pagesize=letter)
            styles = getSampleStyleSheet()
            content = []

            with open(self.selected_file, "rb") as docx_file:
                docx_document = Document(docx_file)
                for paragraph in docx_document.paragraphs:
                    content.append(Paragraph(paragraph.text, styles["Normal"]))

            doc.build(content)

            # Display success message
            self.success_label.config(text="Conversion successful.")
            self.btn_open_folder.config(state=tk.NORMAL)

        except Exception as e:
            # Display failure message
            error_message = f"Failed to convert: {str(e)}"
            self.failure_label.config(text=error_message)

        # Disable convert button and reset UI
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0

    def open_output_folder(self):
        # Open the output folder in the file explorer
        subprocess.Popen(["explorer", self.output_directory])
        
        # Reset UI to default state
        self.reset_ui()

    def reset_ui(self):
        # Reset UI components
        self.selected_file = None
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0
        self.success_label.config(text="")
        self.failure_label.config(text="")
        self.btn_open_folder.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = DOCXtoPDFConverterUI(root)
    root.mainloop()
