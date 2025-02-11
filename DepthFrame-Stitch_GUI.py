import cv2
import os
import numpy as np
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from concurrent.futures import ThreadPoolExecutor
import threading

# Available codecs (Fastest first)
CODECS = {
    "XVID (Good Compatibility)": "XVID",
    "H.264 (Efficient, High Quality)": "H264",
    "MJPG (Motion JPEG)": "MJPG",
    "MP4V (Standard MPEG-4)": "MP4V",
    "DIVX (Older Compatibility)": "DIVX"
}

class DepthFrameStitchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DepthFrame-Stitch - 3D Depth Video Compiler")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Variables
        self.frames_folder = tk.StringVar()
        self.output_file = tk.StringVar()
        self.width = tk.IntVar(value=640)
        self.height = tk.IntVar(value=480)
        self.fps = tk.DoubleVar(value=24.0)
        self.selected_codec = tk.StringVar(value="XVID")

        # GUI Layout
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Frames Folder:").pack(anchor="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.frames_folder, width=50).pack(padx=10, pady=2)
        tk.Button(self.root, text="Browse", command=self.select_frames_folder).pack(pady=2)

        tk.Label(self.root, text="Select Output Video File:").pack(anchor="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.output_file, width=50).pack(padx=10, pady=2)
        tk.Button(self.root, text="Save As", command=self.select_output_file).pack(pady=2)

        tk.Label(self.root, text="Resolution (Width x Height):").pack(anchor="w", padx=10, pady=5)
        frame_res = tk.Frame(self.root)
        frame_res.pack()
        tk.Entry(frame_res, textvariable=self.width, width=10).pack(side="left", padx=5)
        tk.Label(frame_res, text="x").pack(side="left")
        tk.Entry(frame_res, textvariable=self.height, width=10).pack(side="left", padx=5)

        tk.Label(self.root, text="Select Codec:").pack(anchor="w", padx=10, pady=5)
        codec_menu = ttk.Combobox(self.root, textvariable=self.selected_codec, values=list(CODECS.keys()), state="readonly")
        codec_menu.pack(padx=10, pady=2)

        tk.Label(self.root, text="Frame Rate (FPS):").pack(anchor="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.fps, width=10).pack(padx=10, pady=2)

        self.process_btn = tk.Button(self.root, text="Start Processing", command=self.start_processing)
        self.process_btn.pack(pady=10)

        self.progress = ttk.Progressbar(self.root, length=300, mode="determinate")
        self.progress.pack(pady=10)

    def select_frames_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.frames_folder.set(folder)

    def select_output_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".mkv", filetypes=[("MKV files", "*.mkv"), ("MP4 files", "*.mp4")])
        if file:
            self.output_file.set(file)

    def start_processing(self):
        if not self.frames_folder.get() or not os.path.exists(self.frames_folder.get()):
            messagebox.showerror("Error", "Please select a valid frames folder!")
            return

        if not self.output_file.get():
            messagebox.showerror("Error", "Please specify an output file!")
            return

        threading.Thread(target=self.process_video, daemon=True).start()

    def process_video(self):
        folder = self.frames_folder.get()
        frames = sorted([
            os.path.join(folder, f) for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))
        ])

        if not frames:
            messagebox.showerror("Error", "No frames found in the selected folder!")
            return

        width, height = self.width.get(), self.height.get()
        fps = self.fps.get()
        codec_str = CODECS.get(self.selected_codec.get(), "XVID")  # Default to XVID if key is missing
        codec = cv2.VideoWriter_fourcc(*codec_str)

        video = cv2.VideoWriter(self.output_file.get(), codec, fps, (width, height), isColor=False)
        self.progress["maximum"] = len(frames)
        self.progress["value"] = 0

        def process_frame(frame_path):
            frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)
            if frame is None:
                return None
            return cv2.resize(frame, (width, height), interpolation=cv2.INTER_LINEAR)

        with ThreadPoolExecutor(max_workers=4) as executor:
            for frame in executor.map(process_frame, frames):
                if frame is not None:
                    video.write(frame)
                    self.progress["value"] += 1
                    self.root.update_idletasks()

        video.release()
        messagebox.showinfo("Success", "Video processing completed!")

root = tk.Tk()
app = DepthFrameStitchGUI(root)
root.mainloop()
