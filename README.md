# 🎬 Video Watermarking Script (Python + MoviePy)

This Python script automates **video processing** by resizing videos, overlaying a transparent watermark, and saving the output without audio. It uses `moviepy` to efficiently handle video manipulation.

---

## ✨ Features
✅ **Batch processing** – Scans a folder and processes multiple videos at once.  
✅ **Video resizing** – Converts all videos to **720x1280 px** (portrait format).  
✅ **Random watermark selection** – Picks a random `.png` watermark from a specified folder.  
✅ **Watermark resizing** – Ensures the watermark covers the entire video **(720x1280 px)**.  
✅ **Audio removal** – Outputs final videos **without audio**.  
✅ **Automatic folder management** – Saves processed videos in a `"ready"` folder.  

---

## 🛠️ System Requirements

- Python **3.8+**
- `pip` installed
- Works on **Windows, macOS, and Linux**

### **📦 Required Python Libraries**
The script uses `moviepy` for video editing. Install dependencies using:

```bash
pip install moviepy
