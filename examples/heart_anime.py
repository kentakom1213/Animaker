from animaker.line_animation2 import make_animation
import numpy as np
from numpy import pi, e
from numpy.random import rand
import matplotlib.cm as cm

from pathlib import Path
download_dir = Path(__file__).parent

#make
t = np.arange(-3, 3, 0.01)
xlim = [-3, 3]
ylim = [-3, 3]
val = [0, 10]

f1 = [
    "plot",
    (
        lambda i: t,
        lambda i: np.sqrt(np.abs(t)) - np.sqrt(1 - t**2) * np.sin(i*pi/5),
    ),
    {"color": "r"}
]

f2 = [
    "plot",
    (
        lambda i: t,
        lambda i: np.sqrt(np.abs(t)) + np.sqrt(1 - t**2) * np.sin(i*pi/5)
    ),
    {"color": "r"}
]

name = download_dir / "heart.gif"

make_animation(name, (f1, f2), val, xlim=xlim, ylim=ylim)
