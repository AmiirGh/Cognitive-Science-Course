from matplotlib import pyplot as plt
from brian2 import *
import numpy as np


def plot_Figure3_A(SME1, SME2, subN, R1, R2, E1, E2):
    fig, axs = plt.subplots(4, 1, sharex=True, layout='constrained', gridspec_kw={'height_ratios': [3, 3, 3, 3]})
    fig.suptitle('Trial 1', fontsize=16, fontweight='bold')

    axs[0].plot(SME2.t / ms, SME2.i, '.', markersize=2, color='black')
    axs[0].set(ylabel='Neural group A')
    axs[0].set_yticklabels([])
    axs[0].axvline(x=-1, color='b', linewidth=3)

    axs[1].plot(SME1.t / ms, SME1.i, '.', markersize=2, color='black')
    axs[1].set(ylabel='Neural group B')
    axs[1].set_yticklabels([])
    axs[1].axvline(x=-1, color='r', linewidth=3)

    axs[2].plot(R1.t / ms, R1.smooth_rate(window='flat', width=100 * ms) / Hz, color='darkred')
    axs[2].plot(R2.t / ms, R2.smooth_rate(window='flat', width=100 * ms) / Hz, color='darkblue')
    axs[2].set_yticklabels([])
    axs[2].set_xticklabels([])
    axs[2].set(ylabel='Firing rate')

    axs[3].plot(E1.t / ms, E1.rates[0] / Hz, color='darkred')
    axs[3].plot(E2.t / ms, E2.rates[0] / Hz, color='darkblue')
    axs[3].set_yticklabels([])
    axs[3].set(ylabel='Input', xlabel='Time(s)', xticklabels=[0, 1, 2 ,3, 4, 5, 6, 7, 8])

    fig.align_ylabels(axs)

    plt.show()

    # plt.plot(R2.t / ms, R1.t / ms, label='R2.t vs R1.t')
    # plt.scatter(SME2.t[R2.t > 0] / ms, R1.t[R2.t > 0] / ms, color='black', label='SME2')  # Plot time-aligned SME2 points
    # plt.scatter(SME1.t[R2.t > 0] / ms, R1.t[R2.t > 0] / ms, color='red', label='SME1')  # Plot time-aligned SME1 points
    # plt.legend()  # Show legend
    # plt.xlabel('R2.t / ms')
    # plt.ylabel('R1.t / ms')
    # plt.title('R2.t vs R1.t with SME1 and SME2 points')
    # plt.show()
