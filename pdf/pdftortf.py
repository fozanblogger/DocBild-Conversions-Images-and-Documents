import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
import PyPDF2

class PDFtoRTFConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF to RTF")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="PDF to RTF", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.btn_choose_files = ttk.Button(self.master, text="Choose PDF Files", command=self.choose_files)
        self.btn_choose_files.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.convert_files, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.btn_open_folder = ttk.Button(self.master, text="Open Output Folder", command=self.open_output_folder, state=tk.DISABLED)
        self.btn_open_folder.pack(pady=5)

        self.success_label = tk.Label(self.master, text="", fg="green", wraplength=380)  # Adjust wrap length as needed
        self.success_label.pack(pady=5)

        self.failure_label = tk.Label(self.master, text="", fg="red", wraplength=380)  # Adjust wrap length as needed
        self.failure_label.pack(pady=5)

        self.selected_files = []

    def choose_files(self):
        # Choose PDF files
        self.selected_files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_files(self):
        try:
            total_files = len(self.selected_files)
            self.progress_bar["maximum"] = total_files
            for i, pdf_file in enumerate(self.selected_files):
                # Open the PDF file
                with open(pdf_file, "rb") as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""

                    # Extract text from each page
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()

                # Determine the output file name
                pdf_basename = os.path.basename(pdf_file)
                pdf_name, pdf_ext = os.path.splitext(pdf_basename)
                output_rtf_name = f"{pdf_name}.rtf"
                output_rtf_path = os.path.join(self.output_directory, output_rtf_name)

                # Check if the output file already exists
                count = 1
                while os.path.exists(output_rtf_path):
                    output_rtf_name = f"{pdf_name} ({count}).rtf"
                    output_rtf_path = os.path.join(self.output_directory, output_rtf_name)
                    count += 1

                # Write the extracted text to the RTF file
                with open(output_rtf_path, "w", encoding="utf-8") as rtf_file:
                    rtf_file.write(text)

                self.progress_bar["value"] = i + 1

            # Display success message
            self.success_label.config(text=f"Conversion successful for {total_files} files.")
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
        self.selected_files = []
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0
        self.success_label.config(text="")
        self.failure_label.config(text="")
        self.btn_open_folder.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFtoRTFConverterUI(root)
    root.mainloop()