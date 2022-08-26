from enum import Enum, auto
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class PlotType(Enum):
    """
    プロットの方法を保存する
    
    PLOT    : plt.plot
    SCATTER : plt.scatter
    FILL    : plt.fill_between
    IMAGE   : plt.imshow
    """
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
    xfunc         : (float -> numpy.ndarray)
        `PlotType`が`PLOT`,`SCATTER`,`FILL`のときに定義される。
        tからx軸を生成する関数。
    yfunc         : (float -> numpy.ndarray)
        `PlotType`が`PLOT`,`SCATTER`のときに定義される。
        tからy軸を生成する関数。
    yfuncs        : list[ (float -> numpy.ndarray) ]
        `PlotType`が`FILL`のときに定義される。
        tからy軸の塗りつぶし領域の上限を生成する関数。
    imagefunc     : (float -> numpy.ndarray)
        `PlotType`が`Image`の場合に定義される。
        2次元のnumpy配列を返す。
    options       : dict
        プロット関数に渡すオプション
    """
    def __init__(self, plot_type, xfunc, yfunc, yfuncs=None, imagefunc=None, options={}):
        """
        初期値の設定
        """
        self.plot_type = plot_type
        self.xfunc = xfunc
        self.yfunc = yfunc
        self.yfuncs = yfuncs
        self.imagefunc = imagefunc
        self.options = options
    
    def render(self, ax, t):
        """
        渡されたaxオブジェクトに与えられた時点`t`での関数をプロットする

        Paramaters
        --------
        ax        : matplotlib.axes._subplots.AxesSubplot
            プロットする背景
        t         : float
            変化させるパラメータ
        """
        if self.plot_type == PlotType.PLOT:
            ax.plot(self.xfunc(t), self.yfunc(t), **self.options)
        elif self.plot_type == PlotType.SCATTER:
            ax.scatter(self.xfunc(t), self.yfunc(t), **self.options)
        elif self.plot_type == PlotType.FILL:
            y_min, y_max = self.yfuncs
            ax.fill_between(self.xfunc(t), y_min(t), y_max(t), **self.options)
        elif self.plot_type == PlotType.IMAGE:
            ax.imshow(self.imagefunc(t), **self.options)


class Animaker:
    """
    関数プロットのgifアニメーションを作成する

    Attributes
    ----------
    fig           : matplotlib.figure.Figure, default matplotlib.pyplot.figure()
        アニメーションの背景となるオブジェクト。
    xlim          : list, default [-1, 1]
        x座標の範囲。`[xmin, xmax]`で指定する。
    ylim          : list, default [-1, 1]
        y座標の範囲。`[ymin, ymax]`で指定する。
    x             : numpy.ndarray, default numpy.linspace(*xlim, 1000)
        x軸の値。
    time          : numpy.ndarray, default numpy.linspace(0, 1, 50)
        時間を表す変数、デフォルトでは0から1までを50コマに区切ったもの。
    __plots       : list[ Plot ]
        レンダリング時にプロットする関数を保存するリスト
    """
    def __init__(self, frame):
        """
        Animakerクラスの初期化を行う。

        Paramaters
        ----------
        frame     : int
            gifアニメーションを構成する画像の枚数。
        """
        self.xlim = [-1, 1]
        self.ylim = [-1, 1]
        self.x = np.linspace(*self.xlim, 1000)
        self.time = np.linspace(0, 1, frame)
        self.__plots = []
    
    def add_plot(self, plot):
        """
        x軸に対しての陽関数曲線をプロットする。

        Paramaters
        ----------
        plot      : Plot
            プロットオブジェクト
        """
        self.__plots.append(plot)

    def render(self, save_name):
        """
        アニメーションを描画し、保存する。

        Paramaters
        ----------
        save_name : str
            保存するファイル名。拡張子は`gif`を指定する必要がある。
        """

        ims = []

        for t in self.time:
            fig = plt.figure()
            ax = fig.add_subplot()
            ax.set_aspect('equal')
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            ax.grid("on")

            # 描画
            for plot in self.__plots:
                plot.render(ax, t)

                # メモリ解放
                plt.clf()
                plt.close()

            # 画像を保存
            fig.canvas.draw()
            im = np.array(fig.canvas.renderer.buffer_rgba())
            img = Image.fromarray(im)

            # 画像を追加
            ims.append(img)

            # figを削除
            del fig, ax

        ims[0].save(save_name, save_all=True, append_images=ims[1:])
