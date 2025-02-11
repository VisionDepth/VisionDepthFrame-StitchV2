# **DepthFrame-Stitch**

DepthFrame-Stitch is a GUI application for compiling a sequence of depth frames into a 3D depth video. It allows users to specify input frames, adjust resolution, select video codecs and set the frame rate 

# How to install 

## 1. Windows (Using pip)
### Step 1: Install Python
- Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/).
- Ensure "Add Python to PATH" is selected during installation.

### Step 2: Install Dependencies
- Open Command Prompt (cmd) and run:
- pip install -r requirements.txt

### Step 3: Run the Application
- python DepthFrame-Stitch_GUI.py

## 2. Conda (Windows/Linux/macOS)

### Step 1: Install Miniconda or Anaconda
- Download from conda.io.

### Step 2: Create a Conda Environment
- Open Anaconda Prompt (Windows) or Terminal (Linux/macOS) and run:
- conda create --name depthframe python=3.9 -y
- conda activate depthframe

### Step 3: Install Dependencies
- pip install -r requirements.txt

### Step 4: Run the Application
- python DepthFrame-Stitch_GUI.py


## 3. Linux (Ubuntu/Debian-based)
### Step 1: Install System Dependencies
- sudo apt update && sudo apt install python3 python3-pip python3-tk -y

### Step 2: Install Python Packages
- pip install -r requirements.txt

### Step 3: Run the Application
- python3 DepthFrame-Stitch_GUI.py

## Troubleshooting
### Missing tkinter on Linux? Run:
- sudo apt install python3-tk -y
- Python not found? Add it to your system PATH or reinstall it.
### Dependencies failing to install? Try:
- pip install --upgrade pip

---

## **How to Use the GUI**

### **1. Select Frames Folder**
- Click "Browse" to select the folder containing your depth map frames.

### **2. Choose Output File**
- Click "Save As" to specify where to save the output video (.mkv, .mp4, etc.).

### **3. Set Resolution**
- Enter the desired width and height for the output video.

### **4. Select Codec**
**Choose a video codec from the dropdown menu:**
- XVID (Good Compatibility)
- H.264 (Efficient, High Quality)
- MJPG (Motion JPEG)
- TMP4V (Standard MPEG-4)
- DIVX (Older Compatibility)
- 
### **5. Define Frame Rate**
- Set the desired frame rate (default: 24.0 FPS).

### **6. Start Processing**
Click "Start Processing" to begin compiling the video. The progress bar updates as frames are processed.

---

## **Key Features**
- ✔ Select a folder containing depth map frames.  
- ✔ Choose an output video file format.  
- ✔ Select video codec (XVID, H.264, MJPG, etc.)
- ✔ Define frame rate (FPS). 
- ✔ Optimized multi-threaded frame processing for better performance.
- ✔ Track progress with a progress bar.
---

This GUI is useful for **processing and converting grayscale depth maps** into an **animated sequence** for further analysis, visualization, or **3D rendering applications**. 🚀
