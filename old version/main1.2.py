import tkinter as tk
from tkinter import ttk
import subprocess
import os

class DocbildUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Docbild")
        self.master.resizable(False, False)  # Disable resizing

        # Initialize lists to hold buttons and their corresponding file formats
        self.buttons = []
        self.file_formats = []

        # Define all possible file format combinations
        file_format_combinations = [
            (".docx", ".doc"), (".docx", ".pdf"), (".docx", ".rtf"), (".docx", ".odt"), (".docx", ".xlsx"),
            (".docx", ".xls"), (".docx", ".ods"), (".docx", ".pptx"), (".docx", ".ppt"), (".docx", ".odp"),
            (".doc", ".docx"), (".doc", ".pdf"), (".doc", ".rtf"), (".doc", ".odt"), (".doc", ".xlsx"),
            (".doc", ".xls"), (".doc", ".ods"), (".doc", ".pptx"), (".doc", ".ppt"), (".doc", ".odp"),
            (".pdf", ".docx"), (".pdf", ".doc"), (".pdf", ".rtf"), (".pdf", ".odt"), (".pdf", ".xlsx"),
            (".pdf", ".xls"), (".pdf", ".ods"), (".pdf", ".pptx"), (".pdf", ".ppt"), (".pdf", ".odp"),
            (".rtf", ".docx"), (".rtf", ".doc"), (".rtf", ".pdf"), (".rtf", ".odt"), (".rtf", ".xlsx"),
            (".rtf", ".xls"), (".rtf", ".ods"), (".rtf", ".pptx"), (".rtf", ".ppt"), (".rtf", ".odp"),
            (".odt", ".docx"), (".odt", ".doc"), (".odt", ".pdf"), (".odt", ".rtf"), (".odt", ".xlsx"),
            (".odt", ".xls"), (".odt", ".ods"), (".odt", ".pptx"), (".odt", ".ppt"), (".odt", ".odp"),
            (".xlsx", ".docx"), (".xlsx", ".doc"), (".xlsx", ".pdf"), (".xlsx", ".rtf"), (".xlsx", ".odt"),
            (".xlsx", ".xls"), (".xlsx", ".ods"), (".xlsx", ".pptx"), (".xlsx", ".ppt"), (".xlsx", ".odp"),
            (".xls", ".docx"), (".xls", ".doc"), (".xls", ".pdf"), (".xls", ".rtf"), (".xls", ".odt"),
            (".xls", ".xlsx"), (".xls", ".ods"), (".xls", ".pptx"), (".xls", ".ppt"), (".xls", ".odp"),
            (".ods", ".docx"), (".ods", ".doc"), (".ods", ".pdf"), (".ods", ".rtf"), (".ods", ".odt"),
            (".ods", ".xlsx"), (".ods", ".xls"), (".ods", ".pptx"), (".ods", ".ppt"), (".ods", ".odp"),
            (".pptx", ".docx"), (".pptx", ".doc"), (".pptx", ".pdf"), (".pptx", ".rtf"), (".pptx", ".odt"),
            (".pptx", ".xlsx"), (".pptx", ".xls"), (".pptx", ".ods"), (".pptx", ".ppt"), (".pptx", ".odp"),
            (".ppt", ".docx"), (".ppt", ".doc"), (".ppt", ".pdf"), (".ppt", ".rtf"), (".ppt", ".odt"),
            (".ppt", ".xlsx"), (".ppt", ".xls"), (".ppt", ".ods"), (".ppt", ".pptx"), (".ppt", ".odp"),
            (".odp", ".docx"), (".odp", ".doc"), (".odp", ".pdf"), (".odp", ".rtf"), (".odp", ".odt"),
            (".odp", ".xlsx"), (".odp", ".xls"), (".odp", ".ods"), (".odp", ".pptx"), (".odp", ".ppt")
        ]

        # Create buttons for each combination
        for i, (source_format, target_format) in enumerate(file_format_combinations):
            if (i % 10) == 0:
                # Add a new heading label for every 10 buttons
                heading_label = tk.Label(self.master, text=f"{source_format[1:].upper()} to Other Formats",
                                          font=("Helvetica", 14, "bold"))
                heading_label.grid(row=i // 10 * 3, column=0, columnspan=10, pady=10)
                self.buttons.append(heading_label)

            button_text = f"{source_format} to {target_format}"
            button = ttk.Button(self.master, text=button_text, command=lambda s=source_format, t=target_format: self.convert_file(s, t), width=20)
            button.grid(row=i // 10 * 3 + 1, column=i % 10, padx=5, pady=5)
            self.buttons.append(button)
            self.file_formats.append((source_format, target_format))

    def convert_file(self, source_format, target_format):
        # Construct script path based on source and target formats
        script_name = source_format[1:] + "to" + target_format[1:] + ".py"
        img_script_path = os.path.join("img", script_name)

        # Run the conversion script
        subprocess.run(["python", img_script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = DocbildUI(root)
    root.mainloop()
