"""

"""

import pandas
import numpy
import scipy
from scipy.stats import gamma, norm

# from fuzzywuzzy import process


# Create a test data set
size = 100
df = pandas.DataFrame({
    'ID': numpy.arange(start=1, stop=size + 1, step=1, dtype='int64'),
    'phone_type': numpy.random.choice(a=['FIX', 'MOB'], size=size),
    'random_normal_variates': numpy.random.randn(size),
    'diff_normal_dist': norm.rvs(.5, size=size),
    'b_ratio': gamma.rvs(1.5, size=size)

})

# The results from calculating the distributions and providers should be stored in a dictionary.
x = {}

# print(df.head())
# print(df.columns.values)
# print(df.dtypes)
print(df.describe())
# print(df['column_2'].describe())

providers = ['Normal Distribution', 'Another Normal Distribution', 'Ratio of Something', '_id', 'Phone']

# for column in df.columns:
#     provider, match = process.extractOne(column, providers)
#     print('Column: {} matched Provider {} with {} ratio.'.format(column, provider, match))

distributions = {'continuous': ['expon', 'norm'],
                 'multivariate': [],
                 'discrete': ['binom', 'geom' 'poisson']
                 }

continuous_dtypes = ['float', 'float64']
discrete_dtypes = ['int', 'int64']


def fit(data, **kwargs):
    """The fit method takes a numpy.Series
    
    :param data: 
    :return dist: 
    """
    if data.dtype in continuous_dtypes:
        # The location (loc) keyword specifies the mean. The scale (scale) keyword specifies the standard deviation.
        loc = data.mean
        scale = data.std
        for distribution in distributions["continuous"]:
            _, _, _ = scipy.stats.norm.fit(data, loc=loc, scale=scale)

        r

    elif data.dtype in discrete_dtypes:

        return
