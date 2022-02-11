import os
import pandas as pd

from c0001_retrieve_meta import retrieve_path
from c0010_analyze_general import analyze_general



def analyze_nsf_awards():
    """
    Objective: compare cell sources in the database
    """

    print('begin analyze_nsf_awards')

    name_article = 'nih_awards'
    analyze_general(name_article)

    print('begin analyze_nsf_awards')
