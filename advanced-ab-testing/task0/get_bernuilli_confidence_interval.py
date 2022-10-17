import numpy as np


def get_bernoulli_confidence_interval(values: np.array):
    """Calculates the confidence interval for the Bernoulli distribution parameter.

     :param values: an array of elements of zeros and ones.
     :return (left_bound, right_bound): bounds of the confidence interval.
    """
    sample_mean = np.mean(values)
    sample_size = len(values)
    # normal approximation interval or Wald interval
    half_range = 1.96 * np.sqrt((sample_mean) * (1 - sample_mean) / sample_size)

    return (np.clip(sample_mean - half_range, 0, 1), np.clip(sample_mean + half_range, 0, 1))