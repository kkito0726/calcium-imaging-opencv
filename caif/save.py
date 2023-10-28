import pandas as pd
import numpy as np
from numpy import ndarray
import os


def output_csv(video_path: str, brightness, x: int, y: int) -> None:
    csv_path = os.path.splitext(video_path)[0] + ".csv"
    data = np.append([x, y], brightness)

    if os.path.isfile(csv_path):
        df = pd.read_csv(csv_path)
    else:
        df = pd.DataFrame()
    df[df.shape[1]] = data

    df.to_csv(csv_path, index=False)
