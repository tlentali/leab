import pandas as pd
import numpy as np
import scipy.special as sc
import statistics


class TTestSample:
    def __init__(self, sample: pd.DataFrame, confidence_level: float):
        self.sample = sample
        self.confidence_level = confidence_level
        self.summary()

    def summary(self) -> None:
        self.get_mean()
        self.get_std()
        self.get_count()
        self.get_variance()
        self.get_mean_stddev()
        self.get_nu()
        self.get_confidence_interval()
        self.get_mean_difference_with_confidence_interval()

    def get_mean(self) -> None:
        self.mean = np.mean(self.sample)[0]

    def get_std(self) -> None:
        # using the std from Pandas doesn't match the expected result
        # we use stdev from statistics instead
        self.std = statistics.stdev(self.sample.iloc[:, 0].tolist())

    def get_count(self) -> None:
        self.count_elt = len(self.sample)

    def get_variance(self) -> None:
        self.variance = self.std * self.std

    def get_mean_stddev(self) -> None:
        self.mean_stddev = np.sqrt(self.variance / self.count_elt)

    def get_nu(self) -> None:
        self.nu = self.count_elt - 1

    def get_invBeta(self) -> None:
        self.invBeta = sc.betaincinv(0.5 * self.nu, 0.5, 1 - self.confidence_level)

    def get_t(self) -> None:
        self.t = np.sqrt(self.nu / self.invBeta - self.nu)

    def get_confidence_interval(self) -> None:
        self.get_invBeta()
        self.get_t()
        self.conf_inf = self.mean - (self.t * self.mean_stddev)
        self.conf_sup = self.mean + (self.t * self.mean_stddev)
        self.confidence_interval = [self.conf_inf, self.conf_sup]

    def get_mean_difference_with_confidence_interval(self) -> None:
        self.mean_difference_with_confidence_interval = (
            self.mean - self.confidence_interval[0]
        )

    def plot_distribution(self):
        pass


class leMean(TTestSample):
    """
    Build leMean object.

    Parameters:

        sample_A (pd.DataFrame): A sample data.
        sample_B (pd.DataFrame): B sample data.
        confidence_level (float): desired confidence level, default : 95%.
        
    Example:

        ::

            >>> from leab import after
            >>> from leab import leDataset

            >>> data = leDataset.SampleLeMean()
            >>> ab_test = after.leMean(data.A, data.B)

            >>> ab_test.sample_A.confidence_interval

            [34.75214007684581, 81.59785992315418]

            >>> ab_test.get_verdict()

            'Sample A mean is greater'
        """
    def __init__(
        self,
        sample_A: pd.DataFrame,
        sample_B: pd.DataFrame,
        confidence_level: float = 0.95,
    ):
        self.confidence_level = confidence_level
        self.sample_A = TTestSample(sample_A, confidence_level)
        self.sample_B = TTestSample(sample_B, confidence_level)
        self.compute_ttest()

    def compute_ttest(self) -> None:
        self.get_diff_mean()
        self.get_diff_variance()
        self.get_diff_df()
        self.get_diff_mean_stddev()
        self.get_t()
        self.get_x()
        self.get_p_value()
        self.get_d()
        self.get_SE()

    def get_diff_mean(self) -> None:
        self.diff_mean = self.sample_A.mean - self.sample_B.mean

    def get_diff_variance(self) -> None:
        self.diff_variance = (
            self.sample_A.variance / self.sample_A.count_elt
            + self.sample_B.variance / self.sample_B.count_elt
        )

    def get_diff_df(self) -> None:
        self.diff_df = (
            self.diff_variance
            * self.diff_variance
            / (
                (self.sample_A.variance / self.sample_A.count_elt)
                * (self.sample_A.variance / self.sample_A.count_elt)
                / (self.sample_A.count_elt - 1)
                + (self.sample_B.variance / self.sample_B.count_elt)
                * (self.sample_B.variance / self.sample_B.count_elt)
                / (self.sample_B.count_elt - 1)
            )
        )

    def get_diff_mean_stddev(self) -> None:
        self.diff_mean_stddev = np.sqrt(self.diff_variance)

    def get_t(self) -> None:
        self.t = self.diff_mean / self.diff_mean_stddev

    def get_x(self) -> None:
        self.x = self.diff_df / (self.diff_df + self.t * self.t)

    def get_p_value(self) -> None:
        self.p_value = sc.betainc(self.diff_df / 2, 0.5, self.x)

    def get_d(self) -> None:
        self.d = self.diff_mean

    def get_SE(self) -> None:
        self.SE = self.diff_mean_stddev

    def plot_difference_of_means(self):
        pass

    def get_verdict(self) -> None:
        if self.p_value < 1 - self.confidence_level:
            if self.sample_A.mean > self.sample_B.mean:
                print("Sample A mean is greater")
            else:
                print("Sample B mean is greater")
        else:
            print("No significant difference")
