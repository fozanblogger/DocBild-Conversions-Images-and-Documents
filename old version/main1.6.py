import tkinter as tk
from tkinter import ttk
import subprocess
import os

class DocbildUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Docbild")
        self.master.resizable(False, False)  # Disable resizing

        # Define UI sections
        self.create_png_conversion_section()
        self.create_jpg_conversion_section()
        self.create_pdf_conversion_section()
        self.create_doc_conversion_section()
        self.create_docx_conversion_section()

    def create_png_conversion_section(self):
        # PNG to Other Formats Section
        self.heading_label_png = tk.Label(self.master, text="PNG to Other Formats", font=("Helvetica", 14, "bold"))
        self.heading_label_png.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons for PNG to other formats conversions
        buttons = [
            ("PNG to JPG", self.convert_png_to_jpg, 1, 0),
            ("PNG to PDF", self.convert_png_to_pdf, 1, 1),
            ("PNG to BMP", self.convert_png_to_bmp, 1, 2),
            ("PNG to WebP", self.convert_png_to_webp, 1, 3),
            ("CR2 to PNG", self.convert_cr2_to_png, 2, 0),
            ("NEF to PNG", self.convert_nef_to_png, 2, 1),
            ("PNG to TIFF", self.convert_png_to_tiff, 2, 2),
            ("PNG to JP2", self.convert_png_to_jp2, 2, 3),
        ]
        self.create_buttons(buttons)

    def create_jpg_conversion_section(self):
        # JPG to Other Formats Conversion Section
        self.heading_label_jpg = tk.Label(self.master, text="JPG to Other Formats", font=("Helvetica", 14, "bold"))
        self.heading_label_jpg.grid(row=3, column=0, columnspan=4, pady=10)

        # Buttons for JPG to other formats conversions
        buttons = [
            ("JPG to PNG", self.convert_jpg_to_png, 4, 0),
            ("JPG to PDF", self.convert_jpg_to_pdf, 4, 1),
            ("JPG to BMP", self.convert_jpg_to_bmp, 4, 2),
            ("JPG to WebP", self.convert_jpg_to_webp, 4, 3),
            ("JPG to JP2", self.convert_jpg_to_jp2, 5, 0),
            ("CR2 to JPG", self.convert_cr2_to_jpg, 5, 1),
            ("NEF to JPG", self.convert_nef_to_jpg, 5, 2),
            ("JPG to TIFF", self.convert_jpg_to_tiff, 5, 3),
        ]
        self.create_buttons(buttons)

    def create_pdf_conversion_section(self):
        # PDF Conversion Section
        self.heading_label_pdf = tk.Label(self.master, text="PDF Conversion", font=("Helvetica", 14, "bold"))
        self.heading_label_pdf.grid(row=6, column=0, columnspan=4, pady=10)

        # Buttons for PDF to other formats conversions
        buttons = [
            ("PDF to PNG", self.convert_pdf_to_png, 7, 0),
            ("PDF to JPG", self.convert_pdf_to_jpg, 7, 1),
            ("PDF to WebP", self.convert_pdf_to_webp, 7, 2),
            ("PDF to RTF", self.convert_pdf_to_rtf, 7, 3),
            ("PDF to PPTX", self.convert_pdf_to_pptx, 8, 0),
            ("PDF to XLSX", self.convert_pdf_to_xlsx, 8, 1),
            ("PDF to DOCX", self.convert_pdf_to_docx, 8, 2),
            ("PDF to DOC", self.convert_pdf_to_doc, 8, 3),
        ]
        self.create_buttons(buttons)

    def create_doc_conversion_section(self):
        # DOC Conversion Section
        self.heading_label_doc = tk.Label(self.master, text="DOC Conversion", font=("Helvetica", 14, "bold"))
        self.heading_label_doc.grid(row=9, column=0, columnspan=4, pady=10)

        # Buttons for DOC to other formats conversions
        buttons = [
            ("DOC to WebP", self.convert_doc_to_webp, 10, 0),
            ("DOC to RTF", self.convert_doc_to_rtf, 10, 1),
            ("DOC to PPTX", self.convert_doc_to_pptx, 10, 2),
            ("DOC to XLSX", self.convert_doc_to_xlsx, 10, 3),
            ("DOC to PDF", self.convert_doc_to_pdf, 11, 0),
            ("DOC to DOCX", self.convert_doc_to_docx, 11, 1),
            ("DOC to ODT", self.convert_doc_to_odt, 11, 2),
        ]
        self.create_buttons(buttons)

    def create_docx_conversion_section(self):
        # DOCX Conversion Section
        self.heading_label_docx = tk.Label(self.master, text="DOCX Conversion", font=("Helvetica", 14, "bold"))
        self.heading_label_docx.grid(row=12, column=0, columnspan=4, pady=10)

        # Buttons for DOCX to other formats conversions
        buttons = [
            ("DOCX to WebP", self.convert_docx_to_webp, 13, 0),
            ("DOCX to RTF", self.convert_docx_to_rtf, 13, 1),
            ("DOCX to PPTX", self.convert_docx_to_pptx, 13, 2),
            ("DOCX to XLSX", self.convert_docx_to_xlsx, 13, 3),
            ("DOCX to PDF", self.convert_docx_to_pdf, 14, 0),
            ("DOCX to DOC", self.convert_docx_to_doc, 14, 1),
            ("DOCX to ODT", self.convert_docx_to_odt, 14, 2),
        ]
        self.create_buttons(buttons)

    def create_buttons(self, buttons):
        # Utility method to create buttons
        for text, command, row, column in buttons:
            button = ttk.Button(self.master, text=text, command=command, width=20)
            button.grid(row=row, column=column, padx=5, pady=5)

    # Define conversion functions for each format
    def convert_png_to_jpg(self):
        self.run_conversion_script("img/pngtojpg.py")

    def convert_png_to_pdf(self):
        self.run_conversion_script("img/imagestopdf.py")

    def convert_png_to_bmp(self):
        self.run_conversion_script("img/pngtobmp.py")

    def convert_png_to_webp(self):
        self.run_conversion_script("img/pngtowebp.py")

    # Additional PNG conversions
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

    # Additional JPG conversions
    def convert_jpg_to_jp2(self):
        self.run_conversion_script("img/jpgtojp2.py")

    def convert_cr2_to_jpg(self):
        self.run_conversion_script("img/cr2tojpg.py")

    def convert_nef_to_jpg(self):
        self.run_conversion_script("img/neftojpg.py")

    def convert_jpg_to_tiff(self):
        self.run_conversion_script("img/jpgtotiff.py")

    # Define conversion functions for PDF format
    def convert_pdf_to_png(self):
        self.run_conversion_script("pdf/pdftopng.py")

    def convert_pdf_to_jpg(self):
        self.run_conversion_script("pdf/pdftojpg.py")

    def convert_pdf_to_webp(self):
        self.run_conversion_script("pdf/pdftowebp.py")

    # Additional PDF conversions
    def convert_pdf_to_rtf(self):
        self.run_conversion_script("pdf/pdftortf.py")

    def convert_pdf_to_pptx(self):
        self.run_conversion_script("pdf/pdftopptx.py")

    def convert_pdf_to_xlsx(self):
        self.run_conversion_script("pdf/pdftoxlsx.py")

    def convert_pdf_to_docx(self):
        self.run_conversion_script("pdf/pdftodocx.py")

    def convert_pdf_to_doc(self):
        self.run_conversion_script("pdf/pdftodoc.py")

    # DOC Conversion Functions

    def convert_doc_to_webp(self):
        self.run_conversion_script("doc/doctowebp.py")

    # Additional DOC conversions
    def convert_doc_to_rtf(self):
        self.run_conversion_script("doc/doctortf.py")

    def convert_doc_to_pptx(self):
        self.run_conversion_script("doc/doctopptx.py")

    def convert_doc_to_xlsx(self):
        self.run_conversion_script("doc/doctoxlsx.py")

    def convert_doc_to_pdf(self):
        self.run_conversion_script("doc/doctopdf.py")

    def convert_doc_to_docx(self):
        self.run_conversion_script("doc/doctodocx.py")

    def convert_doc_to_odt(self):
        self.run_conversion_script("doc/doctoodt.py")

    # DOCX Conversion Functions

    def convert_docx_to_webp(self):
        self.run_conversion_script("docx/docxtowebp.py")

    # Additional DOCX conversions
    def convert_docx_to_rtf(self):
        self.run_conversion_script("docx/docxtortf.py")

    def convert_docx_to_pptx(self):
        self.run_conversion_script("docx/docxtopptx.py")

    def convert_docx_to_xlsx(self):
        self.run_conversion_script("docx/docxtoxlsx.py")

    def convert_docx_to_pdf(self):
        self.run_conversion_script("docx/docxtopdf.py")

    def convert_docx_to_doc(self):
        self.run_conversion_script("docx/docxtodoc.py")

    def convert_docx_to_odt(self):
        self.run_conversion_script("docx/docxtoodt.py")

    def run_conversion_script(self, script_path):
        # Utility method to execute a script
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = DocbildUI(root)
    root.mainloop()
