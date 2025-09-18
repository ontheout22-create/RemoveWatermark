import sys
import cv2
import numpy as np
from pathlib import Path

def remove_watermark(video_path, out_path, x=10, y=10, w=200, h=80):
    cap = cv2.VideoCapture(str(video_path))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(str(out_path), fourcc, fps, (width, height))

    mask = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if mask is None:
            mask = np.zeros(frame.shape[:2], np.uint8)
            mask[y:y+h, x:x+w] = 255
        result = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)
        out.write(result)

    cap.release()
    out.release()

if __name__ == '__main__':
    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    # default box -- this should be replaced by a UI-specified box
    remove_watermark(in_path, out_path, x=10, y=10, w=200, h=80)
