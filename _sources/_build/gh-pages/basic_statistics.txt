=================
Basic statistics
=================

.. topic:: **Prerequisites**

   This course assumes that you already know Python. The `scipy-lectures
   <http://scipy-lectures.github.io>`_ give an introduction to Python.

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

Mixed-type data: pandas
------------------------

We have a CSV file giving observations of brain size and weight and IQ
(Willerman et al. 1991):

  .. include:: examples/brain_size.csv
    :end-line: 5
    :literal:

.. sidebar:: **Separator**

   Although this is a 'CSV' file, the separator is ";".

|

The data are a mixture of numerical and categorical values. We will use
`pandas <http://pandas.pydata.org>`_ to manipulate them::

    >>> import pandas
    >>> data = pandas.read_csv('examples/brain_size.csv', sep=';')
    >>> print data  # doctest: +ELLIPSIS
        Unnamed: 0  Gender  FSIQ  VIQ  PIQ Weight Height  MRI_Count
    0            1  Female   133  132  124    118   64.5     816932
    1            2    Male   140  150  124      .   72.5    1001121
    2            3    Male   139  123  150    143   73.3    1038437
    3            4    Male   133  129  128    172   68.8     965353
    4            5  Female   137  132  134    147   65.0     951545
    ...

.. sidebar:: **Missing values**

   Note that the weight of the second individual is missing.

|

`data` is a pandas dataframe, that resembles R's dataframe::

    >>> print data.Gender  # doctest: +ELLIPSIS
    0     Female
    1       Male
    2       Male
    3       Male
    4     Female
    ...
    >>> gender_data = data.groupby('Gender')
    >>> print gender_data.mean()
            Unnamed: 0   FSIQ     VIQ     PIQ  MRI_Count
    Gender                                              
    Female       19.65  111.9  109.45  110.45   862654.6
    Male         21.35  115.0  115.25  111.60   954855.4

    >>> # More manual, but more versatile
    >>> for name, value in gender_data['VIQ']:
    ...     print name, np.mean(value)
    Female 109.45
    Male 115.25

|

.. image:: auto_examples/images/plot_categorical_variables_1.png
   :target: auto_examples/plot_categorical_variables.html
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

Male vs Female

Paired tests
------------

VIQ vs another IQ

Wilcoxon paired

Binomial test?
