"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。
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

cos_bar = Plot(
    PlotType.PLOT,
    lambda t: x,
    lambda t: np.zeros_like(x) + np.cos(2*np.pi * t)
)

circle = Plot(
    PlotType.SCATTER,
    lambda t: np.cos(2*np.pi * t),
    lambda t: np.sin(2*np.pi * t),
    options={"color": "r"}
)

# グラフの追加
anime.add_plot(sin_curve)
anime.add_plot(cos_bar)
anime.add_plot(circle)

# 描画
anime.render("test/move_sin.gif")
