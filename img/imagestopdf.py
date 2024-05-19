import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import os
from fpdf import FPDF
import subprocess

class ImageConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Image to PDF Converter")
        self.master.geometry("400x400")
        self.master.resizable(False, False)  # Disable resizing

        # Specify the relative path to the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")

        self.heading_label = tk.Label(self.master, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose Image Files", command=self.choose_files)
        self.btn_choose_file.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.convert_images, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)

        self.name_label = tk.Label(self.master, text="PDF Name:")
        self.name_label.pack(pady=5)

        self.name_entry = ttk.Entry(self.master, width=30)
        self.name_entry.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.btn_open_folder = ttk.Button(self.master, text="Open Output Folder", command=self.open_output_folder, state=tk.DISABLED)
        self.btn_open_folder.pack(pady=5)

        self.success_label = tk.Label(self.master, text="", fg="green")
        self.success_label.pack(pady=5)

        self.failure_label = tk.Label(self.master, text="", fg="red")
        self.failure_label.pack(pady=5)

        self.selected_files = []
        
                # Initialize the timer
        self.timer_count = 0
        self.timer_running = False
        self.timer_id = None

        # Start the timer
        self.start_timer()

    def start_timer(self):
        self.timer_running = True
        self.timer_id = self.master.after(15000, self.start_countdown)

    def start_countdown(self):
        self.timer_running = False
        self.master.after_cancel(self.timer_id)
        self.timer_count = 10
        self.update_timer()

    def update_timer(self):
        if self.timer_count > 0:
            self.master.after(1000, self.update_timer)
            self.timer_count -= 1
        else:
            self.master.destroy()



    def choose_files(self):
        self.selected_files = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg")], multiple=True)
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_images(self):
        # Create the output directory if it doesn't exist
        os.makedirs(self.output_directory, exist_ok=True)

        pdf_name = self.name_entry.get().strip()  # Get the PDF name from the entry box
        if not pdf_name:
            pdf_name = "output.pdf"  # Default PDF name if not specified
        elif not pdf_name.endswith(".pdf"):
            pdf_name += ".pdf"  # Add ".pdf" extension if not provided

        pdf_path = os.path.join(self.output_directory, pdf_name)
        pdf = FPDF()

        for file_path in self.selected_files:
            try:
                image = Image.open(file_path)
                width, height = image.size
                aspect_ratio = width / height

                # Determine page size based on image aspect ratio
                if aspect_ratio >= 1:  # Landscape orientation
                    pdf.add_page(orientation='L')
                    page_width = 297  # A4 size (in mm) is 210x297, adjust as necessary
                    page_height = page_width / aspect_ratio
                else:  # Portrait orientation
                    pdf.add_page(orientation='P')
                    page_height = 297  # A4 size (in mm) is 210x297, adjust as necessary
                    page_width = page_height * aspect_ratio

                # Calculate position to center image on the page
                x = (210 - page_width) / 2  # A4 size (in mm) is 210x297
                y = (297 - page_height) / 2

                pdf.image(file_path, x, y, page_width, page_height)  # Maintain image size in PDF
            except Exception as e:
                print(f"Failed to convert {file_path}: {e}")

        pdf.output(pdf_path)

        success_message = f"Converted {len(self.selected_files)} files successfully."
        self.success_label.config(text=success_message)
        self.btn_open_folder.config(state=tk.NORMAL)

    def open_output_folder(self):
        subprocess.Popen(f'explorer "{self.output_directory}"')
        self.reset_ui()  # Reset UI after opening the output folder

    def reset_ui(self):
        self.btn_convert.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0
        self.success_label.config(text="")
        self.failure_label.config(text="")
        self.btn_open_folder.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterUI(root)
    root.mainloop()
