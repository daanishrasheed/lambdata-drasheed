"""lambdata - collection of data science helper functions"""

import numpy as np
import pandas as pd

# sample code
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))


# sample functions


def increment(x):
    return x + 1
