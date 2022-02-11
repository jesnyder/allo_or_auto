import numpy as np
import os
import pandas as pd

from c0001_retrieve_meta import retrieve_path
from c0100_analyze_nih_awards import aggregate_articles
from c0100_analyze_nih_awards import add_year
from c0100_analyze_nih_awards import unique_values
from c0100_analyze_nih_awards import unique_plot
from c0100_analyze_nih_awards import articles_per_year


def analyze_clinical_trials():
    """
    Objective: compare cell sources in the database

    Tasks:
        1. Aggregate NIH award
        2.

    """

    print('begin analyze_clinical_trials')

    tasks = [0]

    # name paths to files using article name
    name_article = 'clinical_trials'
    name_src = str(name_article + '_search')
    name_dst = str('df_' + name_article + '_search')
    name_summary = str('sum_' + name_article)
    name_unique = str(name_article + '_unique')
    plot_unique = str(name_article + '_unique_plot')

    # tasks 
    if 0 in tasks: tasks = np.arange(1, 100, 1)
    if 1 in tasks: aggregate_articles(name_src, name_dst, name_summary)
    if 2 in tasks: add_year(name_dst, name_summary)
    if 3 in tasks: unique_values(name_dst, name_unique)
    if 4 in tasks: unique_plot(name_unique, plot_unique)
    if 5 in tasks: articles_per_year(name_dst)

    print('begin completed_clinical_trials')
