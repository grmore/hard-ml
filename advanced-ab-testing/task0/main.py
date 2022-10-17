import numpy as np
import get_bernuilli_confidence_interval as bconf

if __name__ == '__main__':
    array_test = np.array([1, 1, 1, 0, 0, 1, 0])
    bernoulli_conf_interval = bconf.get_bernoulli_confidence_interval(array_test)
    print(bernoulli_conf_interval)
