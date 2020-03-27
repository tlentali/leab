import pandas as pd
import statsmodels.stats.proportion as smp
from scipy.stats import chi2
import scipy.stats


class Chi2Sample:
    def __init__(self, sample: pd.DataFrame, confidence_level: float = 0.95):
        self.sample = sample
        self.confidence_level = confidence_level
        self.summary()

    def summary(self) -> None:
        self.get_success()
        self.get_trial()
        self.get_confidence_interval()

    def get_success(self) -> None:
        self.success = self.sample.sum()[0]

    def get_trial(self) -> None:
        self.trial = len(self.sample)

    def get_confidence_interval(self) -> None:
        self.conf_int = smp.proportion_confint(
            self.success, self.trial, alpha=1 - self.confidence_level, method="wilson"
        )
        self.conf_int_inf = self.conf_int[0] * 100
        self.conf_int_sup = self.conf_int[1] * 100
        self.confidence_interval = [self.conf_int_inf, self.conf_int_sup]


class leSuccess(Chi2Sample):
    """
    Build leSuccess object.

    Parameters:

        sample_A (pd.DataFrame): A sample data.
        sample_B (pd.DataFrame): B sample data.
        confidence_level (float): desired confidence level, default : 95%.
        
    Example:

        ::

            >>> from leab import leDataset
            >>> from leab import after

            >>> data = leDataset.SampleLeSuccess()
            >>> ab_test = after.leSuccess(data.A, 
            ...                           data.B, 
            ...                           confidence_level=0.95)
            >>> ab_test.sample_A.confidence_interval

            [8.526343659939133, 22.13718821096384]

            >>> ab_test.p_value

            0.25870176105718934
            
            >>> ab_test.get_verdict()
            
            'No significant difference'
        """
    def __init__(
        self,
        sample_A: pd.DataFrame,
        sample_B: pd.DataFrame,
        confidence_level: float = 0.95,
    ):
        self.confidence_level = confidence_level
        self.sample_A = Chi2Sample(sample_A, self.confidence_level)
        self.sample_B = Chi2Sample(sample_B, self.confidence_level)
        self.summary()

    def summary(self) -> None:
        self.get_contingency_table()
        self.get_observed_values()
        self.get_expected_values()
        self.get_chi_square_statistic()
        self.get_degree_of_freedom()
        self.get_p_value()

    def get_contingency_table(self) -> None:
        sample_A_value_counts = self.sample_A.sample["success"].value_counts()
        sample_B_value_counts = self.sample_B.sample["success"].value_counts()
        self.contingency_table = pd.DataFrame(
            [sample_A_value_counts, sample_B_value_counts]
        )

        self.contingency_table.index = ["sample_A", "sample_B"]
        self.contingency_table.columns = ["fail", "success"]

    def get_observed_values(self) -> None:
        self.observed_values = self.contingency_table.values

    def get_expected_values(self) -> None:
        b = scipy.stats.chi2_contingency(self.contingency_table)
        self.expected_values = b[3]

    def get_chi_square_statistic(self) -> None:
        chi_square = sum(
            [
                (o - e) ** 2.0 / e
                for o, e in zip(self.observed_values, self.expected_values)
            ]
        )
        self.chi_square_statistic = chi_square[0] + chi_square[1]

    def get_degree_of_freedom(self) -> None:
        no_of_rows = len(self.contingency_table.iloc[0:2, 0])
        no_of_columns = len(self.contingency_table.iloc[0, 0:2])
        self.degree_of_freedom = (no_of_rows - 1) * (no_of_columns - 1)

    def get_p_value(self) -> None:
        self.p_value = 1 - chi2.cdf(
            x=self.chi_square_statistic, df=self.degree_of_freedom
        )

    def get_verdict(self) -> None:
        if self.p_value < 1.0 - self.confidence_level:
            if (
                self.sample_A.success / self.sample_A.trial
                > self.sample_B.success / self.sample_B.trial
            ):
                print("Sample A is more successful")
            else:
                print("Sample B is more successful")
        else:
            print("No significant difference")
