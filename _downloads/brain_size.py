"""
Relating Gender and IQ
=======================

Going back to the brain size + IQ data, test if the VIQ of male and
female are different after removing the effect of brain size, height and
weight.
"""
import pandas
from statsmodels.formula.api import ols

data = pandas.read_csv('../brain_size.csv', sep=';', na_values='.')

model = ols('VIQ ~ Gender + MRI_Count + Height', data).fit()
print(model.summary())

# Here, we don't need to define a contrast, as we are testing a single
# coefficient of our model, and not a combination of coefficients.
# However, defining a contrast, which would then be a 'unit contrast',
# will give us the same results
print(model.f_test([0, 1, 0, 0]))
