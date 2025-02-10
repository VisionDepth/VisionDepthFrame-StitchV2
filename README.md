# **DepthFrame-Stitch**

This Python script processes a sequence of **grayscale depth map frames** stored in a specified directory and compiles them into a **video file (`.mkv` format)**.  
It leverages **OpenCV (`cv2`)** for image processing, **CuPy (`cupy`)** for GPU acceleration, and **TQDM** for progress visualization.

---

## **How to Use the Script**

### **1. Define Frame Source and Output Video**
- Specify a list of folders (`frame_folders`) that contain the grayscale depth map frames.
- Set the output video file name (default: `output_video.mkv`).

### **2. Collect and Sort Frames**
- The script scans the specified directories for image files.
- It sorts the frames to maintain the correct sequential order.
- If a directory does not exist or is empty, the script will display a warning and continue.

### **3. Determine Frame Dimensions**
- The script reads the first frame to determine its original dimensions.
- The user is prompted to either enter custom width and height values or use the original frame dimensions.

### **4. Set Up Video Writer**
- Uses OpenCV’s `VideoWriter` with the **XVID codec** to create an `.mkv` video file.
- The frame rate is set to **24 FPS** by default, but you can adjust it to match the FPS of your original video.

### **5. Process Each Frame**
- The script loops through each frame in the list.
- Reads the image in **grayscale mode**.
- Resizes the image if it does not match the specified dimensions.
- Transfers the frame to the **GPU using CuPy** for potential processing _(this is currently a placeholder for future enhancements)_.
- Converts the processed frame back to the CPU (`numpy`) and writes it to the video file.

### **6. Display Progress**
- A **TQDM progress bar** tracks and displays the frame processing progress.

### **7. Finalize and Save Video**
- Once all frames have been processed, the script releases the video writer and completes the video compilation.

---

## **Key Features**
✔ **Handles Missing Frames Gracefully** – Skips unreadable images and warns the user.  
✔ **User-Defined Resolution Support** – Allows custom width/height input.  
✔ **GPU-Accelerated Processing** – Uses **CuPy** for optimized computation _(currently a placeholder)_.  
✔ **Real-Time Progress Feedback** – Displays a progress bar for user convenience.  
✔ **Efficient Video Encoding** – Outputs a high-quality `.mkv` file using the **XVID codec**.  

---

This script is useful for **processing and converting grayscale depth maps** into an **animated sequence** for further analysis, visualization, or **3D rendering applications**. 🚀
