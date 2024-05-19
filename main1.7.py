import tkinter as tk
from tkinter import ttk
import subprocess

class DocbildUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Docbild")
        self.master.resizable(False, False)  # Disable resizing

        # Define color palette
        self.colors = {
            "primary": "#007ACC",    # Soft Blue
            "secondary": "#FF9500",  # Warm Orange
            "background": "#F5F5F5", # Light Gray
            "text": "#000000",       # Black for body text and headings
            "error": "#D32F2F",      # Vivid Red
            "success": "#388E3C",    # Bright Green
            "link": "#1E88E5",       # Medium Blue
            "disabled": "#E0E0E0",   # Light Gray for disabled elements
            "border": "#CCCCCC",     # Gray for borders
            "primary_hover": "#006BB3",  # Darker Soft Blue for primary hover
            "secondary_hover": "#E68800" # Darker Warm Orange for secondary hover
        }

        # Set the background color for the master window and add padding
        self.master.configure(bg=self.colors["background"], padx=20, pady=20)  # Add padding around the window

        # Define UI sections
        self.create_png_conversion_section()
        self.create_jpg_conversion_section()
        self.create_other_formats_section()  # Add this section
        self.create_pdf_conversion_section()
        self.create_docx_conversion_section()

        # Configure button styles
        self.configure_button_styles()

    def create_png_conversion_section(self):
        # PNG to Other Formats Section
        self.heading_label_png = tk.Label(
            self.master,
            text="PNG to Other Formats",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.heading_label_png.grid(row=0, column=0, columnspan=4, pady=10, sticky="w")  # Add padding around the label

        # Buttons for PNG to other formats conversions
        buttons = [
            ("PNG to JPG", self.convert_png_to_jpg, 1, 0),
            ("PNG to PDF", self.convert_png_to_pdf, 1, 1),
            ("PNG to BMP", self.convert_png_to_bmp, 1, 2),
            ("PNG to WebP", self.convert_png_to_webp, 1, 3),
            ("PNG to TIFF", self.convert_png_to_tiff, 2, 0),
            ("PNG to JP2", self.convert_png_to_jp2, 2, 1),
        ]
        self.create_buttons(buttons, row=1)

    def create_jpg_conversion_section(self):
        # JPG to Other Formats Conversion Section
        self.heading_label_jpg = tk.Label(
            self.master,
            text="JPG to Other Formats",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.heading_label_jpg.grid(row=3, column=0, columnspan=4, pady=10, sticky="w")  # Add padding around the label

        # Buttons for JPG to other formats conversions
        buttons = [
            ("JPG to PNG", self.convert_jpg_to_png, 4, 0),
            ("JPG to PDF", self.convert_jpg_to_pdf, 4, 1),
            ("JPG to BMP", self.convert_jpg_to_bmp, 4, 2),
            ("JPG to WebP", self.convert_jpg_to_webp, 4, 3),
            ("JPG to JP2", self.convert_jpg_to_jp2, 5, 0),
            ("JPG to TIFF", self.convert_jpg_to_tiff, 5, 1),
        ]
        self.create_buttons(buttons, row=4)

    def create_other_formats_section(self):
        # Others Format Section
        self.heading_label_other = tk.Label(
            self.master,
            text="Other Formats",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.heading_label_other.grid(row=6, column=0, columnspan=4, pady=10, sticky="w")  # Add padding around the label

        # Buttons for other formats conversions
        buttons = [
            ("CR2 to PNG", self.convert_cr2_to_png, 7, 0),
            ("NEF to PNG", self.convert_nef_to_png, 7, 1),
            ("CR2 to JPG", self.convert_cr2_to_jpg, 7, 2),
            ("NEF to JPG", self.convert_nef_to_jpg, 7, 3),
        ]
        self.create_buttons(buttons, row=7)

    def create_pdf_conversion_section(self):
        # PDF Conversion Section
        self.heading_label_pdf = tk.Label(
            self.master,
            text="PDF Conversion",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.heading_label_pdf.grid(row=8, column=0, columnspan=4, pady=10, sticky="w")  # Add padding around the label

        # Buttons for PDF to other formats conversions
        buttons = [
            ("PDF to PNG", self.convert_pdf_to_png, 9, 0),
            ("PDF to JPG", self.convert_pdf_to_jpg, 9, 1),
            ("PDF to WebP", self.convert_pdf_to_webp, 9, 2),
            ("PDF to RTF", self.convert_pdf_to_rtf, 9, 3),
            ("PDF to DOC", self.convert_pdf_to_doc, 10, 0),
            ("PDF to DOCX", self.convert_pdf_to_docx, 10, 1),
        ]
        self.create_buttons(buttons, row=9)

    def create_docx_conversion_section(self):
        # DOCX Conversion Section
        self.heading_label_docx = tk.Label(
            self.master,
            text="DOCX Conversion",
            font=("Helvetica", 14, "bold"),
            bg=self.colors["background"],
            fg=self.colors["text"]
        )
        self.heading_label_docx.grid(row=11, column=0, columnspan=4, pady=10, sticky="w")  # Add padding around the label

        # Buttons for DOCX to other formats conversions
        buttons = [
            ("DOCX to DOC", self.convert_docx_to_doc, 12, 0),
            ("DOCX to DOT", self.convert_docx_to_dot, 12, 1),
            ("DOCX to DOTX", self.convert_docx_to_dotx, 12, 2),
            ("DOCX to PDF", self.convert_docx_to_pdf, 12, 3),
        ]
        self.create_buttons(buttons, row=12)

    def create_buttons(self, buttons, row):
        # Utility method to create buttons and set padding
        for text, command, r, column in buttons:
            button = ttk.Button(
                self.master,
                text=text,
                command=command,
                width=20,
                style="TButton",
            )
            button.grid(row=r, column=column, padx=10, pady=5)

    # Configure button styles
    def configure_button_styles(self):
        style = ttk.Style(self.master)
        # Configure the primary button style
        style.configure(
            "TButton",
            background=self.colors["primary"],
            foreground=self.colors["text"],  # Set button text color to black
            borderwidth=1,
            relief="solid"
        )
        style.map(
            "TButton",
            foreground=[
                ("pressed", self.colors["text"]),  # Keep text color as black when pressed
                ("active", self.colors["text"])  # Keep text color as black when active
            ],
            background=[
                ("pressed", self.colors["primary_hover"]),
                ("active", self.colors["primary_hover"])
            ]
        )

    # Define conversion functions for each format
    def convert_png_to_jpg(self):
        self.run_conversion_script("img/pngtojpg.py")

    def convert_png_to_pdf(self):
        self.run_conversion_script("img/imagestopdf.py")

    def convert_png_to_bmp(self):
        self.run_conversion_script("img/pngtobmp.py")

    def convert_png_to_webp(self):
        self.run_conversion_script("img/pngtowebp.py")

    def convert_cr2_to_png(self):
        self.run_conversion_script("img/cr2topng.py")

    def convert_nef_to_png(self):
        self.run_conversion_script("img/neftopng.py")

    def convert_png_to_tiff(self):
        self.run_conversion_script("img/pngtotiff.py")

    def convert_png_to_jp2(self):
        self.run_conversion_script("img/pngtojp2.py")

    def convert_jpg_to_png(self):
        self.run_conversion_script("img/jpgtopng.py")

    def convert_jpg_to_pdf(self):
        self.run_conversion_script("img/imagestopdf.py")

    def convert_jpg_to_bmp(self):
        self.run_conversion_script("img/jpgtobmp.py")

    def convert_jpg_to_webp(self):
        self.run_conversion_script("img/jpgtowebp.py")

    def convert_jpg_to_jp2(self):
        self.run_conversion_script("img/jpgtojp2.py")

    def convert_cr2_to_jpg(self):
        self.run_conversion_script("img/cr2tojpg.py")

    def convert_nef_to_jpg(self):
        self.run_conversion_script("img/neftojpg.py")

    def convert_jpg_to_tiff(self):
        self.run_conversion_script("img/jpgtotiff.py")

    def convert_pdf_to_png(self):
        self.run_conversion_script("pdf/pdftopng.py")

    def convert_pdf_to_jpg(self):
        self.run_conversion_script("pdf/pdftojpg.py")

    def convert_pdf_to_webp(self):
        self.run_conversion_script("pdf/pdftowebp.py")

    def convert_pdf_to_rtf(self):
        self.run_conversion_script("pdf/pdftortf.py")

    def convert_pdf_to_doc(self):
        self.run_conversion_script("pdf/pdftodoc.py")

    def convert_pdf_to_docx(self):
        self.run_conversion_script("pdf/pdftodocx.py")

    def convert_docx_to_doc(self):
        self.run_conversion_script("docx/docxtodoc.py")

    def convert_docx_to_dot(self):
        self.run_conversion_script("docx/docxtodot.py")

    def convert_docx_to_dotx(self):
        self.run_conversion_script("docx/docxtodotx.py")

    def convert_docx_to_pdf(self):
        self.run_conversion_script("docx/docxtopdf.py")

    def run_conversion_script(self, script_path):
        # Utility method to execute a script
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = DocbildUI(root)
    root.mainloop()
