import matplotlib 
import matplotlib.ticker as ticker
from math import sqrt
from matplotlib import rc, rcParams
from cycler import cycler
import matplotlib.pyplot as plt
import numpy as np

SPINE_COLOR="gray"
colors = ["#A51C30", "#808080",
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

def get_width_height(fig_width=None, fig_height=None, columns=1):

    assert(columns in [1,2])
    if fig_width is None:
        fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height + 
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES
    return fig_width, fig_height

def global_setting():
    params = {"lines.linewidth": 1.0,
      "axes.edgecolor": "black",
      "patch.linewidth": 0.5,
      "legend.fancybox": True,
     'axes.prop_cycle':cycler('color', colors),
      "axes.facecolor": "white",
      "axes.labelsize": "large",
      "axes.grid": False,
      "patch.edgecolor": "black",
      "axes.titlesize": "small",
      'xtick.labelsize': "x-small",
      'ytick.labelsize': "x-small",
      "text.usetex":True,
      'font.family': 'serif',
        "font.serif": [],
      "figure.dpi": 300,
        'font.size': 10
    }
    rcParams.update(params)

def format_axes(ax):

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
        

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)
    
    
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)
    return ax

def figure(fig_width=None, fig_height=None,  *args, **kwargs):
    """
    Returns a figure with an appropriate size and tight layout.
    """
    fig_width, fig_height = get_width_height(fig_width, fig_height, columns=1)
    fig = plt.figure(figsize=(fig_width, fig_height), *args, **kwargs)
    return fig

def subplots(fig_width=None, fig_height=None, *args, **kwargs):
    """
    Returns subplots with an appropriate figure size and tight layout.
    """
    fig_width, fig_height = get_width_height(fig_width, fig_height, columns=2)
    fig, axes = plt.subplots(figsize=(fig_width, fig_height), *args, **kwargs)
    return fig, axes

def legend(ax, ncol=3, loc=9, pos=(0.5, -0.1)):
    leg=ax.legend(loc=loc, bbox_to_anchor=pos, ncol=ncol)
    return leg

def savefig(filename, leg, *args, **kwargs):
    """
    Save in PDF file with the given filename.
    """
    art=[leg]
    plt.savefig(filename + '.pdf', additional_artists=art, bbox_inches="tight", *args, **kwargs)
    
def line_plot(ax, x, y, label=None):
    if label:
        ax.plot(x, y, label=label)
    else:
        ax.plot(x, y)

def bar_plot(ax, label, x, patch=False):
    postion = np.arange(len(label))
    ax.bar(postion, x, label="crime")
    ax.set_xticks(postion)
    ax.set_xticklabels(label)
    if patch:
        for p in ax.patches:
            ax.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2.,\
                        p.get_height()), ha='center', va='center', xytext=(0, 8), \
                        textcoords='offset points')
