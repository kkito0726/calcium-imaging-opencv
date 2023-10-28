import cv2
import numpy as np
import matplotlib.pyplot as plt
from cv2 import VideoCapture
from numpy import ndarray
from utils import measure_brightness
from save import output_csv


class Mouse:
    def __init__(self, window_name: str, cap: VideoCapture):
        self.FPS = cap.get(cv2.CAP_PROP_FPS)
        self.FRAMES = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        self.event = None
        self.x = None
        self.y = None
        self.flags = None
        self.params = None

        self.background = None
        self.isBackground = False

        self.delta_f = None

        cv2.setMouseCallback(window_name, self.__Callback)

    def __Callback(self, event, x, y, flags, params):
        self.event = event
        self.x = x
        self.y = y
        self.flags = flags
        self.params = params

    def get_position(self):
        return self.x, self.y

    def set_background(self, video_data: ndarray):
        if not self.isBackground:
            self.background = measure_brightness(video_data, self.x, self.y)
            self.isBackground = True

    def measure(self, video_data: ndarray, video_path: str):
        if self.isBackground:
            brightness = measure_brightness(video_data, self.x, self.y)
            self.delta_f = brightness - self.background
            output_csv(video_path, self.delta_f, self.x, self.y)

            plt.figure(f"(x: {self.x}, y: {self.y})")
            x = np.arange(0, self.FRAMES) / self.FPS
            plt.plot(x, self.delta_f)
            plt.xlabel("Time (s)")
            plt.ylabel("ΔF/F0")
            plt.show()
