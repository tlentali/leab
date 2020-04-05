import pandas as pd


class SampleLeAverage:
    """
    Sample data to run with leAverage, from E. Miller default example in app.
    """
    def __init__(self):
        self.A = pd.read_csv(
            "../../data/evan_miller_ttest_default_1.csv", names=["values"]
        )
        self.B = pd.read_csv(
            "../../data/evan_miller_ttest_default_2.csv", names=["values"]
        )
