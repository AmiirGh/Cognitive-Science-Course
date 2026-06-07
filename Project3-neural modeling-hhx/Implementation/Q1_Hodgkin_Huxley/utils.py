import numpy as np
import matplotlib.pyplot as plt

def get_alpha_n(V):
    return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))

def get_alpha_m(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))

def get_alpha_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)

def get_beta_n(V):
    return 0.125 * np.exp(-(V + 65.0) / 80.0)

def get_beta_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)

def get_beta_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))


def plot_gNa_gK(time, gNa_trace, gK_trace):
    plt.figure(figsize=(8, 3))
    plt.plot(time, gNa_trace, label='gNa')
    plt.plot(time, gK_trace, label='gK')
    plt.title('gNa and gK diagrams')
    plt.ylabel('')
    plt.xlabel('Time (ms)')
    plt.legend()
    plt.show()

def plot_m_h_n(time, m_trace, h_trace, n_trace):
    plt.plot(time, m_trace, label='m(sodium activation)')
    plt.plot(time, h_trace, label='h(sodium deactivation)')
    plt.plot(time, n_trace, label='n(potassium activation)')
    plt.title('Gating Variables')
    plt.ylabel('Gating Value')
    plt.xlabel('Time (ms)')
    plt.legend()

def plot_INa_IK_IL(time, INa_trace, IK_trace, IL_trace):
    plt.plot(time, INa_trace, label='Na channel current')
    plt.plot(time, IK_trace, label='K channel current')
    plt.plot(time, IL_trace, label='L channel current')
    plt.title('Channel currents')
    plt.ylabel('I (uA/cm^2)')
    plt.xlabel('Time (ms)')
    plt.legend()



def plot_hh_model(time, V_trace, I_inj_array, m_trace, h_trace, n_trace, gNa_trace, gK_trace, INa_trace, IK_trace, IL_trace):
    # Plotting
    plot_gNa_gK(time, gNa_trace, gK_trace)


    plt.figure(figsize=(12, 8))

    plt.subplot(4, 1, 1)
    plt.plot(time, V_trace, label='Membrane Potential (V)')
    plt.title('Hodgkin-Huxley Model')
    plt.ylabel('Membrane Potential (mV)')
    plt.xlabel('Time (ms)')
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(time, I_inj_array, label='I (current)', color='red')
    plt.title('Injected Current')
    plt.ylabel('I (uA/cm^2)')
    plt.xlabel('Time (ms)')

    plt.subplot(4, 1, 3)
    plot_m_h_n(time, m_trace, h_trace, n_trace)
    plt.subplot(4, 1, 4)
    plot_INa_IK_IL(time, INa_trace, IK_trace, IL_trace)

    plt.tight_layout()
    plt.show()








def plot_min_current_vs_duration():
    durations = [0.2, 0.5, 0.7, 1, 1.5, 2]
    I_min_threshold = [34, 13, 10, 7, 5, 4]
    plt.plot(durations, I_min_threshold, 'b-')  # Plot the line in blue
    plt.plot(durations, I_min_threshold, 'ro')  # Plot the points in red
    plt.title('Minimum current vs Time duration')
    plt.ylabel('I_min (uA/cm^2)')
    plt.xlabel('Duration (ms)')
    plt.xticks(durations)  # Set x-axis ticks to the duration values
    plt.yticks(I_min_threshold)  # Set y-axis ticks to the I_min_threshold values
    plt.show()

