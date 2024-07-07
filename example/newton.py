"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。

- サインカーブを動かす
"""

import numpy as np

from animaker.animaker import Animaker, Plot, PlotType

# アニメーションの作成
anime = Animaker(50)
anime.xlim = [-2, 3]
anime.ylim = [-1, 3]
anime.time = np.linspace(0, 1, 50)

# xの範囲
x = np.linspace(*anime.xlim, 1000)

# 関数
def f(x_): return 0.5*x_**3 + 0.1*x_ + 0.5
def df(x_): return 1.5*x_**2 + 0.1


# 3次関数
curve = Plot(
    PlotType.PLOT,
    lambda t: x,
    lambda t: f(x)
)

# 接線
p = 3

def newton(t):
    global p
    p = p - f(p) / df(p)
    # x = p での接線を返す
    return df(p) * (x - p) + f(p)


line = Plot(
    PlotType.PLOT,
    lambda t: x,
    newton
)


# グラフの追加
anime.add_plot(curve)
anime.add_plot(line)

# 描画
anime.render("example/out/newton.gif", loop=0, duration=10)
