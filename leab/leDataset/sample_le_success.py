import pandas as pd
from pathlib import Path


class SampleLeSuccess:
    """
    Sample data to run with le Mean, from E. Miller default example in app.
    """
    def __init__(self):

        root = Path(__file__).parent
        file_A = root / 'data' / 'evan_miller_chi2_default_1.csv'
        file_B = root / 'data' / 'evan_miller_chi2_default_2.csv'
        file_C = root / 'data' / 'evan_miller_chi2_default_3.csv'
        file_D = root / 'data' / 'evan_miller_chi2_default_4.csv'
        file_E = root / 'data' / 'evan_miller_chi2_default_5.csv'

        self.A = pd.read_csv(
            file_A, names=["success"]
        )
        self.B = pd.read_csv(
            file_B, names=["success"]
        )
        self.C = pd.read_csv(
            file_C, names=["success"]
        )
        self.D = pd.read_csv(
            file_D, names=["success"]
        )
        self.E = pd.read_csv(
            file_E, names=["success"]
        )