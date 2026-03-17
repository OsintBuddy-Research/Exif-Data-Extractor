"""
Graphical user interface for EXIF Extractor (Tkinter, threaded).
"""
import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading

from .extractor import ExifExtractor


class ExifApp:
    def __init__(self, root):
        self.extractor = ExifExtractor()
        self.root = root
        root.title("EXIF Extractor")
        root.geometry("800x500")

        btn = tk.Button(root, text="Open Image", command=self.open_file)
        btn.pack(pady=5)

        self.text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text.pack(fill=tk.BOTH, expand=True)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.tiff *.png")]
        )
        if not file_path:
            return
        # Run extraction in background to keep UI responsive
        threading.Thread(target=self.extract, args=(file_path,), daemon=True).start()

    def extract(self, path):
        try:
            data = self.extractor.extract(path)
            self.text.delete(1.0, tk.END)
            if not data:
                self.text.insert(tk.END, "No EXIF data found.")
                return
            for k, v in data.items():
                self.text.insert(tk.END, f"{k}: {v}\n")
        except Exception as e:
            self.text.insert(tk.END, f"Error: {e}")


def main():
    root = tk.Tk()
    app = ExifApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
