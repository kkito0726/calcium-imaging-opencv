# calcium-imaging-opencv

カルシウムイメージングの動画の輝度解析するためのツール

## インストール

### リポジトリのクローンをする場合

任意のフォルダ階層で以下のコマンドを実行

```
$ https://github.com/kkito0726/calcium-imaging-opencv.git
```

依存ライブラリのインストール

```
$ cd calcium-imaging-opencv
$ pip install .
```

### Python ライブラリとして利用する場合

インスト-ルしたい Python 環境を activate した状態で以下のコマンドを実行

```
$ pip install git+https://github.com/kkito0726/calcium-imaging-opencv.git
```

## GUI アプリケーションの使用

### 1. アプリケーションの起動

リポジトリ内の caif フォルダに移動して main.py を実行する

```
$ cd calcium-imaging-opencv/caif
$ python main.py
```

.avi ファイルのパスを尋ねられるので入力するとそのファイルの最初のフレームが映し出される。

### 2. 使い方

左クリック: マウスポインタ地点の輝度を算出する。\
右クリック: アプリの終了\
輝度データは動画ファイルと同じ階層に CSV ファイルが生成されてそこに書き込まれる。\
初めて動画を開いたときはバックグラウンド地点の設定を行い、その地点の輝度を減算した値が CSV ファイルに書き込まれていく \
次回同じファイルを開くときは最初に指定したバックグラウンドを読み込むため、最初から輝度の算出になる。 \
CSV は x, y, 輝度データの順で列が構成されていく
