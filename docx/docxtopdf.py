import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors

class DOCXtoPDFConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DOCX to PDF")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="DOCX to PDF", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.btn_choose_files = ttk.Button(self.master, text="Choose DOCX Files", command=self.choose_files)
        self.btn_choose_files.pack(pady=5)

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

        self.selected_files = []

    def choose_files(self):
        # Choose multiple DOCX files
        self.selected_files = filedialog.askopenfilenames(filetypes=[("DOCX files", "*.docx")])
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_files(self):
        self.success_label.config(text="")
        self.failure_label.config(text="")
        self.progress_bar["value"] = 0

        successful_conversions = []
        failures = []

        for idx, selected_file in enumerate(self.selected_files):
            try:
                # Convert DOCX to PDF using reportlab
                docx_filename = os.path.basename(selected_file)
                pdf_output_name = docx_filename.replace(".docx", ".pdf")
                pdf_output_path = os.path.join(self.output_directory, pdf_output_name)

                # Handle duplicate names by appending "(1)", "(2)", etc.
                file_exists = os.path.exists(pdf_output_path)
                counter = 1
                while file_exists:
                    pdf_output_path = os.path.join(self.output_directory, f"{os.path.splitext(pdf_output_name)[0]} ({counter}).pdf")
                    counter += 1
                    file_exists = os.path.exists(pdf_output_path)

                doc = SimpleDocTemplate(pdf_output_path, pagesize=letter)
                styles = getSampleStyleSheet()
                content = []

                with open(selected_file, "rb") as docx_file:
                    docx_document = Document(docx_file)
                    for element in docx_document.element.body:
                        if element.tag.endswith('p'):
                            for paragraph in docx_document.paragraphs:
                                content.append(Paragraph(paragraph.text, styles["Normal"]))
                        elif element.tag.endswith('tbl'):
                            for table in docx_document.tables:
                                data = []
                                for row in table.rows:
                                    row_data = []
                                    for cell in row.cells:
                                        row_data.append(cell.text)
                                    data.append(row_data)
                                table_style = TableStyle([
                                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                                ])
                                pdf_table = Table(data)
                                pdf_table.setStyle(table_style)
                                content.append(pdf_table)

                doc.build(content)

                # Record successful conversion
                successful_conversions.append(docx_filename)

                # Update progress bar
                self.progress_bar["value"] = int((idx + 1) / len(self.selected_files) * 100)
                self.master.update_idletasks()

            except Exception as e:
                failures.append(f"Failed to convert {os.path.basename(selected_file)}: {str(e)}")

        if successful_conversions:
            success_message = "Successfully converted:\n" + "\n".join(successful_conversions)
            self.success_label.config(text=success_message)

        if failures:
            self.failure_label.config(text="\n".join(failures))

        # Enable open output folder button if at least one conversion was successful
        if successful_conversions:
            self.btn_open_folder.config(state=tk.NORMAL)

        self.reset_ui()

    def open_output_folder(self):
        # Open the output folder in the file explorer
        subprocess.Popen(["explorer", os.path.abspath(self.output_directory)])

    def reset_ui(self):
        # Reset UI components
        self.selected_files = []
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = DOCXtoPDFConverterUI(root)
    root.mainloop()
