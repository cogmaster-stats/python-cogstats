=================
FMRI signals
=================

Here we will cover fMRI signals and their analysis.

.. topic:: This page content

   The aim of this first part is to get familiar with fMRI data.

.. warning:: 

   Carve in your mind that the only characters you can safely use in a
   file name are non-accented upper and lower case letters, numbers and two
   special characters: the underscore "_" and the dot "." . Don't cry if you
   run into problems with file names including accents and space.
   
   Most of the problems one has to solve in any hands-on lab course are
   related to the students not knowing how to deal with the file structure
   of their own computer. If you are still unsure about concepts such as
   "home directory", "working directory", or "path", go back to your first
   lectures on python by Christophe Pallier and make sure you are able to
   explertly navigate in your file structure.


.. topic:: **Before we start: installing the software**

  .. toctree::

   install.rst


Activation IRMf
---------------

Why do we do activation fMRI?  Basically: localization Hypothesis:
functional specialization Aim: given a target process, detect the brain
areas involved Principle: the experimenter imposes on the subject a
temporal variation related to the target process and looks for whichever
part of the brain displays a signal in which the same variation could be
found.

=> we need to get the time series of BOLD signal AND the time series of
what happened to the subject AND they both have to be synchonous!

also

- resting state fMRI
- more than localization: connectivity

BOLD signal
-----------

BOLD signal: local vascular changes somehow related to increased brain
activity can be detected by a MRI scanner (T2* signal increases).
However the fluctuation of the signal induced by the BOLD effect is about
few percents.

fMRI stimulation data
---------------------

Same time reference than the MRI acquisitions.  Describe the time series
of conditions.

Reminder: we are looking for voxels in which part of the signal variance
is explained by our manipulation, thus we need to know what is the
shape of the temporal variation induces by our experimental paradigm. 

Let's start with a basi example taken from a classical auditory
stimulation dataset (exerpt from the SPM manual describing the
paradigm)::

    This data set comprises whole brain BOLD/EPI images acquired on a
    modified 2T Siemens MAGNETOM Vision system. Each acquisition consisted
    of 64 contiguous slices (64×64×64 3×3mm×3 mm3 voxels). Acquisition took
    6.05s, with the scan to scan repeat time (TR) set arbitrarily to 7s.
    96 acquisitions were made (TR=7s) from a single subject, in blocks of 6,
    giving 16 42s blocks. The condition for successive blocks alternated
    between rest and auditory stimulation, starting with rest. Auditory
    stimulation was bi-syllabic words presented binaurally at a rate of 60
    per minute. The functional data starts at acquisition 4

    To avoid T1 effects in the initial scans of an fMRI time series we
    recommend discarding the first few scans. To make this example simple,
    we’ll discard the first complete cycle (12 scans, 04-15), leaving 84
    scans, image files 16-99.

Two different ways of defining a regressor

1) manually::

    >>> reg=np.zeros(84)
    >>> reg[6]=1
    >>> reg[18]=1

2) using a .csv file which defines in different columns the runs, the
   conditions, the onset time and the duration.

Convolution
-----------

::

    >>> import nipy.modalities.fmri.hemodynamic_models as hm
    >>> hrf = hm.spm_hrf(1.0, oversampling=1)
    >>> plt.plot(np.convolve(reg, hrf))

Try to play a bit with the convolution using different regressors


fMRI scanner data
-----------------

As usual, we would like to measure a variation => temporal resolution
Localization => spatial resolution Trade-off : it takes more time to
acquire more data points.

The MRI scanner allows the BOLD signal to be recorded in a given space
where the experimenter puts the object to measure, in our case, a living
brain (and around: the human that sustains it).

Scanner => sequential acquisition of data

- 2D: one slice n * n voxels (a voxel is an element of volume, think 3D
  pixel)

- 3D: many slices = one volume, which usually covers the whole brain

- 4D: time series of sequentially acquired volumes == for each voxel, we
  get a time series

Let's look at the data:

Few words about DICOM files and nifti
Conversion:
Application Menu->NeuroDebian->Medical Imaging -> dcm2nii::

    >>> import numpy as np
    >>> from nipy import load_image
    >>> import matplotlib.pyplot as plt
    >>> i=load_image('host/python-cogstats/examples/wrf4d.nii.gz')
    >>> i.shape
    >>> i[0,0,0,0]
    

Now you can play with python in order to visualize

1) a slice

2) a volume

3) a time series in a given voxel


Now, try to get some time series using
Application Menu->NeuroDebian->Medical Imaging -> FSLview

Conclusions about the signal characteristics:

- NOISY!!!!
- Highly correlated, spatially, temporally!
- spatial resolution
- temporal resolution
- different sources of variations

Remember, the fluctuation induced by brain activity is few percents =>
measurement of a small effect size in huge noise => need for a LOT of
repetition!  => substractive approach


Analysis principle
------------------

As said earlier, the idea is to find voxels in which the regressor
describing a condition has some effect on the BOLD signal. Each regressor
is actually explaining a part of the variance in a Linear Model

Analysis example
----------------

The first example file is 'host/examples/plot_auditory_analysis.py'.

.. topic:: **Exercise**
    :class: green

    * Run the example.
    * Change the .csv file to make it match the actual paradigm.
    * Compare with a random-generated regressor.
    * Remarks?

Contrasts for T- and F-tests
----------------------------

- T-tests are used to compare the contributions of different regressors :
  one contrast vector
- F-tests are used to compare a model to a submodel (same as
  anova(model0,model 1) in R) : matrix identifying regressors that will
  NOT be in the submodel 

Another example
---------------

The second example file is 'host/examples/plot_localizer_analysis.py'

.. topic:: **Exercise**
    :class: green

    * Define some interesting contrasts prior to the analysis.
    * Run the example.

Multiple comparisons
--------------------

Several strategies.

1. Voxel-level

   * Uncorrected (silly)
   * Family-Wise: Bonferroni and others (only type I risk)
   * Estimation of independant elements of volume related to
     the spatial correlation: Random Field Theory
   * False Discovery Rate (type I and type II risks)
   * Reduce the number of voxels for the correction (ROI)


Number of voxels on which the model is estimated:

    >>> fmri_glm.glms[0].get_beta().shape
    >>> np.sum(fmri_glm.mask.get_data()!=0)

cumulative 
    >>> from scipy.stats import norm
    >>> norm.ppf(1-0.001)

.. topic:: **Exercise**
    :class: green

    1. Caclulate a Bonferroni-correcter threshold
    2. Apply 

2. Cluster-level

   * Permutation test



.. topic:: **Exercise**
    :class: green

    1. From the Z-map of a contrast, retrieve cluster sizes.
    2. Sort the Cluster sizes.
   
    >>> Z = z_map.get_data()
    >>> cluster_map, n_clusters = ndimage.label(np.abs(Z) > 2.5)
    >>> cluster_sizes_h0.append(np.bincount(cluster_map.ravel())[1:])

    3. What is the relathinship between the permutation and H0?
    4. What is permuted exactly?
    5. Run the file 'host/python-cogstats/examples/plot_permutation.py'

Second-level analysis
---------------------

Is related to between-subject comparison.
Fixed or Random effect analysis.
Necessitate normalization.



