import pandas as pd


class SampleLeMean:
    """
    Sample data to run with le Mean, from E. Miller default example in app.
    """
    def __init__(self):
        self.A = pd.read_csv(
            "../../data/evan_miller_ttest_default_1.csv", names=["values"]
        )
        self.B = pd.read_csv(
            "../../data/evan_miller_ttest_default_2.csv", names=["values"]
        )
