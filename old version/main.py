import tkinter as tk
from tkinter import ttk
import subprocess
import os

class DocbildUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Docbild")
        self.master.resizable(False, False)  # Disable resizing

        # PNG to JPG Conversion Section
        self.heading_label_png = tk.Label(self.master, text="PNG to Other Formats", font=("Helvetica", 14, "bold"))
        self.heading_label_png.grid(row=0, column=0, columnspan=5, pady=10)

        self.btn_png_to_jpg = ttk.Button(self.master, text="PNG to JPG", command=self.convert_png_to_jpg, width=20)
        self.btn_png_to_jpg.grid(row=1, column=0, padx=5, pady=5)

        self.btn_png_to_pdf = ttk.Button(self.master, text="PNG to PDF", command=self.convert_png_to_pdf, width=20)
        self.btn_png_to_pdf.grid(row=1, column=1, padx=5, pady=5)

        self.btn_png_to_bmp = ttk.Button(self.master, text="PNG to BMP", command=self.convert_png_to_bmp, width=20)
        self.btn_png_to_bmp.grid(row=1, column=2, padx=5, pady=5)

        self.btn_png_to_gif = ttk.Button(self.master, text="PNG to GIF", command=self.convert_png_to_gif, width=20)
        self.btn_png_to_gif.grid(row=1, column=3, padx=5, pady=5)

        self.btn_png_to_icns = ttk.Button(self.master, text="PNG to ICNS", command=self.convert_png_to_icns, width=20)
        self.btn_png_to_icns.grid(row=1, column=4, padx=5, pady=5)

        self.btn_png_to_ico = ttk.Button(self.master, text="PNG to ICO", command=self.convert_png_to_ico, width=20)
        self.btn_png_to_ico.grid(row=2, column=0, padx=5, pady=5)

        self.btn_png_to_ps = ttk.Button(self.master, text="PNG to PS", command=self.convert_png_to_ps, width=20)
        self.btn_png_to_ps.grid(row=2, column=1, padx=5, pady=5)

        self.btn_png_to_psd = ttk.Button(self.master, text="PNG to PSD", command=self.convert_png_to_psd, width=20)
        self.btn_png_to_psd.grid(row=2, column=2, padx=5, pady=5)

        self.btn_png_to_webp = ttk.Button(self.master, text="PNG to WEBP", command=self.convert_png_to_webp, width=20)
        self.btn_png_to_webp.grid(row=2, column=3, padx=5, pady=5)

        # JPG to Other Formats Conversion Section
        self.heading_label_jpg = tk.Label(self.master, text="JPG to Other Formats", font=("Helvetica", 14, "bold"))
        self.heading_label_jpg.grid(row=3, column=0, columnspan=5, pady=10)

        self.btn_jpg_to_png = ttk.Button(self.master, text="JPG to PNG", command=self.convert_jpg_to_png, width=20)
        self.btn_jpg_to_png.grid(row=4, column=0, padx=5, pady=5)

        self.btn_jpg_to_pdf = ttk.Button(self.master, text="JPG to PDF", command=self.convert_jpg_to_pdf, width=20)
        self.btn_jpg_to_pdf.grid(row=4, column=1, padx=5, pady=5)

        self.btn_jpg_to_bmp = ttk.Button(self.master, text="JPG to BMP", command=self.convert_jpg_to_bmp, width=20)
        self.btn_jpg_to_bmp.grid(row=4, column=2, padx=5, pady=5)

        self.btn_jpg_to_gif = ttk.Button(self.master, text="JPG to GIF", command=self.convert_jpg_to_gif, width=20)
        self.btn_jpg_to_gif.grid(row=4, column=3, padx=5, pady=5)

        self.btn_jpg_to_icns = ttk.Button(self.master, text="JPG to ICNS", command=self.convert_jpg_to_icns, width=20)
        self.btn_jpg_to_icns.grid(row=4, column=4, padx=5, pady=5)

        self.btn_jpg_to_ico = ttk.Button(self.master, text="JPG to ICO", command=self.convert_jpg_to_ico, width=20)
        self.btn_jpg_to_ico.grid(row=5, column=0, padx=5, pady=5)

        self.btn_jpg_to_ps = ttk.Button(self.master, text="JPG to PS", command=self.convert_jpg_to_ps, width=20)
        self.btn_jpg_to_ps.grid(row=5, column=1, padx=5, pady=5)

        self.btn_jpg_to_psd = ttk.Button(self.master, text="JPG to PSD", command=self.convert_jpg_to_psd, width=20)
        self.btn_jpg_to_psd.grid(row=5, column=2, padx=5, pady=5)

        self.btn_jpg_to_webp = ttk.Button(self.master, text="JPG to WEBP", command=self.convert_jpg_to_webp, width=20)
        self.btn_jpg_to_webp.grid(row=5, column=3, padx=5, pady=5)

    # Define conversion functions for each format
    def convert_png_to_jpg(self):
        img_script_path = os.path.join("img", "pngtojpg.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_pdf(self):
        img_script_path = os.path.join("img", "pngtopdf.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_bmp(self):
        img_script_path = os.path.join("img", "pngtobmp.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_gif(self):
        img_script_path = os.path.join("img", "pngtogif.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_icns(self):
        img_script_path = os.path.join("img", "pngtoicns.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_ico(self):
        img_script_path = os.path.join("img", "pngtoico.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_ps(self):
        img_script_path = os.path.join("img", "pngtops.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_psd(self):
        img_script_path = os.path.join("img", "pngtopsd.py")
        subprocess.run(["python", img_script_path])

    def convert_png_to_webp(self):
        img_script_path = os.path.join("img", "pngtowebp.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_png(self):
        img_script_path = os.path.join("img", "jpgtopng.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_pdf(self):
        img_script_path = os.path.join("img", "jpgtopdf.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_bmp(self):
        img_script_path = os.path.join("img", "jpgtobmp.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_gif(self):
        img_script_path = os.path.join("img", "jpgtogif.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_icns(self):
        img_script_path = os.path.join("img", "jpgtoicns.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_ico(self):
        img_script_path = os.path.join("img", "jpgtoico.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_ps(self):
        img_script_path = os.path.join("img", "jpgtops.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_psd(self):
        img_script_path = os.path.join("img", "jpgtopsd.py")
        subprocess.run(["python", img_script_path])

    def convert_jpg_to_webp(self):
        img_script_path = os.path.join("img", "jpgtowebp.py")
        subprocess.run(["python", img_script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = DocbildUI(root)
    root.mainloop()
