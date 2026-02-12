# Ski Lift Wait Time Estimator

A computer vision project that estimates ski lift wait times by automatically counting people using YOLOv11 segmentation.

![Screenshot with 28 people](screenshot_20251215_140903_count28.jpg)


## 📋 Overview

This project uses deep learning to analyze ski lift webcam streams in real time. The system detects and counts people inside a defined Region of Interest (ROI) and produces visualizations plus logs for statistical analysis.

**Key features:**
- People detection with YOLOv11 segmentation
- Supports multiple video sources (local files, YouTube, webcams)
- ROI-based counting with automatic scaling
- Timestamped logging (CSV)
- Live visualization with mask overlays

## 🚀 Quickstart

### Prerequisites

```bash
# Python 3.8+ required
pip install -r requirements.txt
```

### Run

1. **Open the notebook**: `Ski_Lift_Wait_Time_Estimator_(Medium).ipynb`

2. **Run cells in order**:
   - **Cell 1**: Environment setup (local/Colab)
   - **Cell 2**: Optional file upload (Colab only)
   - **Cell 3**: Run the main program

3. **Program runs for 2 minutes** and then stops

### Configuration (optional)

Adjust parameters in [src/config.py](src/config.py):

```python
MODE = "bergfex"              # Video source: "file", "live", "bergfex", "feratel"
MAX_SECONDS = 120             # Maximum runtime in seconds
CONF_THRESHOLD = 0.25         # Detection confidence (0.0-1.0)
BASE_ROI_X1, BASE_ROI_Y1 = 200, 500    # Region of Interest
BASE_ROI_X2, BASE_ROI_Y2 = 950, 900    # Adjust for other cameras
```

## 📁 Project structure

```
├── Ski_Lift_Wait_Time_Estimator_(Medium).ipynb  # Main notebook
├── src/
│   ├── config.py          # Configuration parameters
│   └── utils.py           # Utility functions (URL extraction, ROI)
├── ski_cam_logs/          # CSV logs of counts
├── screenshots/           # Auto screenshots at high counts
├── yolo11s-seg.pt         # YOLOv11 segmentation model
└── requirements.txt       # Python dependencies
```

## 🔧 How it works

### 1. Video capture
- **File**: Local video file
- **Live**: YouTube live stream (via yt-dlp)
- **Bergfex**: Bergfex webcams (static image polling or stream)
- **Feratel**: Feratel WebTV streams

### 2. ROI definition and scaling
The Region of Interest (ROI) is defined using a reference resolution (2090×1164) and automatically scaled to the actual stream resolution.

### 3. People detection
1. YOLO segmentation detects people (class 0)
2. ROI is upscaled 2.5× for better detection
3. Masks are generated and downscaled to the original size
4. Small fragments are filtered out (< 200 pixels)
5. Only people with centroids inside the ROI are counted

### 4. Counting and logging
- **Raw count**: Direct number of detected people
- **Smoothed count**: Moving average over 15 seconds
- Output: CSV with timestamp, counts, filtered detections

### 5. Visualization
- Green mask overlays for counted people
- ROI polygon as a green outline
- Live stats in the frame (people count, time, FPS)

## 📊 Output

### CSV log
Saved to `ski_cam_logs/roi_counts_TIMESTAMP.csv`:

```csv
frame_idx,epoch_time,local_time,raw_count,smoothed_count,filtered_out_count
0,1702650123.45,2024-12-15 10:02:03 CET,12,12.0,3
1,1702650124.50,2024-12-15 10:02:04 CET,14,13.0,2
```

### Screenshots
Automatically saved in `screenshots/` when:
- People count ≥ 20
- At least 10 seconds since the last screenshot

## ⚙️ Parameter tuning

Key parameters in [src/config.py](src/config.py):

| Parameter | Default | Description |
|-----------|----------|--------------|
| `CONF_THRESHOLD` | 0.25 | Confidence for detections (higher = fewer false positives) |
| `MIN_MASK_AREA` | 200 | Minimum pixel area per person mask |
| `SMOOTH_WINDOW_SEC` | 15 | Smoothing window in seconds |
| `SCALE` | 2.5 | ROI upscaling for better detection |
| `MAX_SECONDS` | 120 | Maximum runtime (2 minutes) |

**More detections:** lower `CONF_THRESHOLD` (e.g., 0.20)  
**Fewer false positives:** raise `CONF_THRESHOLD` (e.g., 0.35), raise `MIN_MASK_AREA` (e.g., 300)

