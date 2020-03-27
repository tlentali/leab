import numpy as np
from scipy.stats import norm


class leSample:
    """
    Build leSample object.

    Parameters:

        conversion_rate (float): baseline conversion rate.
        min_detectable_effect (float): minimum detectable effect.
        significance_level (float): alpha, percent of the time a difference will be detected, assuming one does NOT exist.
        statistical_power (float): 1-beta, percent of the time the minimum effect size will be detected, assuming it exists.
    
    Example:

        ::

            >>> from leab import before

            >>> ab_test = before.leSample(conversion_rate=20, 
            ...                           min_detectable_effect=2)
            >>> ab_test.get_size()
            6347

            >>> ab_test.get_duration(avg_daily_total_visitor=1000)
            13
        """
    def __init__(
        self,
        conversion_rate: float,
        min_detectable_effect: float,
        significance_level: float = 0.05,
        statistical_power: float = 0.8,
        absolute: bool = True,
    ):
        self.conversion_rate = conversion_rate / 100
        self.absolute = absolute
        self.min_detectable_effect = min_detectable_effect / 100
        self.absolute_or_relative()
        self.significance_level = significance_level
        self.statistical_power = statistical_power
        self.alpha = significance_level
        self.beta = 1 - statistical_power
        self.n = None

    def absolute_or_relative(self) -> None:
        """
        Set up the min_detectable_effect absolute value or relative to conversion_rate.
        """
        if self.absolute:
            self.min_detectable_effect = self.min_detectable_effect
        else:
            self.min_detectable_effect = (
                self.conversion_rate * self.min_detectable_effect
            )

    @staticmethod
    def compute_z_score(alpha: float) -> float:
        """
        Compute z score from alpha value.

        Parameters: 

            alpha (float): required alpha value (alpha should already fit the required test).

        Returns: 

            Z-score.
        """
        return norm.ppf(alpha)

    def _get_z_1(self) -> None:
        self.significance = 1 - (self.alpha / 2)
        self.z_1 = self.compute_z_score(self.significance)

    def _get_z_2(self) -> None:
        self.power = 1 - self.beta
        self.z_2 = self.compute_z_score(self.power)

    def _get_zs(self) -> None:
        self._get_z_1()
        self._get_z_2()

    def _get_sd1(self) -> None:
        """
        Compute standard deviation v1.  
        p-baseline conversion rate which is our estimated p and d-minimum detectable change.
        """
        self.sd1 = np.sqrt(2 * self.conversion_rate * (1 - self.conversion_rate))

    def _get_sd2(self) -> None:
        """
        Compute standard deviation v1.
        p-baseline conversion rate which is our estimated p and d-minimum detectable change.
        """
        self.sd2 = np.sqrt(
            self.conversion_rate * (1 - self.conversion_rate)
            + (self.conversion_rate + self.min_detectable_effect)
            * (1 - (self.conversion_rate + self.min_detectable_effect))
        )

    def _get_sds(self) -> None:
        self._get_sd1()
        self._get_sd2()

    def _compute_n(self) -> None:
        self.n = int(
            np.round(
                ((self.z_1 * self.sd1 + self.z_2 * self.sd2) ** 2)
                / (self.min_detectable_effect ** 2)
            )
        )

    def get_size(self) -> int:
        """
        Calls all methods used to get the size needed per group to get significance on the test.

        Returns: 

            Minimum sample size required per group according to metric denominator.
        """
        self._get_zs()
        self._get_sds()
        self._compute_n()
        return self.n

    def get_duration(self, avg_daily_total_visitor: int, nb_split: int = 2) -> int:
        """
        Compute the estimate duration in day needed to get significance on the test.

        Parameters:

            avg_daily_total_visitor (int): The first parameter.
            nb_split (int): The second parameter.

        Returns:

            Return the estimate duration in day needed to get significance on the test.
        """
        self.avg_daily_total_visitor = avg_daily_total_visitor
        self.nb_split = nb_split
        if self.n:
            self.duration = int(
                np.round(self.n / (self.avg_daily_total_visitor / self.nb_split))
            )
        else:
            self.get_size()
            self.duration = int(
                np.round(self.n / (self.avg_daily_total_visitor / self.nb_split))
            )
        return self.duration
