import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
import fitz  # PyMuPDF library

class PDFtoJPGConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF to JPG")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="PDF to JPG", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose PDF File", command=self.choose_file)
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
        # Choose PDF file
        self.selected_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.selected_file:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_file(self):
        try:
            # Convert PDF to JPG images using PyMuPDF
            pdf_document = fitz.open(self.selected_file)
            for page_number in range(len(pdf_document)):
                page = pdf_document.load_page(page_number)
                image = page.get_pixmap()
                image.save(os.path.join(self.output_directory, f"page_{page_number + 1}.jpg"))

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
    app = PDFtoJPGConverterUI(root)
    root.mainloop()
