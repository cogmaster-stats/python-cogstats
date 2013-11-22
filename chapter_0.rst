First course
============

Activation IRMf
---------------

Why do we do activation fMRI?
Basically: localization
Hypothesis: functional specialization
Aim: given a target process, detect the brain areas involved
Principle: the experimenter imposes on the subject a temporal variation related to the target process and looks for whichever part of the brain displays a signal in which the same variation could be found.

=> we need to get the time series of BOLD signal AND the time series of what happened to the subject AND they both have to be synchonous!

also
- resting state fMRI
- more than localization: connectivity

BOLD signal
-----------

BOLD signal: local vascular changes somehow related to increased brain activity can be detected by a MRI scanner (T2* signal increases).
However the fluctuation of the signal induced by the BOLD effect is about few percents.

fMRI data
---------

As usual, we would like to measure a variation => temporal resolution
Localization => spatial resolution
Trade-off : it takes more time to acquire more data points.

The MRI scanner allows the BOLD signal to be recorded in a given space where the experimenter puts the object to measure, in our case, a living brain (and around: the human that sustains it).

Scanner => sequential acquisition of data
- 2D: one slice n * n voxels (a voxel is an element of volume, think 3D pixel)
- 3D: many slices = one volume, which usually covers the whole brain
- 4D: time series of sequentially acquired volumes == for each voxel, we get a time series

Let's look at the data:

1) a volume:
montrer qu'un volume est une matrice dont les dimensions sont imposées par le champ de vue, le nombre de coupes et la taille des voxels
sous SPM :
v=spm_read_vols(spm_vol_nifti('path_vers_mon_image.nii'));
size(v);
signal in a pixel:
v(i,j,k);

2) a slice
surf(v(:,:,size(v,3)/2));

3) time series
P=ls(path_to_images/*.nii);
s(:,1)=spm_get_data(P,[i;j;k]);
figure;plot(s);
s(:,1)=spm_get_data(P,[i;j;k]);
hold on;
plot(s(:,2));
characteristics:
- NOISY!!!!
- Highly correlated, spatially, temporally!
- spatial resolution
- temporal resolution
- different sources of variations

Remember, the fluctuation induced by brain activity is few percents => measurement of a small effect size in huge noise
=> need for a LOT of repetition!
=> substractive approach