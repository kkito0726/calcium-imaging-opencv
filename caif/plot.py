import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
import cv2
from sklearn.preprocessing import minmax_scale
from PIL.ImageColor import getcolor
from PIL import Image
from IPython.display import display, Image


# 輝度データを0-1に正規化する関数
def normalizer(brightness: ndarray) -> ndarray:
    tmp = [minmax_scale(brightness[i]) for i in range(len(brightness))]
    return np.array(tmp)


# 正規化した輝度データを1縦にずらしながらプロットする関数
def plot_multi(brightness: ndarray, dpi=300, FPS=30) -> list[tuple[int]]:
    normalized_data = normalizer(brightness)
    colors = []
    plt.figure(dpi=dpi)
    for i, data in enumerate(normalized_data):
        t = np.arange(0, len(data)) / FPS
        c = plt.plot(t, data + i)
        # プロットした色のカラーコードを追加していく
        colors.append(c[0].get_color())
    plt.yticks(np.arange(0, len(brightness)))
    plt.xlabel("Time (s)")

    plt.show()

    # カラーコードをRGBに変換して返す
    return [getcolor(color, "RGB") for color in colors]


# 画像上に点を打つ
def point_image(img: ndarray, xy: tuple[int], color=(110, 212, 101), radius=5):
    # 白黒画像の場合カラー画像へ変換する。
    if len(img.shape) != 3:
        img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        img_color = img

    x, y = xy
    cv2.circle(img_color, (x, y), radius=radius, color=color, thickness=-1)

    return img_color


# データのプロットと計測地点を画像上に点を打つ
def point_plot_multi(
    brightness: ndarray,
    img: ndarray,
    xy: tuple[int],
    dpi=300,
    FPS=30,
    radius=5,
) -> None:
    colors = plot_multi(brightness, dpi=dpi, FPS=FPS)

    for i in range(len(colors)):
        img = point_image(img=img, xy=xy[i], color=colors[i], radius=radius)

    _, buf = cv2.imencode(".jpg", img)
    display(Image(data=buf.tobytes()))
