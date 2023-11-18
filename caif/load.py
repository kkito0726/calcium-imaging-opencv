import numpy as np
from numpy import ndarray
import pandas as pd

"""
解析データを読み込む関数
データフレームの各地点の最初から2行分はx, y座標を示している
それ以下は輝度データ
"""


def load_csv(path: str) -> tuple[ndarray, ndarray]:
    df = pd.read_csv(path)
    xy = df.head(2).values.T
    brightness = df[2:].values.T

    return xy, brightness
