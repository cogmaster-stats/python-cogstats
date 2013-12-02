"""
GLM fitting in fMRI
===================

Full step-by-step example of fitting a GLM to experimental data and visualizing
the results.

More specifically:

1. A sequence of fMRI volumes are loaded
2. A design matrix describing all the effects related to the data is computed
3. a mask of the useful brain volume is computed
4. A GLM is applied to the dataset (effect/covariance,
   then contrast estimation)

"""

from os import mkdir, getcwd, path

import numpy as np

import matplotlib.pyplot as plt

from nibabel import save

from nipy.modalities.fmri.glm import FMRILinearModel
from nipy.modalities.fmri.design_matrix import make_dmtx
from nipy.modalities.fmri.experimental_paradigm import \
    load_paradigm_from_csv_file
from nipy.labs.viz import plot_map, cm


#######################################
# Data and analysis parameters
#######################################

# volume mask
# This dataset is large
data_file = 'swrf4d.nii.gz'
paradigm_file = 'stim.csv'

# timing
n_scans = 84
tr = 7

# paradigm
frametimes = np.arange(0,n_scans * tr,tr)
# confounds
hrf_model = 'canonical'
drift_model = "cosine"
hfcut = 128

# write directory
write_dir = path.join(getcwd(), 'results')
if not path.exists(write_dir):
    mkdir(write_dir)

print('Computation will be performed in directory: %s' % write_dir)

########################################
# Design matrix
########################################

print('Loading design matrix...')

paradigm = load_paradigm_from_csv_file(paradigm_file)['0']

design_matrix = make_dmtx(frametimes, paradigm, hrf_model=hrf_model,
                          drift_model=drift_model, hfcut=hfcut)

ax = design_matrix.show()
ax.set_position([.05, .25, .9, .65])
ax.set_title('Design matrix')

plt.savefig(path.join(write_dir, 'design_matrix.png'))

#########################################
# Specify the contrasts
#########################################

# simplest ones
contrasts = {}
n_columns = len(design_matrix.names)

contrasts['audio'] = np.array([1,0,0,0,0,0,0,0,0,0,0])

########################################
# Perform a GLM analysis
########################################

print('Fitting a GLM (this takes time)...')
fmri_glm = FMRILinearModel(data_file, design_matrix.matrix,
                           mask='compute')
fmri_glm.fit(do_scaling=True, model='ar1')

#########################################
# Estimate the contrasts
#########################################

print('Computing contrasts...')
for index, (contrast_id, contrast_val) in enumerate(contrasts.items()):
    print('  Contrast % 2i out of %i: %s' %
          (index + 1, len(contrasts), contrast_id))
    # save the z_image
    image_path = path.join(write_dir, '%s_z_map.nii' % contrast_id)
    z_map, = fmri_glm.contrast(contrast_val, con_id=contrast_id, output_z=True)
    save(z_map, image_path)

    # Create snapshots of the contrasts
    vmax = max(-z_map.get_data().min(), z_map.get_data().max())
    plot_map(z_map.get_data(), z_map.get_affine(),
             cmap=cm.cold_hot, vmin=-vmax, vmax=vmax,
             slicer='z', black_bg=True, threshold=2.5,
             title=contrast_id)
    plt.savefig(path.join(write_dir, '%s_z_map.png' % contrast_id))

print("All the  results were witten in %s" % write_dir)

plt.show()
