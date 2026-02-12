"""
Konfigurationsparameter für Ski Lift Wait Time Estimator
"""

# ============================================================
# MODES
# ============================================================
MODE = "bergfex"  # "file", "live", "bergfex", or "feratel"

# ============================================================
# VIDEO SOURCES
# ============================================================
# File mode
INPUT_VIDEO = "your_video.mov"

# Live mode (YouTube)
YOUTUBE_URL = "https://www.youtube.com/watch?v=wooEGQw9yrw"
COOKIES_PATH = None  # optional, for age-restricted streams

# Bergfex mode (static image polling)
BERGFEX_URL = "https://www.bergfex.at/scheffau/webcams/c114/"
BERGFEX_POLL_INTERVAL = 5  # seconds between image fetches

# Feratel WebTV mode (live stream)
FERATEL_URL = "https://webtv.feratel.com/webtv/?design=v5&pg=121E2E32-862A-4791-8936-B41853615FB6&cam=5665"
FERATEL_USE_STREAMLINK = True
FERATEL_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# ============================================================
# PREVIEW & DEBUG
# ============================================================
LIVE_PREVIEW = True
PREVIEW_EVERY = 1  # show every frame for real-time preview
DEBUG_MODE = True
DEBUG_PRINT_EVERY = 30

# ============================================================
# LOOP LIMITS
# ============================================================
MAX_FRAMES = 1200  # stop after max frames
MAX_SECONDS = 120  # stop after 2 minutes (angepasst für Prof)
FRAME_SKIP = 0  # skip frames for faster processing (0 = no skip)

# ============================================================
# DETECTION PARAMETERS
# ============================================================
CONF_THRESHOLD = 0.25  # higher = fewer false positives
IOU_THRESHOLD = 0.9  # higher = less merging of nearby detections
MIN_MASK_AREA = 200  # filter out tiny fragments
PERSON_CLASS_ONLY = True

# ============================================================
# MODEL
# ============================================================
MODEL_PATH = "yolo11s-seg.pt"  # smaller, faster model

# ============================================================
# ROI CONFIG
# ============================================================
# Reference resolution (what your ROI coords are based on)
REF_WIDTH = 2090
REF_HEIGHT = 1164

# ROI bounding box (adjust for your camera)
BASE_ROI_X1, BASE_ROI_Y1 = 200, 500
BASE_ROI_X2, BASE_ROI_Y2 = 950, 900

SCALE = 2.5  # upscale factor for better detection on small regions

# ============================================================
# LOGGING
# ============================================================
TIMEZONE = "Europe/Berlin"
LOG_DIR = "ski_cam_logs"
SMOOTH_WINDOW_SEC = 15

# ============================================================
# SCREENSHOTS
# ============================================================
SCREENSHOT_DIR = "screenshots"
SCREENSHOT_THRESHOLD = 20
SCREENSHOT_COOLDOWN = 10
