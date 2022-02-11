import numpy as np

from c0100_analyze_nih_awards import analyze_nih_awards
from c0200_analyze_clinical_trials import analyze_clinical_trials
from c0300_analyze_nsf_awards import analyze_nsf_awards

from c9900_build_webpage import build_webpage


def main():
    """
    Motivation:
        Did the cell therapy/regenerative medicine community start with autologous cell source?
        Why?
        Were there limitations of that approach due to patient-to-patient variabiity?

        Is there an observable trend toward allogeneic cell sources?
        Why?
        Is this because off-the-shelf, well characterized cells, perform in a predictable manner.

    Objective:
        Analyze publicly available datasets to compare research output and resource investment in several types of cell sources.

    Tasks:
        1. Analyze NIH Awards
        2. Analyze NSF Awards
        3. Analyze Clinical Trials
        4. Analyze US Patent Office
        5. Analyze Peer Reviewed Literature

        6. Answer - is the approach changing course?
    """

    # List task numbers to complete
    tasks = [100]

    print('beginning main')
    if 0 in tasks: tasks = np.arange(1, 101, 1)
    if 1 in tasks: analyze_nih_awards()
    if 2 in tasks: analyze_clinical_trials()
    if 3 in tasks: analyze_nsf_awards()
    if 100 in tasks: build_webpage()
    print('completed main')


if __name__ == "__main__":
    main()
