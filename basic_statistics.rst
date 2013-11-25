=================
Basic statistics
=================

.. topic:: **Prerequisites**

   This course assumes that you already know Python. The `scipy-lectures
   <http://scipy-lectures.github.io>`_ give an introduction to Python.

.. tip::

    This course gives an introduction to statistics with Python. It is
    useful to get acquainted with data representations in Python. In
    terms of experimental psychology, the patterns demonstrated here can
    be applied to simple dataset that arise from psychophysics, or
    reaction time experiments. We will see how to process efficiently
    more complex data as produced by brain imaging in the next course.

.. contents:: Contents
   :local:
   :depth: 1

|

Interacting with data
======================

Work environment: IPython
---------------------------

.. tip::

    We will be working in the interactive Python prompt, `IPython
    <http://ipython.org/>`_. You can either start it by itself, or in the 
    `spyder <http://code.google.com/p/spyderlib>`_ environment.

    In this document, the Python prompts are represented with the sign
    ">>>". If you need to copy-paste code, you can click on the top right
    of the code blocks, to hide the prompts and the outputs.

Basic array manipulation: numpy
--------------------------------

We have the reaction times in a psychophysical experiment:

  474.688  506.445  524.081  530.672  530.869 566.984  582.311  582.940 603.574  792.358

In Python, we will represent them using a numerical "array", with the
:mod:`numpy` module::

    >>> import numpy as np
    >>> x = np.array([474.688, 506.445, 524.081, 530.672, 530.869, 566.984, 582.311, 582.940, 603.574, 792.358])

We can access the elements of x with **indexing, starting at 0**::

    >>> x[0]    # First element
    474.68799999999999
    >>> x[:3]   # Up to the third element
    array([ 474.688,  506.445,  524.081])
    >>> x[-1]   # Last element
    792.35799999999995

Mathematical operations on arrays are done using the numpy module::

    >>> np.max(x)
    792.35799999999995
    >>> np.sum(x[:3])
    1505.2139999999999
    >>> np.mean(x)
    569.49219999999991
    >>> np.log(x)
    array([ 6.16265775,  6.22741573,  6.26164625,  6.27414413,  6.27451529,
            6.34033108,  6.36700467,  6.36808427,  6.40286865,  6.67501331])

.. topic:: **Finding help**

   * The reference documentation can be found on http://docs.scipy.org
   * http://scipy-lectures.github.io contains tutorials on Python, numpy,
     and the scientific Python ecosystem.
   * Typing `np.mean?` in IPython will display help on
     :func:`numpy.mean`.
   * :func:`numpy.lookfor` can be used to search for keywords in
     functions help.

|


.. topic:: **Exercise**
    :class: green

    * Display the last two entries of x.
    * Compute the standard deviation of x (how will you find the function
      to do so?).


Basic plotting: pylab
----------------------

The box plot
.............

.. image:: auto_examples/images/plot_basic_statistics_1.png
   :scale: 40
   :target: auto_examples/plot_localizer_analysis.html
   :align: right

Basic plotting is done with `matplotlib <http://matplotlib.org/>`_::

    >>> from matplotlib import pyplot as plt
    >>> plt.boxplot(x)      # doctest: +SKIP

|

.. hint::

   If a window doesn't display, you need to call `plt.show()`.

   Under IPython, type `%matplotlib` to have plots display automatically.

More plots
...........

.. image:: auto_examples/matplotlib_demos/images/plot_plot_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_plot.html
.. image:: auto_examples/matplotlib_demos/images/plot_scatter_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_scatter.html
.. image:: auto_examples/matplotlib_demos/images/plot_bar_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_bar.html
.. image:: auto_examples/matplotlib_demos/images/plot_contour_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_contour.html
.. image:: auto_examples/matplotlib_demos/images/plot_imshow_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_imshow.html
.. image:: auto_examples/matplotlib_demos/images/plot_pie_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_pie.html
.. image:: auto_examples/matplotlib_demos/images/plot_multiplot_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_multiplot.html
.. image:: auto_examples/matplotlib_demos/images/plot_text_1.png
   :scale: 45
   :target: auto_examples/matplotlib_demos/plot_text.html


.. seealso::

   Matplotlib is very rich and can be controlled in detail. See the
   `scipy lectures
   <http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html>`_
   for more details.

Mixed-type data: pandas
------------------------

Inputing data
..............

We have a CSV file giving observations of brain size and weight and IQ
(Willerman et al. 1991):

  .. include:: examples/brain_size.csv
    :end-line: 5
    :literal:

.. sidebar:: **Separator**

   Although it is a 'CSV' file, the separator is ";".

|

The data are a mixture of numerical and categorical values. We will use
`pandas <http://pandas.pydata.org>`_ to manipulate them::

    >>> import pandas
    >>> data = pandas.read_csv('examples/brain_size.csv', sep=';', na_values=".")
    >>> print data  # doctest: +ELLIPSIS
        Unnamed: 0  Gender  FSIQ  VIQ  PIQ  Weight  Height  MRI_Count
    0            1  Female   133  132  124     118    64.5     816932
    1            2    Male   140  150  124     NaN    72.5    1001121
    2            3    Male   139  123  150     143    73.3    1038437
    3            4    Male   133  129  128     172    68.8     965353
    4            5  Female   137  132  134     147    65.0     951545
    ...

.. warning:: **Missing values**

   The weight of the second individual is missing in the CSV file. If we
   don't specify the missing value (NA = not available) marker, we will
   not be able to do statistics on the weight.

Manipulating data
..................

`data` is a pandas dataframe, that resembles R's dataframe::

    >>> print data['Gender']  # doctest: +ELLIPSIS
    0     Female
    1       Male
    2       Male
    3       Male
    4     Female
    ...
    >>> gender_data = data.groupby('Gender')
    >>> print gender_data.mean()
            Unnamed: 0   FSIQ     VIQ     PIQ      Weight     Height  MRI_Count
    Gender                                                                     
    Female       19.65  111.9  109.45  110.45  137.200000  65.765000   862654.6
    Male         21.35  115.0  115.25  111.60  166.444444  71.431579   954855.4


    >>> # More manual, but more versatile
    >>> for name, value in gender_data['VIQ']:
    ...     print name, np.mean(value)
    Female 109.45
    Male 115.25

    >>> # Simpler selector
    >>> data[data['Gender'] == 'Female']['VIQ'].mean()
    109.45

|

.. image:: auto_examples/images/plot_pandas_1.png
   :target: auto_examples/plot_pandas.html
   :align: right
   :scale: 40


.. topic:: **Exercise**
    :class: green

    * What is the mean value for VIQ for the full population?
    * How many males/females were included in this study?

      **Hint** use 'tab completion' to find out the methods that can be
      called, instead of 'mean' in the above example.

    * What is the average value of MRI counts expressed in log units, for
      males and females?

Plotting data
..............

Pandas comes with some plotting tools (that use matplotlib behind the
scene) to display statistics on dataframes::

    >>> from pandas.tools import plotting
    >>> plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])   # doctest: +SKIP

.. image:: auto_examples/images/plot_pandas_2.png
   :target: auto_examples/plot_pandas.html
   :scale: 50
   :align: center

::

    >>> plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])   # doctest: +SKIP

.. sidebar:: **Two populations**

   The IQ metrics are bimodal. It looks like there are 2 sub-populations.
   We will come back to this hypothesis.

.. image:: auto_examples/images/plot_pandas_3.png
   :target: auto_examples/plot_pandas.html
   :scale: 50
   :align: center

.. topic:: **Exercise**
    :class: green

    Plot the scatter matrix for males only, and for females only. Do you
    think that the 2 sub-populations correspond to gender?

|

Hypothesis testing: two-group comparisons
==========================================

For simple statistical tests, we will use the `stats` sub-module of 
`scipy <http://docs.scipy.org/doc/>`_::

    >>> from scipy import stats

.. seealso::

   Scipy is a vast library. For a tutorial covering the whole scope of
   scipy, see http://scipy-lectures.github.io/


Student's t-test
-----------------

1-sample t-test
...............

:func:`scipy.stats.ttest_1samp` tests if observations are drawn from a
Gaussian distributions of given population mean. It returns the T
statistic, and the p-value (see the function's help)::

    >>> stats.ttest_1samp(data['VIQ'], 0)
    (30.088099970849338, 1.3289196468727784e-28)

.. tip::
   
    With a p-value of 10^-28 we can claim that the population mean for
    the IQ (VIQ measure) is not 0.

.. image:: images/two_sided.png
   :scale: 50
   :align: right

.. topic:: **Exercise**
    :class: green

    Is the test performed above one-sided or two-sided? Which one should
    we use, and what is the corresponding p-value?

2-sample t-test
................

We have seen above that the mean VIQ in the male and female populations
were different. To test if this is significant, we do a 2-sample t-test
with :func:`scipy.stats.ttest_ind`::

    >>> female_viq = data[data['Gender'] == 'Female']['VIQ']
    >>> male_viq = data[data['Gender'] == 'Male']['VIQ']
    >>> stats.ttest_ind(female_viq, male_viq)
    (-0.77261617232750124, 0.44452876778583217)

Paired tests
------------

.. image:: auto_examples/images/plot_pandas_4.png
   :target: auto_examples/plot_pandas.html
   :scale: 70
   :align: right

PIQ, VIQ, and FSIQ give 3 measures of IQ. Let us test if FISQ and PIQ are
significantly different. We need to use a 2 sample test::

    >>> stats.ttest_ind(data['FSIQ'], data['PIQ'])
    (0.46563759638096403, 0.64277250094148408)

The problem with this approach is that is forgets that there are links
between observations: FSIQ and PIQ are measure on the same individuals.
Thus the variance due to inter-subject variability is confounding, and
can be removed, using a "paired test", or "repeated measure test"::

    >>> stats.ttest_rel(data['FSIQ'], data['PIQ'])
    (1.7842019405859857, 0.082172638183642358)

.. image:: auto_examples/images/plot_pandas_5.png
   :target: auto_examples/plot_pandas.html
   :scale: 60
   :align: right

This is equivalent to a 1-sample test on the difference::

    >>> stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)
    (1.7842019405859857, 0.082172638183642358)

|

T-tests assume Gaussian errors. The bi-modal distribution viewed on the
scatter matrices tells us that a Gaussian distribution is unlikely. We
can use a `Wilcoxon signed-rank test
<http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test>`_, that relaxes
this assumption::

    >>> stats.wilcoxon(data['FSIQ'], data['PIQ'])
    (274.5, 0.034714577290489719)

.. note::

   The corresponding test in the non paired case is the `Mann–Whitney U
   test <http://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U>`_,
   :func:`scipy.stats.mannwhitneyu`.

.. topic:: **Exercice**
   :class: green

   * Test the difference between weights in males and females.

   * Use non parametric statistics to test the difference between VIQ in
     males and females.

|

Linear models, ANOVA
======================

A simple linear regression
---------------------------

.. image:: auto_examples/images/plot_regression_1.png
   :target: auto_examples/plot_regression.html
   :scale: 60
   :align: right

Given two set of observations, `x` and `y`, we want to test the
hypothesis that `y` is a linear function of `x`. In other terms:

    :math:`y = x * coef + e`

where `e` is observation noise. We will use the `statmodels
<http://statsmodels.sourceforge.net/>`_ module to:

#. Fit a linear model. We will use the simplest strategy, `ordinary least
   squares <http://en.wikipedia.org/wiki/Ordinary_least_squares>`_ (OLS).

#. Test that `coef` is non zero.

|

First, we generate simulated data according to the model::

    >>> x = np.linspace(-5, 5, 20)
    >>> np.random.seed(1)
    >>> # normal distributed noise
    >>> y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
    >>> # Create a data frame containing all the relevant variables
    >>> data = pandas.DataFrame({'x': x, 'y': y})

Specify an OLS model and fit it::

    >>> from statsmodels.formula.api import ols
    >>> model = ols("y ~ x", data).fit()
    >>> print(model.summary())  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE 
                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                      y   R-squared:                       0.804
    Model:                            OLS   Adj. R-squared:                  0.794
    Method:                 Least Squares   F-statistic:                     74.03
    Date:                ...                Prob (F-statistic):           8.56e-08
    Time:                        ...        Log-Likelihood:                -57.988
    No. Observations:                  20   AIC:                             120.0
    Df Residuals:                      18   BIC:                             122.0
    Df Model:                           1                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [95.0% Conf. Int.]
    ------------------------------------------------------------------------------
    Intercept     -5.5335      1.036     -5.342      0.000        -7.710    -3.357
    x              2.9369      0.341      8.604      0.000         2.220     3.654
    ==============================================================================
    Omnibus:                        0.100   Durbin-Watson:                   2.956
    Prob(Omnibus):                  0.951   Jarque-Bera (JB):                0.322
    Skew:                          -0.058   Prob(JB):                        0.851
    Kurtosis:                       2.390   Cond. No.                         3.03
    ==============================================================================

.. topic:: **Exercise**

   Retrieve the estimated parameters from the model above. **Hint**:
   use tab-completion to find the relevent attribute.



