import pandas as pd


class SampleLeSuccess:
    """
    Sample data to run with le Mean, from E. Miller default example in app.
    """
    def __init__(self):
        self.A = pd.read_csv(
            "../../data/evan_miller_chi2_default_1.csv", names=["success"]
        )
        self.B = pd.read_csv(
            "../../data/evan_miller_chi2_default_2.csv", names=["success"]
        )
        self.C = pd.read_csv(
            "../../data/evan_miller_chi2_default_3.csv", names=["success"]
        )
        self.D = pd.read_csv(
            "../../data/evan_miller_chi2_default_4.csv", names=["success"]
        )
        self.E = pd.read_csv(
            "../../data/evan_miller_chi2_default_5.csv", names=["success"]
        )