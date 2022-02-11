import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import statistics

from c0001_retrieve_meta import retrieve_path
from c0010_analyze_general import analyze_general
from c0010_analyze_general import name_paths
from find_color import find_color


def analyze_nih_awards():
    """
    Objective: compare cell sources in the database

    """

    tasks = [2]
    print('begin analyze_nih_awards')

    name_article = 'nih_awards'
    if 0 in tasks: tasks = np.arange(1,101,1)
    if 1 in tasks: analyze_general(name_article)
    if 2 in tasks: plot_year_cost(name_article)

    print('completed analyze_nih_awards')

def plot_year_cost(name_article):
    """
    Do shorter grants cost more?
    """

    name_src, name_dst, name_summary, name_unique, plot_unique = name_paths(name_article)
    file_name = os.path.join(retrieve_path(name_dst), 'agg_with_year' + '.csv')
    print('file_name = ' + str(file_name))
    df = pd.read_csv(file_name)

    col_name_x, col_name_y = 'Support Year', 'Direct Cost IC'

    print(list(df[col_name_x])[10:20])
    print(list(df[col_name_y])[10:20])

    # only plot rows with a float or int in both columns
    support_years, costs = [], []
    for i in range(len(list(df[col_name_x]))):
        #print('blaze 1')
        x = list(df[col_name_x])[i]
        y = list(df[col_name_y])[i]

        try:
            x = float(x)
            y = float(y)
            if x > 0 and y > 0:
                support_years.append(x)
                costs.append(y)
                print('x / y = ' + str(x) + ' / ' + str(y))
        except:
            x = 2
            #print('row skipped')
            #print('x / y = ' + str(x) + ' / ' + str(y))

    # create plot
    plt.close('all')
    plt.figure(figsize=(16, 6))
    xx, yy = support_years, costs
    colorMarker, colorEdge, colorTransparency = find_color(6)
    plt.scatter(xx, yy, s=40, color=colorMarker, edgecolor=colorEdge, alpha=colorTransparency)

    plt.title(str(len(yy)) + ' ' + name_article + ' included in plot.')
    plt.xlabel('Years of Support (mode = ' + str(round(statistics.mode(xx),1)) + ' years )')
    plt.ylabel('Direct Cost (mode = $' + str(round(statistics.mode(yy),2)) + ')')
    # plt.yscale('log')
    # plt.grid()

    plot_dst = os.path.join(retrieve_path('plot_nih_awards_year_cost'))
    plt.savefig(plot_dst, dpi = 600, edgecolor = 'w')
    print('saved plot: ' + plot_dst)
    plt.close('all')
