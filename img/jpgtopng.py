import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import os
import subprocess

class ImageConverterUI:
    def __init__(self, master):
        self.master = master
        self.master.title("JPG to PNG")
        self.master.geometry("400x300")
        self.master.resizable(False, False)  # Disable resizing

        # Specify the relative path to the output directory
        self.output_directory = os.path.join(os.path.dirname(__file__), "..", "otp")

        self.heading_label = tk.Label(self.master, text="JPG to PNG", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        self.btn_choose_file = ttk.Button(self.master, text="Choose JPG Files", command=self.choose_files)
        self.btn_choose_file.pack(pady=5)

        self.btn_convert = ttk.Button(self.master, text="Convert", command=self.convert_images, state=tk.DISABLED)
        self.btn_convert.pack(pady=5)

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
        self.selected_files = filedialog.askopenfilenames(filetypes=[("JPG files", "*.jpg")])
        if self.selected_files:
            self.btn_convert.config(state=tk.NORMAL)

    def convert_images(self):
        total_files = len(self.selected_files)
        success_count = 0
        failure_count = 0
        for i, file_path in enumerate(self.selected_files):
            try:
                image = Image.open(file_path)
                new_file_path = os.path.join(self.output_directory, os.path.splitext(os.path.basename(file_path))[0] + ".png")
                image.save(new_file_path, "PNG")
                success_count += 1
            except Exception as e:
                failure_count += 1
            progress = (i + 1) / total_files * 100
            self.progress_bar["value"] = progress
            self.master.update_idletasks()

        success_message = f"Converted {success_count} files successfully."
        failure_message = f"Failed to convert {failure_count} files."
        self.success_label.config(text=success_message)
        self.failure_label.config(text=failure_message)
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
