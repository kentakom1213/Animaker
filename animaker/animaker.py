from enum import Enum, auto
from textwrap import fill
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class PlotType(Enum):
    PLOT = auto()
    SCATTER = auto()
    FILL = auto()
    IMAGE = auto()

class Plot:
    """
    プロット用の関数の情報を保存する。

    Attributes
    ----------
    plot_type     : PlotType
        レンダリング時に呼び出す関数
    xfunc         : (numpy.ndarray -> numpy.ndarray)
        `PlotType`が`PLOT`,`SCATTER`,`FILL`のときに定義される。
        tからx軸を生成する関数。
    yfunc         : (numpy.ndarray -> numpy.ndarray)
        `PlotType`が`PLOT`,`SCATTER`のときに定義される。
        tからy軸を生成する関数。
    yfuncs        : list[ (numpy.ndarray -> numpy.ndarray) ]
        `PlotType`が`FILL`のときに定義される。
        tからy軸の塗りつぶし領域の上限を生成する関数。
    options       : dict
        プロット関数に渡すオプション
    """
    def __init__(self, plot_type, xfunc, yfunc, yfuncs=None, options={}):
        """
        初期値の設定
        """
        self.plot_type = plot_type
        self.xfunc = xfunc
        self.yfunc = yfunc
        self.yfuncs = yfuncs
        self.options = options
    
    def render(self, ax):
        """
        渡されたaxオブジェクトにプロットする

        Paramaters
        --------
        """


class Animaker:
    """
    関数プロットのgifアニメーションを作成する

    Attributes
    ----------
    fig           : matplotlib.figure.Figure, default matplotlib.pyplot.figure()
        アニメーションの背景となるオブジェクト。
    ax            : matplotlib.axes._subplots.AxesSubplot, default self.fig.add_subplot(111)
        プロットの背景。
    xlim          : list, default [-1, 1]
        x座標の範囲。`[xmin, xmax]`で指定する。
    ylim          : list, default [-1, 1]
        y座標の範囲。`[ymin, ymax]`で指定する。
    x             : numpy.ndarray, default numpy.linspace(*xlim, 1000)
        x軸の値。
    t             : numpy.ndarray, default numpy.linspace(0, 1, 50)
        時間を表す変数、デフォルトでは0から1までを50コマに区切ったもの。
    __plots       : list[Plot]
        レンダリング時にプロットする関数を保存するリスト
    """
    def __init__(self, frame):
        """
        Animakerクラスの初期化を行う。

        Paramaters
        ----------
        frame : int
            gifアニメーションを構成する画像の枚数。
        """
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.xlim = [-1, 1]
        self.ylim = [-1, 1]
        self.x = np.linspace(*self.xlim, 1000)
        self.t = np.linspace(0, 1, frame)
    
    def add_plot(self, func, xlim):
        """
        x軸に対しての陽関数曲線をプロットする。

        Paramaters
        ----------
        func : (numpy.ndarray -> numpy.ndarray)
            時間(`self.t`)を受け取って、`ndarray`を返す関数。
            例) `lambda t: np.sin(x) * t`
        
        x : list, default self.xlim
            プロットを行うxの範囲
        """




def make_animation(saveName, funcs, valuable=[-1,1], xlim=[-1,1], ylim=[-1,1], frame=50):
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
        fig = plt.fig()
        ax = fig.add_subplot()
        ax.set_aspect('equal')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        #ax.axis("off")
        ax.grid("on")

        # 描画
        value = start + i*v_range/50
        for plot_type, xy, *opt in funcs:
            opt = (opt[0] if opt else {})
            if plot_type == "plot":
                x, y = xy
                ax.plot(x(value), y(value), **opt)
            elif plot_type == "scatter":
                x, y = xy
                ax.scatter(x(value), y(value), **opt)
            elif plot_type == "image":
                ax.imshow(xy(value), **opt)
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
