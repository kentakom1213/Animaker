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

s = t.shape

f1 = [
    "scatter",
    (
        lambda i: (rand(*s)-0.5) * 6,
        lambda i: (rand(*s)-0.5) * 6,
    ),
]

name = download_dir / "random_points.gif"

make_animation(name, (f1,), val, xlim=xlim, ylim=ylim)
