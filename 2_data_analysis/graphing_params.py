import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# svg.fonttype:
# 'none': Assume fonts are installed on the machine where the SVG will be viewed.
# 'path': Embed characters as paths -- supported by most SVG renderers

mpl.rcParams.update({
    'svg.fonttype':'none', 
    'font.family':'Arial',
    'axes.spines.top': False,
    'axes.spines.right': False, 
    'axes.axisbelow': True,
    'axes.linewidth':0.8,
    'font.size':9,
    'axes.labelsize':9,
    'legend.fontsize':9,
    'xtick.labelsize':8,
    'ytick.labelsize':8,
    'lines.linewidth':1,
    'figure.dpi': 100,
    'grid.color': '#EFEFEF',
    'figure.facecolor':'white',
    'legend.edgecolor': '1',
    'legend.facecolor':'#fff',
    'legend.frameon':True,
    'legend.framealpha': 0.9,
})

# From: okabe-ito from http://jfly.iam.u-tokyo.ac.jp/color/#pallet
def get_palette(name="okabe-ito"):
    if name=="okabe-ito":
        return [get_color(x) for x in ['sky-blue', 'orange', 'green', 'yellow', 'blue', 'dark-orange', 'pink']]
    if name=="okabe-ito-2":
        return [get_color(x) for x in ['sky-blue', 'orange', 'yellow', 'green']]
    if name=="okabe-ito-3":
        return [get_color(x) for x in ['orange', 'sky-blue', 'green']]
    
def get_color(name='light-grey'):
    return {
        'sky-blue':'#56b4e9',
        'orange':'#e69f00',
        'green':'#009e73',
        'yellow':'#f0e442',
        'blue':'#0072b2',
        'dark-orange':'#d55e00',
        'pink':'#cc79a7',
        'light-grey':'#ccc',
    }[name]


def set_axis_props(ax, **kwargs):
    
    xlab = kwargs.get('xlabel', None)
    xfontsize = kwargs.get('xlabel_fontsize', mpl.rcParams['axes.labelsize'])
    if xlab != None:
        ax.set_xlabel(xlab, fontsize=xfontsize)
        
    ylab = kwargs.get('ylabel', None)
    yfontsize = kwargs.get('ylabel_fontsize', mpl.rcParams['axes.labelsize'])
    if ylab != None:
        ax.set_ylabel(ylab, fontsize=yfontsize)
    
    show_xticks = kwargs.get('show_xticks', True)
    if show_xticks==False:
        ax.tick_params(axis='x', which='both', length=0)
    
    show_yticks = kwargs.get('show_yticks', True)
    if show_yticks==False:
        ax.tick_params(axis='y', which='both', length=0)
        
    show_yticklabels = kwargs.get('show_yticklabels', True)
    if show_yticklabels==False:
        ax.get_yaxis().set_ticks([])
        
    show_xticklabels = kwargs.get('show_xticklabels', True)
    if show_xticklabels==False:
        ax.get_xaxis().set_ticks([])
        
    xtick_fontsize = kwargs.get('xtick_fontsize', mpl.rcParams['xtick.labelsize'])
    ax.tick_params(axis='x', which='both', labelsize=xtick_fontsize)
    
    ytick_fontsize = kwargs.get('ytick_fontsize', mpl.rcParams['ytick.labelsize'])
    ax.tick_params(axis='y', which='both', labelsize=ytick_fontsize)

    show_xaxis = kwargs.get('show_xaxis', True)
    if show_xaxis==False:
        ax.spines['bottom'].set_visible(False)
        
    show_top_spine = kwargs.get('show_top_spine', False)
    if show_top_spine==True:
        ax.spines['top'].set_visible(True)

    show_right_spine = kwargs.get('show_right_spine', False)
    if show_right_spine==True:
        ax.spines['right'].set_visible(True)