import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mouse import Mouse
from utils import read_video, measure_brightness


def main():
    path = input("AVIファイルのパスを入力: ")
    print("=================================")
    print("Videoデータの読み込み中です・・・")
    cap = cv2.VideoCapture(path)
    video_data = read_video(cap)
    current_frame = 0
    print("読み込み完了")
    print("=================================")

    window_name = os.path.basename(path)

    cv2.imshow(window_name, video_data[current_frame])

    mouse = Mouse(window_name, cap)

    # すでにcsvファイルが有る場合はcsvファイル内のbackgroundを参照
    csv_path = os.path.splitext(path)[0] + ".csv"
    mouse.isBackground = os.path.isfile(csv_path)
    if mouse.isBackground:
        df = pd.read_csv(csv_path)
        mouse.background = df["0"].values[2:]
        print("輝度計測したい地点をクリック")
    else:
        print("Backgroundの地点をクリック")

    while 1:
        cv2.waitKey(20)
        # csvファイルが無い場合はbackgroundの地点をクリック
        if mouse.event == cv2.EVENT_LBUTTONDOWN:
            if not mouse.isBackground:
                mouse.set_background(video_data)
                print("設定完了")
                print("=================================")
                print("輝度計測したい地点をクリック")
                continue
            else:
                mouse.measure(video_data, path)

        if mouse.event == cv2.EVENT_RBUTTONDOWN:
            print("アプリを終了します")
            break
    cv2.destroyAllWindows()
    print("=================================")


if __name__ == "__main__":
    main()
