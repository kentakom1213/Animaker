"""
`Plot`オブジェクトを直接定義し、アニメーションを作成する。
"""

import numpy as np
from numpy import pi
from animaker.line_animation2 import make_animation

# アニメーションの作成
xlim = [-2, 2]
ylim = [-1.5, 1.5]
v = [0, 2*pi]

# xの範囲
x = np.linspace(*xlim, 1000)

# グラフの定義
sin_curve = [
    "plot",
    (lambda t: x,
     lambda t: np.sin(x) * np.sin(t*2*np.pi)),
]

cos_bar = [
    "plot",
    (lambda t: x,
     lambda t: np.zeros_like(x) + np.cos(2*np.pi * t))
]

circle = [
    "scatter",
    (lambda t: np.cos(2*np.pi * t),
     lambda t: np.sin(2*np.pi * t)),
    {"color": "r"}
]

make_animation(
    "test/move_sin2.gif",
    (
        sin_curve,
        cos_bar,
        circle,
    ),
    v,
    xlim=xlim,
    ylim=ylim
)