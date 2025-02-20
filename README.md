# 🎬 Video Watermarking Script (Python + MoviePy)

This Python script automates **video processing** by resizing videos, overlaying a transparent watermark, and saving the output without audio. It randomly selects a watermark from a folder, ensuring variation in processed videos.

---

## ✨ Features  
✔ **Batch processing** – Scans a folder and processes multiple videos at once.  
✔ **Video resizing** – Converts all videos to **720x1280 px** (portrait format).  
✔ **Random watermark selection** – Picks a random `.png` watermark from the `"watermark"` folder.  
✔ **Watermark resizing** – Ensures the watermark is **720x1280 px** to fully cover the video.  
✔ **Audio removal** – Outputs final videos **without audio**.  
✔ **Automatic folder management** – Saves processed videos in a `"ready"` folder.  

---

## 🛠 System Requirements  

- 🐍 Python **3.8+**  
- 📦 `pip` installed  
- 💻 Works on **Windows, macOS, and Linux**  

---

## 📦 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/pinnedbyme/Video-Watermarking-Script.git
