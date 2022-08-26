"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。

- 歪む円のアニメーション
"""

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from animaker.animaker import PlotImage, Animaker

# アニメーションの作成
anime = Animaker(20)
anime.xlim = [0, 200]
anime.ylim = [0, 200]

# 画像の定義
X, Y = np.linspace(-100, 100, 200), np.linspace(-100, 100, 200)
XX, YY = np.meshgrid(X, Y)

# 画像を動かす関数を定義
def move_circle(t):
    cicle_t = 50 * np.sin(2 * pi * t)
    return np.sqrt(XX**2 + (YY - cicle_t)**2)

# plotオブジェクト
circle = PlotImage(move_circle)

# グラフの追加
anime.add_plot(circle)

# 描画
anime.render("example/out/move_circle_animation.gif")
