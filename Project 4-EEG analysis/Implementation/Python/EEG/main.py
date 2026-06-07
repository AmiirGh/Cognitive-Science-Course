# Cognitive Science
# HW4
# Amir Gharghabi
from utils import *

raw = mne.io.read_epochs_eeglab('ICA_c2.set')


stim_types = pd.read_csv('stm_type.csv')
face_ids, nonface_ids, invertedface_ids = get_stim_types_ids(stim_types)

# plot_ERP_all_channels(raw)

faces_epochs_index = []
nonfaces_epochs_index = []
invertedface_epochs_index = []

for id in face_ids:
    faces_epochs_index.append(f'223/{id}/222')

for id in nonface_ids:
    nonfaces_epochs_index.append(f'223/{id}/222')

for id in invertedface_ids:
    invertedface_epochs_index.append(f'223/{id}/222')

fullnonfaces_epochs_index = invertedface_epochs_index + nonfaces_epochs_index



channel_name = 'P7'
plot_P7_datas(raw, channel_name)

raw.pick_channels([channel_name])

face_epochs_subset = raw[np.isin(raw.events[:, -1], [raw.event_id[event] for event in faces_epochs_index])]
nonface_epochs_subset = raw[np.isin(raw.events[:, -1], [raw.event_id[event] for event in nonfaces_epochs_index])]
invertedface_epochs_subset = raw[np.isin(raw.events[:, -1], [raw.event_id[event] for event in invertedface_epochs_index])]
fullnonface_epochs_subset = raw[np.isin(raw.events[:, -1], [raw.event_id[event] for event in fullnonfaces_epochs_index])]


# Plots Face, NonFace and Inverted Face
plot_face_nonface_inverted_face(face_epochs_subset, nonface_epochs_subset, invertedface_epochs_subset, channel_name)

# Plots Face, NonFace and Inverted Face
plot_face_face_nonface(face_epochs_subset, fullnonface_epochs_subset, channel_name)



fmin = 1  # Minimum frequency
fmax = 70  # Maximum frequency
n_fft = 2048  # Number of points along the signal's windowed segments
n_per_seg = 256  # Number of data points in each Welch segment
n_jobs = 1  # Number of CPUs to use simultaneously (here, set to 1)
bandwidth = 2  # Bandwidth of the multitaper windowing function

# Compute the PSD using the multitaper method
fmin = 1  # Minimum frequency
fmax = 70  # Maximum frequency
n_fft = 2048  # Number of points along the signal's windowed segments
n_jobs = 1  # Number of CPUs to use simultaneously (here, set to 1)
bandwidth = 2  # Bandwidth of the multitaper windowing function

# Compute the PSD using the multitaper method
# psds, freqs = mne.time_frequency.psd_array_multitaper(raw, sfreq=256 , fmin=fmin, fmax=fmax, n_jobs=n_jobs, bandwidth=bandwidth)

# Plot the PSD
# mne.viz.plot_psd(psds, freqs)
