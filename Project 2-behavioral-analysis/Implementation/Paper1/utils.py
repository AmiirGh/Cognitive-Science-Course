import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
def read_csv_files_to_df(expType):
    if expType == 'p':
        learning_file_path = 'Paper1_data_python/Partial/Partial_table_learning.csv'
        estimate_file_path = 'Paper1_data_python/Partial/Partial_table_estimate.csv'
        transfer_file_path = 'Paper1_data_python/Partial/Partial_table_transfer.csv'
        learning_df = pd.read_csv(learning_file_path)
        estimate_df = pd.read_csv(estimate_file_path)
        transfer_df = pd.read_csv(transfer_file_path)
    elif expType == 'c':
        learning_file_path = 'Paper1_data_python/Complete/Complete_table_learning.csv'
        estimate_file_path = 'Paper1_data_python/Complete/Complete_table_estimate.csv'
        transfer_file_path = 'Paper1_data_python/Complete/Complete_table_transfer.csv'
        learning_df = pd.read_csv(learning_file_path)
        estimate_df = pd.read_csv(estimate_file_path)
        transfer_df = pd.read_csv(transfer_file_path)
    return learning_df, estimate_df, transfer_df



def calculate_adv_rate(chunk, learning_df_p):
    filtered_chunk = chunk[(chunk['stimLeft'] != 0) & (chunk['stimRight'] != 0)]
    filtered_chunk['is_adv'] = (
                filtered_chunk[['stimLeft', 'stimRight']].min(axis=1) == filtered_chunk['chosen']).astype(int)
    # filtered_chunk = filtered_chunk[filtered_chunk['is_adv'] == 1]  # filter by chosen stimulus
    adv_rate = filtered_chunk['is_adv'].mean()
    return adv_rate

def get_advantage_rate_var(learning_df, chunk_size):
    num_chunks = len(learning_df) // chunk_size + (len(learning_df) % chunk_size > 0)
    chunks = [learning_df[i * chunk_size:(i + 1) * chunk_size] for i in
              range(num_chunks)]

    adv_rates = [calculate_adv_rate(chunk, learning_df) for chunk in chunks]
    adv_rates_mean = np.mean(adv_rates)
    adv_rates_var = np.var(adv_rates)
    t_stat, p_value = stats.ttest_ind(adv_rates, [0.5] * len(adv_rates))

    return adv_rates, adv_rates_mean, math.sqrt(adv_rates_var), t_stat, p_value
def compare_performance_p_c(adv_rates_p, adv_rates_c):
    t_stat, p_value = stats.ttest_ind(adv_rates_p, adv_rates_c, equal_var=False)
    return p_value, t_stat



def calculate_adv_rate_transfer(chunk):
    filtered_chunk = chunk[(chunk['stimLeft'] != 0) & (chunk['stimRight'] != 0)]
    filtered_chunk['is_adv'] = (
                filtered_chunk[['stimLeft', 'stimRight']].min(axis=1) == filtered_chunk['chosen']).astype(int)
    # filtered_chunk = filtered_chunk[filtered_chunk['is_adv'] == 1]  # filter by chosen stimulus
    filtered_chunk.loc[filtered_chunk['chosen'] == 2, 'is_adv'] = 1
    adv_rate = filtered_chunk['is_adv'].mean()
    return adv_rate
def get_advantage_rate_var_transfer(learning_df, chunk_size):
    num_chunks = len(learning_df) // chunk_size + (len(learning_df) % chunk_size > 0)
    chunks = [learning_df[i * chunk_size:(i + 1) * chunk_size] for i in
              range(num_chunks)]

    adv_rates = [calculate_adv_rate_transfer(chunk) for chunk in chunks]
    adv_rates_mean = np.mean(adv_rates)
    adv_rates_var = np.var(adv_rates)
    t_stat, p_value = stats.ttest_ind(adv_rates, [0.5] * len(adv_rates))

    return adv_rates, adv_rates_mean, math.sqrt(adv_rates_var), t_stat, p_value



def calculate_confidence_mean_adv(chunk):
    filtered_chunk = chunk[(chunk['stimLeft'] != 0) & (chunk['stimRight'] != 0)]
    filtered_chunk['is_adv'] = (
            filtered_chunk[['stimLeft', 'stimRight']].min(axis=1) == filtered_chunk['chosen']).astype(int)
    filtered_chunk.loc[filtered_chunk['chosen'] == 2, 'is_adv'] = 1
    filtered_chunk = filtered_chunk[filtered_chunk['is_adv'] == 1]  # filter by chosen stimulus
    adv_rate = filtered_chunk['conf'].mean()
    return adv_rate
def calculate_confidence_mean_nonadv(chunk):
    filtered_chunk = chunk[(chunk['stimLeft'] != 0) & (chunk['stimRight'] != 0)]
    filtered_chunk['is_nonadv'] = (
                filtered_chunk[['stimLeft', 'stimRight']].min(axis=1) != filtered_chunk['chosen']).astype(int)
    filtered_chunk.loc[filtered_chunk['chosen'] == 2, 'is_nonadv'] = 0
    filtered_chunk = filtered_chunk[filtered_chunk['is_nonadv'] == 1]  # filter by chosen stimulus
    nonadv_rate = filtered_chunk['conf'].mean()
    return nonadv_rate
def get_adv_nonadv_confidence(transfer_df, chunk_size):
    num_chunks = len(transfer_df) // chunk_size + (len(transfer_df) % chunk_size > 0)
    chunks = [transfer_df[i * chunk_size:(i + 1) * chunk_size] for i in
              range(num_chunks)]

    adv_confidence_means = [calculate_confidence_mean_adv(chunk) for chunk in chunks]
    nonadv_confidence_means = [calculate_confidence_mean_nonadv(chunk) for chunk in chunks if not math.isnan(calculate_confidence_mean_nonadv(chunk))]

    adv_confidence_mean = np.mean(adv_confidence_means)
    nonadv_confidence_mean = np.mean(nonadv_confidence_means)
    adv_confidence_var = np.var(adv_confidence_means)
    nonadv_confidence_var = np.var(nonadv_confidence_means)

    return adv_confidence_mean, math.sqrt(adv_confidence_var), nonadv_confidence_mean, nonadv_confidence_var










def get_rate(transfer_df):
    chosen_A1_df = transfer_df[transfer_df['chosen'] == 1]
    chosen_A2_df = transfer_df[transfer_df['chosen'] == 2]
    chosen_B_df = transfer_df[transfer_df['chosen'] == 3]
    chosen_C_df = transfer_df[transfer_df['chosen'] == 4]

    A1_rate = len(chosen_A1_df) / (len(chosen_A1_df) + len(chosen_B_df))
    B_rate  = len(chosen_B_df)  / (len(chosen_A1_df) + len(chosen_B_df))
    A2_rate = len(chosen_A2_df) / (len(chosen_A2_df) + len(chosen_C_df))
    C_rate  = len(chosen_C_df)  / (len(chosen_A2_df) + len(chosen_C_df))

    return A1_rate, A2_rate, B_rate, C_rate
def get_choice_rate_all_iters(transfer_df):
    filtered_df = transfer_df[((transfer_df['stimLeft'] == 1) | (transfer_df['stimLeft'] == 2)) &
                                  ((transfer_df['stimRight'] == 1) | (transfer_df['stimRight'] == 2))]
    chosen_A1_df = filtered_df[filtered_df['chosen'] == 1]
    chosen_A2_df = filtered_df[filtered_df['chosen'] == 2]
    A1_choice_rate = len(chosen_A1_df) / (len(chosen_A1_df) + len(chosen_A2_df))
    A2_choice_rate = len(chosen_A2_df) / (len(chosen_A1_df) + len(chosen_A2_df))

    return A1_choice_rate, A2_choice_rate
def get_choice_rate_P_values(transfer_df, chunk_size, iternum):
    num_chunks = len(transfer_df) // chunk_size + (len(transfer_df) % chunk_size > 0)
    chunks = [transfer_df[i * chunk_size:(i + 1) * chunk_size] for i in
              range(num_chunks)]
    filtered_chunks = []
    for chunk in chunks:
        filtered_chunks.append(chunk.head(iternum * 6))

    A1_rates = []
    A2_rates = []
    for filtered_chunk in filtered_chunks:
        A1_rate, A2_rate = get_choice_rate_all_iters(filtered_chunk)
        A1_rates.append(A1_rate)
        A2_rates.append(A2_rate)

    t = 2
    return 1 # TEMPORARY



# Amir bomb   this function generates significant resulst for partial
def get_P_value_A1_A2_est(estimate_df):
    A1_estimate = estimate_df[estimate_df['stim'] == 1]['estimate']
    A2_estimate = estimate_df[estimate_df['stim'] == 2]['estimate']

    # Perform a paired t-test
    t_stat, p_value = stats.ttest_rel(A1_estimate, A2_estimate)

    return p_value, t_stat




def get_conf(transfer_df_p, transfer_df_c):
    chosen_A1_df_p = transfer_df_p[transfer_df_p['chosen'] == 1]
    chosen_A2_df_p = transfer_df_p[transfer_df_p['chosen'] == 2]
    chosen_B_df_p = transfer_df_p[transfer_df_p['chosen'] == 3]
    chosen_C_df_p = transfer_df_p[transfer_df_p['chosen'] == 4]

    chosen_A1_df_c = transfer_df_c[transfer_df_c['chosen'] == 1]
    chosen_A2_df_c = transfer_df_c[transfer_df_c['chosen'] == 2]
    chosen_B_df_c = transfer_df_c[transfer_df_c['chosen'] == 3]
    chosen_C_df_c = transfer_df_c[transfer_df_c['chosen'] == 4]

    A1_conf_p = chosen_A1_df_p['conf'].mean()
    A2_conf_p = chosen_A2_df_p['conf'].mean()
    B_conf_p  = chosen_B_df_p['conf'].mean()
    C_conf_p  = chosen_C_df_p['conf'].mean()
    A1_conf_c = chosen_A1_df_c['conf'].mean()
    A2_conf_c = chosen_A2_df_c['conf'].mean()
    B_conf_c  = chosen_B_df_c['conf'].mean()
    C_conf_c  = chosen_C_df_c['conf'].mean()


    return  A1_conf_p, A2_conf_p, B_conf_p, C_conf_p, A1_conf_c, A2_conf_c, B_conf_c, C_conf_c
def calc_mean_var_estimation(estimate_df):
    A1_df = estimate_df[estimate_df['stim'] == 1]
    A2_df = estimate_df[estimate_df['stim'] == 2]
    B_df  = estimate_df[estimate_df['stim'] == 3]
    C_df  = estimate_df[estimate_df['stim'] == 4]

    A1_mean = np.mean(A1_df['estimate'])
    A1_var  = np.var(A1_df['estimate'])
    A2_mean = np.mean(A2_df['estimate'])
    A2_var  = np.var(A2_df['estimate'])
    B_mean  = np.mean(B_df['estimate'])
    B_var   = np.var(B_df['estimate'])
    C_mean  = np.mean(C_df['estimate'])
    C_var   = np.var(C_df['estimate'])

    return A1_mean, A1_var, A2_mean, A2_var, B_mean, B_var, C_mean, C_var
def plot_choice_rates(A1_choice_rate_p, A2_choice_rate_p, A1_choice_rate_c, A2_choice_rate_c):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.bar(['A1', 'A2'], [A1_choice_rate_p, A2_choice_rate_p],
            color=['#49D113', '#205A09'], width=[0.4, 0.4])
    ax1.set_title('Partial Experiment')
    ax1.set_xlabel('Action')
    ax1.set_ylabel('Choice Rate')
    ax1.set_yticks([0, 0.5, 1])  # Set y-ticks

    ax2.bar(['A1', 'A2'], [A1_choice_rate_c, A2_choice_rate_c],
            color=['#C97C06', '#833707'], width=[0.4, 0.4])
    ax2.set_title('Complete Experiment')
    ax2.set_xlabel('Action')
    ax2.set_ylabel('Choice Rate')
    ax2.set_yticks([0, 0.5, 1])  # Set y-ticks

    plt.subplots_adjust(wspace=0.4)
    plt.show()
def plot_normal_distribution(mean, var, label, color, ax):
    var = var**2
    x = np.linspace(0, 100, 200)
    # y = (1 / np.sqrt(2 * np.pi * var)) * \
    #     np.exp(-(x - mean) ** 2 / (2 * var))
    # ax.plot(x, y, label=label, color=color)
    # x = np.linspace(mean - 3 * np.sqrt(var), mean + 3 * np.sqrt(var), 100)
    y = (1 / np.sqrt(2 * np.pi * var)) * np.exp(-(x - mean) ** 2 / (2 * var))
    ax.plot(x, y, label=label, color=color, linewidth=3)
def plot_normal_distributions(A1_mean, A1_var, A2_mean, A2_var, B_mean, B_var, C_mean, C_var, expType):
    if expType == 'p':
        colors = ['0', '#33980B', '#1F5B07', '#49D113', '#66F8A2']
    else:
        colors = ['0', '#BF7402', '#4C2F03', '#FE9900', '#FEBF60']
    # The normal distribution plots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].set_title('')
    plot_normal_distribution(A1_mean, A1_var, 'A1', colors[1], axs[0])
    plot_normal_distribution(B_mean, B_var, 'B', colors[3], axs[0])
    axs[0].set_xlabel('Value')
    axs[0].set_ylabel('choice rate')
    axs[0].legend()

    # Plot A2 and C in the right subplot
    axs[1].set_title('')
    plot_normal_distribution(A2_mean, A2_var, 'A2', colors[2], axs[1])
    plot_normal_distribution(C_mean, C_var, 'C', colors[4], axs[1])
    axs[1].set_xlabel('Value')
    axs[1].set_ylabel('choice rate')
    axs[1].legend()

    plt.tight_layout()
    plt.show()


def figure2_plots(A1_choice_rate_p, A2_choice_rate_p, A1_choice_rate_c, A2_choice_rate_c,
                  A1_mean_p, A1_var_p, A2_mean_p, A2_var_p, B_mean_p, B_var_p, C_mean_p, C_var_p,
                  A1_mean_c, A1_var_c, A2_mean_c, A2_var_c, B_mean_c, B_var_c, C_mean_c, C_var_c):

    plot_choice_rates(A1_choice_rate_p, A2_choice_rate_p, A1_choice_rate_c, A2_choice_rate_c)

    # Estimated values
    # plot_normal_distributions(A1_mean_p, math.sqrt(A1_var_p), A2_mean_p, math.sqrt(A2_var_p), B_mean_p, math.sqrt(B_var_p), C_mean_p, math.sqrt(C_var_p), 'p')
    # plot_normal_distributions(A1_mean_c, math.sqrt(A1_var_c), A2_mean_c, math.sqrt(A2_var_c), B_mean_c, math.sqrt(B_var_c), C_mean_c, math.sqrt(C_var_c), 'c')

    # The actual values
    plot_normal_distributions(64, 13, 64, 13, 54, 13, 44, 13, 'p')
    plot_normal_distributions(64, 13, 64, 13, 54, 13, 44, 13, 'c')

########################################################################################################################

def plot_fig3_rate_conf(transfer_df, expType):
    A1_df = transfer_df[transfer_df['chosen'] == 1]
    A2_df = transfer_df[transfer_df['chosen'] == 2]
    B_df  = transfer_df[transfer_df['chosen'] == 3]
    C_df  = transfer_df[transfer_df['chosen'] == 4]
    if expType == 'p':
        colors = ['#12A512', '#014D0A', '#85D702', '#44FF9E']
    else:
        colors = ['#FE9900', '#885303', '#FDB549', '#FED68C']

    mean_values = [A1_df['conf'].mean(), A2_df['conf'].mean(), B_df['conf'].mean(), C_df['conf'].mean()]
    variances = [A1_df['conf'].var(), A2_df['conf'].var(), B_df['conf'].var(), C_df['conf'].var()]
    variances = [x / 100 for x in variances]
    categories = ['A1', 'A2', 'B', 'C']

    plt.figure(figsize=(8, 8))
    A1_rate, A2_rate, B_rate, C_rate = get_rate(transfer_df)
    rates = [A1_rate, A2_rate, B_rate, C_rate]
    plt.subplot(2, 1, 1)
    plt.bar(categories, rates, yerr=np.sqrt(variances), capsize=5, color=colors, alpha=0.7)
    plt.errorbar(categories, rates, yerr=np.sqrt(variances), fmt='none', ecolor='black', elinewidth=4, capsize=5)

    plt.xlabel('Categories')
    plt.ylabel('Rates')
    plt.title('Rates for A1 to C')
    plt.yticks([0, 0.5, 1])
    plt.subplot(2, 1, 2)
    plt.bar(categories, mean_values, yerr=np.sqrt(variances), capsize=5, color=colors, alpha=0.7)
    plt.errorbar(categories, mean_values, yerr=np.sqrt(variances), fmt='none', ecolor='black', elinewidth=4, capsize=5)
    plt.xlabel('Categories')
    plt.ylabel('Confidence')
    plt.title('Confidence Values for A1 to C with Variances')
    plt.yticks([0, 0.5, 1])

    # plt.bar(categories, mean_values, yerr=np.sqrt(variances), capsize=5)
    # plt.xlabel('Categories')
    # plt.ylabel('Mean Confidence')
    # plt.title('Mean Confidence with 95% Confidence Intervals')
    # plt.show()

    plt.tight_layout()
    plt.show()
def plot_fig3_est(estimate_df, expType):
    A1_df = estimate_df[estimate_df['stim'] == 1]
    a1 = len(A1_df)
    A2_df = estimate_df[estimate_df['stim'] == 2]
    a2 = len(A1_df)
    B_df  = estimate_df[estimate_df['stim'] == 3]
    b = len(A1_df)
    C_df  = estimate_df[estimate_df['stim'] == 4]
    c = len(A1_df)
    if expType == 'p':
        colors = ['#12A512', '#014D0A', '#85D702', '#44FF9E']
    else:
        colors = ['#FE9900', '#885303', '#FDB549', '#FED68C']

    mean_values = [A1_df['estimate'].mean(), A2_df['estimate'].mean(), B_df['estimate'].mean(), C_df['estimate'].mean()]
    variances = [A1_df['estimate'].var(), A2_df['estimate'].var(), B_df['estimate'].var(), C_df['estimate'].var()]
    variances = [x / 100 for x in variances]
    categories = ['A1', 'A2', 'B', 'C']

    plt.figure(figsize=(8, 8))

    plt.axhline(y=44, color='grey', linestyle='--', zorder=1)
    plt.axhline(y=54, color='grey', linestyle='--', zorder=0.5)
    plt.axhline(y=64, color='grey', linestyle='--', zorder=1)
    plt.axhline(y=64, xmin=0.03, xmax=0.25, color=colors[0], linewidth=4)
    plt.axhline(y=64, xmin=0.27, xmax=0.49, color=colors[1], linewidth=4)
    plt.axhline(y=54, xmin=0.51, xmax=0.73, color=colors[2], linewidth=4)
    plt.axhline(y=44, xmin=0.75, xmax=0.97, color=colors[3], linewidth=4)

    A1_x_positions = [np.random.uniform(-0.2, 0.2) for _ in range(len(A1_df))]
    plt.scatter(A1_x_positions, A1_df['estimate'], color='gray', s=10, zorder=3)
    A2_x_positions = [np.random.uniform(+0.8, 1.2) for _ in range(len(A2_df))]
    plt.scatter(A2_x_positions, A2_df['estimate'], color='gray', s=10, zorder=3)
    B_x_positions = [np.random.uniform(+1.8, 2.2) for _ in range(len(B_df))]
    plt.scatter(B_x_positions, B_df['estimate'], color='gray', s=10, zorder=3)
    C_x_positions = [np.random.uniform(+2.8, 3.2) for _ in range(len(C_df))]
    plt.scatter(C_x_positions, C_df['estimate'], color='gray', s=10, zorder=3)

    categories = ['A1', 'A2', 'B', 'C']
    plt.bar(categories, mean_values, yerr=np.sqrt(variances), capsize=5, color=colors, alpha=0.7)
    plt.errorbar(categories, mean_values, yerr=np.sqrt(variances), fmt='none', ecolor='black', elinewidth=4, capsize=5)

    plt.xlabel('Categories')
    plt.ylabel('Estimete values')
    plt.title('Estimated Values for A1 to C with Variances')
    plt.yticks([0, 44, 54, 64, 100])



    plt.tight_layout()
    plt.show()
def get_A1_to_C_means_vars(learning_df):
    chunk_size = 300
    num_chunks = len(learning_df) // chunk_size + (len(learning_df) % chunk_size > 0)
    chunks = [learning_df[i * chunk_size:(i + 1) * chunk_size] for i in
              range(num_chunks)]

    A1_choice_rates = []
    A1_choice_rates_means = []
    A1_choice_rates_vars = []
    A2_choice_rates = []
    A2_choice_rates_means = []
    A2_choice_rates_vars = []
    B_choice_rates = []
    B_choice_rates_means = []
    B_choice_rates_vars = []
    C_choice_rates = []
    C_choice_rates_means = []
    C_choice_rates_vars = []
    for i in range(0, 31):
        for chunk in chunks:
            subset_A1 = chunk[10 * i:10 * i + 10]
            subset_A1 = subset_A1[(subset_A1['condition'] == 1)]
            A1_choice_rate = (subset_A1['chosen'] == 1).sum() / len(subset_A1)
            if not np.isnan(A1_choice_rate):
                A1_choice_rates.append(A1_choice_rate)
                B_choice_rates.append(1 - A1_choice_rate)

            subset_A2 = chunk[10 * i:10 * i + 10]
            subset_A2 = subset_A2[(subset_A2['condition'] == 2)]
            A2_choice_rate = (subset_A2['chosen'] == 2).sum() / len(subset_A2)
            if not np.isnan(A2_choice_rate):
                A2_choice_rates.append(A2_choice_rate)
                C_choice_rates.append(1 - A2_choice_rate)

        A1_choice_rates_means.append(np.mean(A1_choice_rates))
        A2_choice_rates_means.append(np.mean(A2_choice_rates))
        B_choice_rates_means.append(np.mean(B_choice_rates))
        C_choice_rates_means.append(np.mean(C_choice_rates))
        A1_choice_rates_vars.append(np.var(A1_choice_rates))
        A2_choice_rates_vars.append(np.var(A2_choice_rates))
        B_choice_rates_vars.append(np.var(B_choice_rates))
        C_choice_rates_vars.append(np.var(C_choice_rates))
        A1_choice_rate = []
        A2_choice_rate = []
        B_choice_rate = []
        C_choice_rate = []
    return (A1_choice_rates_means, A2_choice_rates_means, B_choice_rates_means, C_choice_rates_means,
            A1_choice_rates_vars, A2_choice_rates_vars, B_choice_rates_vars, C_choice_rates_vars)
def plot_choice_rate_conf_interval(learning_df, expType):
    A1_choice_rates_means, A2_choice_rates_means, B_choice_rates_means, C_choice_rates_means,\
    A1_choice_rates_vars, A2_choice_rates_vars, B_choice_rates_vars, C_choice_rates_vars = get_A1_to_C_means_vars(learning_df)

    labels = ['A1,data', 'A2,data', 'B,data', 'C,data']
    if expType == 'p':
        colors = ['0', '#33980B', '#1F5B07', '#49D113', '#66F8A2']
    else:
        colors = ['0', '#BF7402', '#4C2F03', '#FE9900', '#FEBF60']
    means = [A1_choice_rates_means, A2_choice_rates_means, B_choice_rates_means, C_choice_rates_means]
    x = range(len(A1_choice_rates_means))

    fig, axs = plt.subplots(1, 2, figsize=(8, 8))

    # Upper plot for A1 and B
    axs[0].plot(x, A1_choice_rates_means, linestyle='-', color=colors[1], label='A1')
    axs[0].fill_between(x, np.array(A1_choice_rates_means) - np.array(A1_choice_rates_vars),
                        np.array(A1_choice_rates_means) + np.array(A1_choice_rates_vars), alpha=0.3, color=colors[1])

    axs[0].plot(x, B_choice_rates_means, linestyle='-', color=colors[3], label='B')
    axs[0].fill_between(x, np.array(B_choice_rates_means) - np.array(B_choice_rates_vars),
                        np.array(B_choice_rates_means) + np.array(B_choice_rates_vars), alpha=0.3, color=colors[3])

    axs[0].set_xlabel('time (each bin is 10 trials)')
    axs[0].set_ylabel('Choice Rates')
    # axs[0].set_title('Mean Choice Rates for A1 and B')
    axs[0].legend()

    # Lower plot for A2 and C
    axs[1].plot(x, A2_choice_rates_means, linestyle='-', color=colors[2], label='A2')
    axs[1].fill_between(x, np.array(A2_choice_rates_means) - np.array(A2_choice_rates_vars),
                        np.array(A2_choice_rates_means) + np.array(A2_choice_rates_vars), alpha=0.3, color=colors[2])

    axs[1].plot(x, C_choice_rates_means, linestyle='-', color=colors[4], label='C')
    axs[1].fill_between(x, np.array(C_choice_rates_means) - np.array(C_choice_rates_vars),
                        np.array(C_choice_rates_means) + np.array(C_choice_rates_vars), alpha=0.3, color=colors[4])

    axs[1].set_xlabel('time (each bin is 10 trials)')
    # axs[1].set_ylabel('Mean Choice Rates')
    # axs[1].set_title('Mean Choice Rates for A2 and C')
    axs[1].legend()

    plt.tight_layout()
    plt.show()
def figure3_plots(transfer_df_p, transfer_df_c, estimate_df_p, estimate_df_c, learning_df_p, learning_df_c):
    plot_fig3_rate_conf(transfer_df_p, 'p')
    plot_fig3_rate_conf(transfer_df_c, 'c')

    plot_fig3_est(estimate_df_p, 'p')
    plot_fig3_est(estimate_df_c, 'c')

    plot_choice_rate_conf_interval(learning_df_p, 'p')
    plot_choice_rate_conf_interval(learning_df_c, 'c')




