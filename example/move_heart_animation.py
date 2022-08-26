"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。

- ハートのアニメーション
"""

import numpy as np
from numpy import pi
from animaker.animaker import PlotType, Plot, Animaker

# アニメーションの作成
anime = Animaker(20)
anime.xlim = [-2, 2]
anime.ylim = [-1, 2]

# xの範囲
t = np.linspace(*anime.xlim, 1000)

# グラフの定義

heart = Plot(
    PlotType.FILL,
    lambda i: t,
    lambda i: np.sqrt(np.abs(t)) - np.sqrt(1 - t**2) * (np.sin(i*pi) / 5 + 0.6),
    lambda i: np.sqrt(np.abs(t)) + np.sqrt(1 - t**2) * (np.sin(i*pi) / 5 + 0.6),
    options={ "color": "r" }
)

# グラフの追加
anime.add_plot(heart)

# 描画
anime.render("test/out/move_heart_animation.gif")
