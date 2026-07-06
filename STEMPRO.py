import numpy as np
import cv2
import os
from math import log10, sqrt
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

# ---------- Metrics ----------
def calculate_mse(original, compressed):
    return np.mean((original - compressed) ** 2)

def calculate_psnr(mse):
    if mse == 0:
        return float('inf')
    return 20 * log10(255 / sqrt(mse))

# ---------- SVD ----------
def svd_channel(channel, k):
    U, S, VT = np.linalg.svd(channel, full_matrices=False)
    k = min(k, len(S))
    return U[:, :k] @ np.diag(S[:k]) @ VT[:k, :]

# ---------- GUI ----------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SVD Image Compression Tool")
        self.root.geometry("1300x750")

        self.filepath = None
        self.original_img = None
        self.compressed_img = None

        # Upload
        tk.Button(root, text="Upload Image", command=self.upload).pack(pady=10)

        # Mode
        self.mode = ttk.Combobox(root, values=["Grayscale", "Color"])
        self.mode.set("Color")
        self.mode.pack(pady=5)

        # Slider
        tk.Label(root, text="Adjust k value (1–100)").pack()
        self.k_slider = tk.Scale(root, from_=1, to=100, orient="horizontal")
        self.k_slider.set(50)
        self.k_slider.pack(pady=5)

        # Compress
        tk.Button(root, text="Compress Image", command=self.compress).pack(pady=10)

        # Download
        self.download_btn = tk.Button(root, text="Download Compressed Image",
                                      command=self.download, state="disabled")
        self.download_btn.pack(pady=5)

        # Titles
        frame_titles = tk.Frame(root)
        frame_titles.pack()

        tk.Label(frame_titles, text="Input Image", font=("Arial", 12, "bold")).pack(side="left", padx=250)
        tk.Label(frame_titles, text="Compressed Image", font=("Arial", 12, "bold")).pack(side="right", padx=250)

        # Image Panels
        frame_images = tk.Frame(root)
        frame_images.pack()

        self.panel1 = tk.Label(frame_images)
        self.panel1.pack(side="left", padx=20)

        self.panel2 = tk.Label(frame_images)
        self.panel2.pack(side="right", padx=20)

        # Result box
        self.result = tk.Text(root, height=15, width=100,
                              font=("Courier New", 11), wrap="none")
        self.result.pack(pady=10)

    def upload(self):
        self.filepath = filedialog.askopenfilename()
        if not self.filepath:
            return

        self.original_img = cv2.imread(self.filepath)

        img_rgb = cv2.cvtColor(self.original_img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb).resize((400, 300))
        img_tk = ImageTk.PhotoImage(img_pil)

        self.panel1.config(image=img_tk)
        self.panel1.image = img_tk

        self.result.delete(1.0, tk.END)
        self.result.insert(tk.END, "Image uploaded successfully.\n")

    def compress(self):
        if self.original_img is None:
            return

        k = self.k_slider.get()
        mode = self.mode.get()
        img = self.original_img
        orig_size = os.path.getsize(self.filepath)

        # Grayscale
        if mode == "Grayscale":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            comp = svd_channel(gray, k)

        # Color
        else:
            B, G, R = cv2.split(img)
            Bc = svd_channel(B, k)
            Gc = svd_channel(G, k)
            Rc = svd_channel(R, k)
            comp = cv2.merge([Bc, Gc, Rc])

        comp = np.clip(comp, 0, 255).astype(np.uint8)
        self.compressed_img = comp

        cv2.imwrite("compressed.jpg", comp)
        comp_size = os.path.getsize("compressed.jpg")

        # Metrics
        orig_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        comp_gray = cv2.cvtColor(comp, cv2.COLOR_BGR2GRAY) if len(comp.shape) == 3 else comp

        mse = calculate_mse(orig_gray, comp_gray)
        psnr = calculate_psnr(mse)
        ratio = orig_size / comp_size

        # Show compressed image
        comp_rgb = cv2.cvtColor(comp, cv2.COLOR_BGR2RGB) if len(comp.shape) == 3 else comp
        comp_pil = Image.fromarray(comp_rgb).resize((400, 300))
        comp_tk = ImageTk.PhotoImage(comp_pil)

        self.panel2.config(image=comp_tk)
        self.panel2.image = comp_tk

        # Enable download
        self.download_btn.config(state="normal")

        w, h = comp_pil.size

        # Output
        self.result.delete(1.0, tk.END)
        self.result.insert(tk.END,
"------------------------------\n"
"   IMAGE COMPRESSION RESULT\n"
"------------------------------\n\n"

"--- Image Resolution ---\n"
f"{'Width':<15}: {w} pixels\n"
f"{'Height':<15}: {h} pixels\n"
f"{'Total Pixels':<15}: {w*h}\n\n"

f"Converted To      : {mode}\n\n"

"--- Selected k value ---\n"
f"{k}\n\n"

"--- Quality Metrics ---\n"
f"{'MSE':<15}: {mse:.4f}\n"
f"{'PSNR':<15}: {psnr:.2f} dB\n\n"

"--- File Size Comparison ---\n"
f"{'Original':<15}: {orig_size} bytes | {orig_size/1024:.2f} KB | {orig_size/(1024*1024):.2f} MB\n"
f"{'Compressed':<15}: {comp_size} bytes | {comp_size/1024:.2f} KB | {comp_size/(1024*1024):.2f} MB\n\n"

f"Compression Ratio: {ratio:.2f} : 1\n"
)

    def download(self):
        if self.compressed_img is None:
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
        )

        if save_path:
            cv2.imwrite(save_path, self.compressed_img)


# ---------- RUN ----------
root = tk.Tk()
app = App(root)
root.mainloop()
