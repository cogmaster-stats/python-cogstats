"""
Plotting quantities from a CSV file
=====================================

This example loads from a CSV file data with mixed numerical and
categorical entries, and plots a few quantities, separately for females
and males.

"""

import pandas

import matplotlib.pyplot as plt

data = pandas.read_csv('brain_size.csv', sep=';')
gender_data = data.groupby('Gender')
gender_data.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])

plt.show()
