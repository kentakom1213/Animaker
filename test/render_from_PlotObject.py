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


# グラフの追加
sin_curve = Plot(
    PlotType.PLOT,
)
