import optparse
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from PIL import Image


#円のアニメーション

def make_animation(saveName, func, valuable=[-1,1], xlim=[-1,1], ylim=[-1,1], frame=50):
    """save gif animation of function_graph
    saveName          : str
    funcs             : list  <-  [ ( x(i), y(i), color:str ), ...]  <-  x(i) / y(i) : (0 -> i -> 49)
    variable          : list  <-  [begin, end]
    xlim              : list
    ylim              : list
    -----------------------------------------------------
    return            : None
    """

    ims = []
    
    start = valuable[0]
    v_range = valuable[1] - valuable[0]
    
    for i in range(frame):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.axis("off")
        # ax.grid("on")

        # 描画
        value = start + i*v_range/50
        im, *opt = func
        opt = (opt[0] if opt else {})
        ax.imshow(im(value), **opt)
        plt.close(fig)


        # 画像を保存
        fig.canvas.draw()
        im = np.array(fig.canvas.renderer.buffer_rgba())
        img = Image.fromarray(im)

        # 画像を追加
        ims.append(img)

        # figを削除
        del fig, ax

    ims[0].save(saveName, save_all=True, append_images=ims[1:])
