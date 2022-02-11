import os
import pandas as pd

from c0001_retrieve_meta import retrieve_path
from c0100_analyze_nih_awards import aggregate_articles
from c0100_analyze_nih_awards import add_year
from c0100_analyze_nih_awards import articles_per_year



def analyze_nsf_awards():
    """
    Objective: compare cell sources in the database

    Tasks:
        1. Aggregate NIH award
        2.

    """

    print('begin analyze_nsf_awards')

    tasks = [0]

    # name paths to files using article name
    name_article = 'nsf_awards'
    name_src = str(name_article + '_search')
    name_dst = str('df_' + name_article + '_search')
    name_summary = str('sum_' + name_article)
    name_unique = str(name_article + '_unique')
    plot_unique = str(name_article + '_unique_plot')

    if 1 in tasks: aggregate_articles(name_src, name_dst, name_summary)

    print('begin analyze_nsf_awards')
