import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale


# 輝度データを0-1に正規化する関数
def normalizer(brightness: ndarray) -> ndarray:
    tmp = [minmax_scale(brightness[i]) for i in range(len(brightness))]
    return np.array(tmp)


# 正規化した輝度データを1縦にずらしながらプロットする関数
def plot_multi(brightness: ndarray, dpi=300, FPS=30) -> None:
    normalized_data = normalizer(brightness)
    plt.figure(dpi=dpi)
    for i, data in enumerate(normalized_data):
        t = np.arange(0, len(data)) / FPS
        plt.plot(t, data + i)
    plt.xlabel("Time (s)")

    plt.show()
