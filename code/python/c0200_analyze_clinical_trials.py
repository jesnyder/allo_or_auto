import numpy as np
import os
import pandas as pd

from c0001_retrieve_meta import retrieve_path
from c0010_analyze_general import analyze_general


def analyze_clinical_trials():
    """
    Objective: compare cell sources in the database

    Tasks:
        1. Aggregate NIH award
        2.

    """

    print('begin analyze_clinical_trials')

    name_article = 'nih_awards'
    analyze_general(name_article)

    print('begin completed_clinical_trials')
