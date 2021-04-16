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

    
    
    
    
# # x and y should both be categories
# # x is sorted by default
# def countplot(x, df, ax=None, y=None, yval=None, xorder=None, xlabel=None, ylabel=None, stacked=False, vert=True, 
#               normalize=False, annotate_bars=False, palette=None, **kwargs):
    
#     func = "barh" if vert==False else "bar"
#     ctab = pd.DataFrame()
#     pal = get_color()
    
#     # Do crosstab instead of just value counts - y is generally the color encoding
#     if y!=None:
#         ctab = pd.crosstab(df[x], df[y], dropna=False)
        
#         # Compute percentage along rows
#         if normalize:
#             ctab = ctab.div(ctab.sum(axis=1), axis=0)*100
        
#         # Just use one of the values, e.g. what percent of y == True for each category x
#         if yval!=None:
#             ctab = ctab.loc[:, yval].sort_values(ascending=False)
#             # Custom sort order
#             if xorder:
#                 ctab = ctab.loc[xorder]
#         else:
#             pal = get_palette()
#             # Custom sort order
#             if xorder:
#                 ctab = ctab.loc[xorder,:]
        
#         # Check for custom palette
#         if palette!=None:
#             pal = palette
        
#         ctab.plot(kind=func, ax=ax, width=0.85, rot=0, color=pal, stacked=stacked)
    
#     # value_counts branch
#     else:
#         ctab = df[x].value_counts()
        
#         # Compute what percentage of all samples is in each x category
#         if normalize:
#             ctab = ctab.div(ctab.sum())*100
#         # Custom sort order
#         if xorder:
#             ctab = ctab.loc[xorder]
#         # Check for custom palette
#         if palette!=None:
#             pal = palette  
        
#         ctab.plot(kind=func, ax=ax, width=0.85, rot=0, color=pal)

#     # Determine and set x and y axis labels
#     xlab = (xlabel if xlabel!=None else x)
#     ylab = (ylabel if ylabel!=None else ("Count" if normalize==False else ("% "+str(yval)+" of "+y if yval!=None else "% of total")))
#     xfontsize = kwargs.get('xlabel_fontsize', mpl.rcParams['axes.labelsize'])
#     yfontsize = kwargs.get('ylabel_fontsize', mpl.rcParams['axes.labelsize'])

#     if vert:
#         ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins='auto'))
#         ax.set_xlabel(xlab, fontsize=xfontsize)
#         ax.set_ylabel(ylab, fontsize=yfontsize)
#     else:
#         ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins='auto'))
#         ax.set_xlabel(ylab, fontsize=xfontsize)
#         ax.set_ylabel(xlab, fontsize=yfontsize)
    
#     # Code for annotating the bars
#     if annotate_bars and y!=None and yval==None:
#         print("INFO: Cannot annotate stacked or grouped bar charts")
    
#     elif annotate_bars:   
#         if normalize==False: labels = ["%d" % i for i in ctab.values]
#         else: labels = ["%.f%%" % i for i in ctab.values]
#         maxlen = len(max(labels, key=len))
#         labels = [(' ' * (maxlen - len(l))) + l for l in labels]
#         for rect, label in zip(ax.patches, labels):
#             if rect.get_height()==0 or rect.get_width()==0: continue
#             xoffset = (rect.get_width()/2 if vert else rect.get_width()-(ctab.values.max()*0.023*len(label)))
#             yoffset = (rect.get_height()-ctab.values.max()*0.035*len(label) if vert else (rect.get_height()/2*0.9))
#             ax.text(rect.get_x()+xoffset, rect.get_y()+yoffset, label, ha='center', va='center')
            
#     set_axis_props(ax, **kwargs)


# def boxplot(y, df, x=None, ax=None, showfliers=True, boxalpha=1, linecolor='#444', medianlinecolor='black',
#             linewidth=1, palette=get_palette(), xlabel=None, ylabel=None, vert=True, annotate_medians=False, 
#             annotation_xoffset=0, annotation_yoffset=0, **kwargs):
#     orient = ("v" if vert else "h")
#     # Swap x and y encodings for horizontal graph
#     if vert:
#         xenc=x; yenc=y
#     else:
#         xenc=y; yenc=x
#     sns.boxplot(y=yenc, x=xenc, data=df, palette=palette, ax=ax, linewidth=linewidth, showfliers=showfliers, 
#                 saturation=1, orient=orient,
#                 boxprops=dict(alpha=boxalpha, edgecolor=linecolor), whiskerprops=dict(color=linecolor), 
#                 medianprops=dict(linewidth=linewidth, color=medianlinecolor),
#                 capprops=dict(color=linecolor))
    
#     # Set x and y axis labels, swap if horizontal graph
#     xlab = (xlabel if xlabel!=None else x)
#     ylab = (ylabel if ylabel!=None else y)
#     if vert:
#         ax.set_ylabel(ylab); ax.set_xlabel(xlab)
#     else:
#         ax.set_ylabel(xlab); ax.set_xlabel(ylab)
        

            
#     set_axis_props(ax, **kwargs)