"""
Utility-Funktionen für Ski Lift Wait Time Estimator
"""

import requests
import re
import cv2
import numpy as np


def extract_feratel_webtv_stream_url(page_url, user_agent, use_streamlink=True):
    """
    Extract HLS stream URL from Feratel WebTV page.
    """
    try:
        headers = {"User-Agent": user_agent}
        response = requests.get(page_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        patterns = [
            r'"([^"]*\.m3u8[^"]*)"',
            r"'([^']*\.m3u8[^']*)'",
            r'"([^"]*streaming[^"]*)"',
            r'"(https?://[^"]*\.mp4[^"]*)"',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, response.text)
            if matches:
                stream_url = matches[0]
                if stream_url.startswith(('http://', 'https://', '//')):
                    if stream_url.startswith('//'):
                        stream_url = 'https:' + stream_url
                    print(f"✓ Found stream URL: {stream_url[:100]}...")
                    return stream_url
        
        if use_streamlink:
            print("✓ Trying streamlink...")
            cmd = f'streamlink "{page_url}" best -o -'
            return f"pipe://{cmd}"
        
        raise ValueError("Could not extract stream URL from Feratel page")
        
    except Exception as e:
        print(f"⚠️ Error extracting Feratel stream: {e}")
        raise


def extract_bergfex_stream_url(page_url):
    """
    Extract stream URL from bergfex webcam page.
    Returns: tuple (stream_url or None, is_video_stream: bool)
    """
    try:
        match = re.search(r'/c(\d+)/?', page_url)
        if not match:
            raise ValueError(f"Could not extract webcam ID from URL: {page_url}")
        
        webcam_id = match.group(1)
        print(f"✓ Webcam ID: {webcam_id}")
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
        
        # Try Feratel URLs
        known_feratel_cams = {"114": "5665"}
        
        if webcam_id in known_feratel_cams:
            feratel_cam_id = known_feratel_cams[webcam_id]
            feratel_url = f"https://webtv.feratel.com/webtv/?cam={feratel_cam_id}"
            print(f"✓ Trying Feratel: {feratel_url}")
            return feratel_url, True
        
        # Fallback: static image
        image_url = f"https://images.bergfex.at/webcams/?id={webcam_id}"
        print(f"✓ Using static image: {image_url}")
        return image_url, False
        
    except Exception as e:
        print(f"✗ Error: {e}")
        raise


def inside_roi(x, y, roi_polygon):
    """
    Check if point (x, y) is inside the ROI polygon.
    """
    poly = np.array(roi_polygon, np.int32)
    return cv2.pointPolygonTest(poly, (x, y), False) >= 0
