import matplotlib.pyplot as plt
import numpy as np
import mne
import pandas as pd


def get_stim_types_ids(stim_types):
    face_ids = []
    Nonface_ids = []
    Invertedface_ids = []
    for i in range(0, 155):
        c = stim_types.iloc[i][0]
        if c == 1:
            face_ids.append(i+1)
        elif c == 0:
            Nonface_ids.append(i+1)
        elif c == -1:
            Invertedface_ids.append(i+1)

    return face_ids, Nonface_ids, Invertedface_ids



def plot_P7_datas(raw, channel_name):

    ch_index = raw.ch_names.index(channel_name)
    erp = raw.copy().pick_channels([channel_name]).average()
    erp.plot()





def plot_ERP_all_channels(raw):
  erp = raw.average()
  erp.plot()




def plot_face_nonface_inverted_face(face_epochs_subset, nonface_epochs_subset, invertedface_epochs_subset, channel):
    faces_erp = face_epochs_subset.average()
    nonfaces_erp = nonface_epochs_subset.average()
    invertedfaces_erp = invertedface_epochs_subset.average()

    faces_se = np.std(face_epochs_subset.get_data(), axis=0) / np.sqrt(len(face_epochs_subset))
    nonfaces_se = np.std(nonface_epochs_subset.get_data(), axis=0) / np.sqrt(len(nonface_epochs_subset))
    invertedfaces_se = np.std(invertedface_epochs_subset.get_data(), axis=0) / np.sqrt(len(invertedface_epochs_subset))

    # Define the time axis
    times = face_epochs_subset.times

    # Calculate confidence intervals
    faces_ci_low = faces_erp.data - 1.96 * faces_se  # Assuming 95% confidence interval
    faces_ci_up = faces_erp.data + 1.96 * faces_se
    nonfaces_ci_low = nonfaces_erp.data - 1.96 * nonfaces_se
    nonfaces_ci_up = nonfaces_erp.data + 1.96 * nonfaces_se
    invertedfaces_ci_low = invertedfaces_erp.data - 1.96 * invertedfaces_se
    invertedfaces_ci_up = invertedfaces_erp.data + 1.96 * invertedfaces_se

    plt.figure(figsize=(12, 6))
    faces_ci_low_1d = faces_ci_low.squeeze()  # Ensure the array is 1-dimensional
    faces_ci_up_1d = faces_ci_up.squeeze()
    nonfaces_ci_low_1d = nonfaces_ci_low.squeeze()
    nonfaces_ci_up_1d = nonfaces_ci_up.squeeze()
    invertedfaces_ci_low_1d = invertedfaces_ci_low.squeeze()
    invertedfaces_ci_up_1d = invertedfaces_ci_up.squeeze()

    # Plot faces ERP with confidence interval
    plt.plot(times, faces_erp.data.T, color='b', label='Faces')
    plt.fill_between(times, faces_ci_low_1d, faces_ci_up_1d, color='b', alpha=0.3)

    # Plot non-faces ERP with confidence interval
    plt.plot(times, nonfaces_erp.data.T, color='g', label='Non-faces')
    plt.fill_between(times, nonfaces_ci_low_1d, nonfaces_ci_up_1d, color='g', alpha=0.3)

    # Plot inverted faces ERP with confidence interval
    plt.plot(times, invertedfaces_erp.data.T, color='r', label='Inverted Faces')
    plt.fill_between(times, invertedfaces_ci_low_1d, invertedfaces_ci_up_1d, color='r', alpha=0.3)

    plt.axvline(x=0, color='k', linestyle='--')
    plt.text(0, -0.05, 'start', color='k', fontsize=9, transform=plt.gca().transAxes)
    plt.axvline(x=0.1, color='darkgreen', linestyle='--')
    plt.text(0.2, -0.05, 'P100', color='darkgreen', fontsize=9, transform=plt.gca().transAxes)
    plt.axvline(x=0.17, color='darkred', linestyle='--')
    plt.text(0.24, -0.05, 'N170', color='darkred', fontsize=9, transform=plt.gca().transAxes)

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('ERPs of channel ' + channel)
    plt.legend()
    plt.grid(True)
    plt.show()




def plot_face_face_nonface(face_epochs_subset, fullnonface_epochs_subset, channel_name):
    faces_erp = face_epochs_subset.average()
    nonfaces_erp = fullnonface_epochs_subset.average()

    faces_se = np.std(face_epochs_subset.get_data(), axis=0) / np.sqrt(len(face_epochs_subset))
    nonfaces_se = np.std(fullnonface_epochs_subset.get_data(), axis=0) / np.sqrt(len(fullnonface_epochs_subset))

    # Define the time axis
    times = face_epochs_subset.times

    # Calculate confidence intervals
    faces_ci_low = faces_erp.data - 1.96 * faces_se  # Assuming 95% confidence interval
    faces_ci_up = faces_erp.data + 1.96 * faces_se
    nonfaces_ci_low = nonfaces_erp.data - 1.96 * nonfaces_se
    nonfaces_ci_up = nonfaces_erp.data + 1.96 * nonfaces_se


    plt.figure(figsize=(12, 6))
    faces_ci_low_1d = faces_ci_low.squeeze()  # Ensure the array is 1-dimensional
    faces_ci_up_1d = faces_ci_up.squeeze()
    nonfaces_ci_low_1d = nonfaces_ci_low.squeeze()
    nonfaces_ci_up_1d = nonfaces_ci_up.squeeze()


    # Plot faces ERP with confidence interval
    plt.plot(times, faces_erp.data.T, color='b', label='Faces')
    plt.fill_between(times, faces_ci_low_1d, faces_ci_up_1d, color='b', alpha=0.3)

    # Plot non-faces ERP with confidence interval
    plt.plot(times, nonfaces_erp.data.T, color='r', label='Non-faces')
    plt.fill_between(times, nonfaces_ci_low_1d, nonfaces_ci_up_1d, color='r', alpha=0.3)

    plt.axvline(x=0, color='k', linestyle='--')
    plt.text(0.1, -0.1, 'start', color='k', fontsize=12, transform=plt.gca().transAxes)
    plt.axvline(x=0.1, color='darkgreen', linestyle='--')
    plt.text(0.2, -0.05, 'P100', color='darkgreen', fontsize=9, transform=plt.gca().transAxes)
    plt.axvline(x=0.17, color='darkred', linestyle='--')
    plt.text(0.24, -0.05, 'N170', color='darkred', fontsize=9, transform=plt.gca().transAxes)

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('ERPs of channel ' + channel_name)
    plt.legend()
    plt.grid(True)
    plt.show()








