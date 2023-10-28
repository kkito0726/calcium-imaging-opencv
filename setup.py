from setuptools import setup, find_packages

setup(
    name="caif",  # パッケージ名（pip listで表示される）
    version="1.0.0",  # バージョン
    description="カルシウムイメージングの動画から輝度を計測する",  # 説明
    author="kentaro kito",  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license="MIT",  # ライセンス
)
