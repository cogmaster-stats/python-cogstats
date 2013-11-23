=================
Basic statistics
=================

.. topic:: **Prerequisites**

   This course assumes that you already know Python syntax. An
   introduction to Python can be found in the `scipy-lectures
   <http://scipy-lectures.github.io>`_.

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

Basic array manipulation
-------------------------

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


