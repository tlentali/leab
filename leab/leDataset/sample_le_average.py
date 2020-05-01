import pandas as pd
from pathlib import Path


class SampleLeAverage:
    """
    Sample data to run with leAverage, from E. Miller default example in app.
    """
    def __init__(self):

        root = Path(__file__).parent
        file_1 = root / 'data' / 'evan_miller_ttest_default_1.csv'
        file_2 = root / 'data' / 'evan_miller_ttest_default_2.csv'

        self.A = pd.read_csv(
            file_1, names=["values"]
        )
        self.B = pd.read_csv(
            file_2, names=["values"]
        )
