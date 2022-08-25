from animaker.image_animation import make_animation
import numpy as np
from numpy import pi, e
from numpy.random import rand
import matplotlib.cm as cm

from pathlib import Path
download_dir = Path(__file__).parent

#make
t = np.arange(-3, 3, 0.01)
xlim = [0, 1000]
ylim = [0, 1000]
val = [0, 10]

X, Y = np.linspace(-10, 10, 1000), np.linspace(-10, 10, 1000)
XX, YY = np.meshgrid(X, Y)

f = [
    lambda i: np.sin((XX ** 2 + YY ** 2) * np.sin(i*pi/5 + 1e-5) * 100),
]

name = download_dir / "move_circles.gif"

make_animation(name, f, val, xlim=xlim, ylim=ylim)
