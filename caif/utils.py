import cv2
import numpy as np

from pandas import DataFrame
from cv2 import VideoCapture
from numpy import ndarray


def read_video(cap: VideoCapture) -> ndarray:
    FRAMES = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    video_data = np.array([None for _ in range(int(FRAMES))])
    for i in range(int(FRAMES)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        _, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        video_data[i] = frame

    return video_data


def measure_brightness(video_data: ndarray, x: int, y: int) -> ndarray:
    FRAMES = video_data.shape[0]

    brightness = np.array([None for _ in range(FRAMES)])
    for i in range(FRAMES):
        brightness[i] = video_data[i][y][x]

    return brightness
