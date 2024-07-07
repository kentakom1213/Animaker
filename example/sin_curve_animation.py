"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。

- サインカーブを動かす
"""

import numpy as np

from animaker.animaker import PlotType, Plot, Animaker

# アニメーションの作成
anime = Animaker(50)
anime.xlim = [-2, 2]
anime.ylim = [-1.5, 1.5]

# xの範囲
x = np.linspace(*anime.xlim, 1000)

# グラフの定義
sin_curve = Plot(
    PlotType.PLOT,
    lambda t: x,
    lambda t: np.sin(x) * np.sin(t*2*np.pi),
)

# グラフの追加
anime.add_plot(sin_curve)

# 描画
anime.render("example/out/sin_curve_animation.gif", loop=0)
