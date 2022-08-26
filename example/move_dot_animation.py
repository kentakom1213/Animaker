"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。

- 円の媒介変数表示
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
cos_bar = Plot(
    PlotType.PLOT,
    lambda t: np.zeros_like(x) + np.cos(2*np.pi * t),
    lambda t: x,
    options={ "color": "r" }
)

sin_bar = Plot(
    PlotType.PLOT,
    lambda t: x,
    lambda t: np.zeros_like(x) + np.sin(2*np.pi * t),
    options={ "color": "b" }
)

dot = Plot(
    PlotType.SCATTER,
    lambda t: np.cos(2*np.pi * t),
    lambda t: np.sin(2*np.pi * t),
    options={"color": "black"}
)

# グラフの追加
anime.add_plot(cos_bar)
anime.add_plot(sin_bar)
anime.add_plot(dot)

# 描画
anime.render("example/out/move_dot_animation.gif")
