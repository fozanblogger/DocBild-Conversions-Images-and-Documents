import tkinter as tk
from tkinter import filedialog, ttk
import os
import subprocess
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

class DocToDotConverterUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Doc to Dot")  # Updated title
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Specify the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")
        os.makedirs(self.output_directory, exist_ok=True)  # Create output directory if it doesn't exist

        # Create widgets
        self.heading_label = tk.Label(self.master, text="Doc to Dot", font=("Helvetica", 16, "bold"))  # Updated label
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose Doc File", command=self.choose_file)
        self.btn_choose_file.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.start_conversion, state=tk.DISABLED)
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
        # Choose Doc file
        self.selected_file = filedialog.askopenfilename(filetypes=[("Doc files", "*.docx")])
        if self.selected_file:
            self.btn_convert.config(state=tk.NORMAL)

    def start_conversion(self):
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0
        self.convert_file_in_thread()

    def convert_file_in_thread(self):
        import threading
        threading.Thread(target=self.convert_file).start()

    def convert_file(self):
        try:
            # Convert Doc to Dot using python-docx and reportlab
            doc_filename = os.path.basename(self.selected_file)
            dot_output_name = doc_filename.replace(".docx", ".dot")
            dot_output_path = os.path.join(self.output_directory, dot_output_name)

            # Handle duplicate names by appending "(01)", "(02)", etc.
            file_exists = os.path.exists(dot_output_path)
            counter = 1
            while file_exists:
                dot_output_path = os.path.join(self.output_directory, f"{os.path.splitext(dot_output_name)[0]} ({counter}).dot")
                counter += 1
                file_exists= os.path.exists(dot_output_path)

            # Read the contents of the Doc file
            doc = Document(self.selected_file)

            # Create a new Dot file with the same contents
            doc_template = SimpleDocTemplate(dot_output_path, pagesize=letter)
            styles = getSampleStyleSheet()
            content = []
            for paragraph in doc.paragraphs:
                content.append(Paragraph(paragraph.text, styles["Normal"]))
            doc_template.build(content)

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
    app = DocToDotConverterUI(root)
    root.mainloop()