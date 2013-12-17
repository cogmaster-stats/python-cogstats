"""
Cluster-size permutation in fMRI
=================================

Here we do a cluster-size analysis: we are going to find a threshold for
the size of clusters. Clusters that are found to be smaller than that
threshold are deemed non significant.

To find the threshold, we need to do a permutation: we randomly shuffle
the two conditions that we are interested in, which gives a sampling of
the null hypothesis. We can then set the threshold on cluster size as the
95 percentile of this distribution.
"""

import numpy as np
import matplotlib.pyplot as plt

import nibabel

from nipy.modalities.fmri.glm import FMRILinearModel
from nipy.modalities.fmri.design_matrix import make_dmtx
from nipy.modalities.fmri.experimental_paradigm import \
    load_paradigm_from_csv_file
from nipy.labs.viz import plot_map, cm


#######################################
# Data and analysis parameters
#######################################

# timing
n_scans = 128
tr = 2.4
# paradigm
frametimes = np.linspace(0.5 * tr, (n_scans - .5) * tr, n_scans)

fmri_data = nibabel.load('s12069_swaloc1_corr.nii.gz')

########################################
# Design matrix
########################################

paradigm = load_paradigm_from_csv_file('localizer_paradigm.csv')['0']

design_matrix = make_dmtx(frametimes, paradigm,
                          hrf_model='canonical with derivative',
                          drift_model="cosine", hfcut=128)

#########################################
# Specify the contrasts
#########################################

# simplest ones
contrasts = {}
n_columns = len(design_matrix.names)
for i in range(paradigm.n_conditions):
    contrasts['%s' % design_matrix.names[2 * i]] = np.eye(n_columns)[2 * i]

# Our contrast of interest
reading_vs_visual = contrasts["phrasevideo"] - contrasts["damier_H"]

########################################
# Perform a GLM analysis on H1
########################################

fmri_glm = FMRILinearModel(fmri_data,
                           design_matrix.matrix, mask='compute')
fmri_glm.fit(do_scaling=True, model='ar1')

# Estimate the contrast
z_map, = fmri_glm.contrast(reading_vs_visual, output_z=True)

# Plot the contrast
vmax = max(-z_map.get_data().min(), z_map.get_data().max())
plot_map(z_map.get_data(), z_map.get_affine(),
            cmap=cm.cold_hot, vmin=-vmax, vmax=vmax,
            slicer='z', black_bg=True, threshold=2.5,
            title='Reading vs visual')

# Count all the clusters for |Z| > 2.5
Z = z_map.get_data()
from scipy import ndimage
cluster_map, n_clusters = ndimage.label(np.abs(Z) > 2.5)
cluster_sizes = np.bincount(cluster_map.ravel())[1:]

print "Cluster sizes:"
print np.sort(cluster_sizes)

mask = fmri_glm.mask

########################################
# Perform GLM analysis on H0 (permuted)
########################################
cluster_sizes_h0 = list()
conditions_to_permute = np.logical_or(paradigm.con_id == 'damier_H',
                                      paradigm.con_id == 'phrasevideo')

for i in range(100):
    permuted_cond = paradigm.con_id[conditions_to_permute]
    np.random.shuffle(permuted_cond)
    paradigm.con_id[conditions_to_permute] = permuted_cond

    design_matrix = make_dmtx(frametimes, paradigm,
                            hrf_model='canonical with derivative',
                            drift_model="cosine", hfcut=128)

    # simplest ones
    contrasts = {}
    n_columns = len(design_matrix.names)
    for i in range(paradigm.n_conditions):
        contrasts['%s' % design_matrix.names[2 * i]] = np.eye(n_columns)[2 * i]

    # Our contrast of interest
    reading_vs_visual = contrasts["phrasevideo"] - contrasts["damier_H"]

    fmri_glm = FMRILinearModel(fmri_data,
                            design_matrix.matrix, mask=mask)
    fmri_glm.fit(do_scaling=True, model='ar1')

    # Estimate the contrast
    z_map, = fmri_glm.contrast(reading_vs_visual, output_z=True)

    Z = z_map.get_data()
    cluster_map, n_clusters = ndimage.label(np.abs(Z) > 2.5)
    cluster_sizes_h0.append(np.bincount(cluster_map.ravel())[1:])


# Plot the contrast under permutation
plot_map(z_map.get_data(), z_map.get_affine(),
            cmap=cm.cold_hot, vmin=-vmax, vmax=vmax,
            slicer='z', black_bg=True, threshold=2.5,
            title='Permuted')


########################################
# Conclude on the threshold
########################################

cluster_sizes_h0 = np.concatenate(cluster_sizes_h0)
cluster_sizes_h0.sort()
threshold = cluster_sizes_h0[int(.95*(len(cluster_sizes_h0)))]
print "Percentile 95 for cluster size under permutation:", threshold

plt.show()
