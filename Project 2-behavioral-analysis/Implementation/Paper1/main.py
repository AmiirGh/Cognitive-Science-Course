# Main file of stimulating paper 1 results
# Student
    # Amir Gharghabi
    # 810102217

from utils import *
# condition 1: (A1, B) (1, 3)
# condition 2: (A2, C) (2, 4)
# A1 = A2 = N(64, 13)
# A1 = A2 = N(64, 13)
# B       = N(54, 13)
# C       = N(44, 13)
    
learning_df_p, estimate_df_p, transfer_df_p = read_csv_files_to_df('p')
learning_df_c, estimate_df_c, transfer_df_c = read_csv_files_to_df('c')

adv_rates_leaning_p, adv_rates_leaning_mean_p, adv_rates_leaning_var_p, t_stat_leaning_p, p_value_leaning_p = get_advantage_rate_var(learning_df_p, 300)
adv_rates_leaning_c, adv_rates_leaning_mean_c, adv_rates_leaning_var_c, t_stat_leaning_c, p_value_leaning_c = get_advantage_rate_var(learning_df_c, 300)
P_value_leaning_p_c, t_test_leaning_p_c = compare_performance_p_c(adv_rates_leaning_c, adv_rates_leaning_p)
print("Partial Group (p) in learning phase:")
print("Mean advantage rate in learning rate:", adv_rates_leaning_mean_p)
print("Variance of advantage rates in learning rate:", adv_rates_leaning_var_p)
print("T-statistic value in learning rate:", t_stat_leaning_p)
print("P-value in learning rate:", p_value_leaning_p)

print("\nComplete Group (c) in learning phase:")
print("Mean advantage rate in learning rate:", adv_rates_leaning_mean_c)
print("Variance of advantage rates in learning rate:", adv_rates_leaning_var_c)
print("T-statistic value in learning rate:", t_stat_leaning_c)
print("P-value in learning rate:", p_value_leaning_c)

print("Comparison between partial and complete performances in learning rate")
print("T-statistic value:", t_test_leaning_p_c)
print("P-value:", P_value_leaning_p_c)


adv_rates_transfer_p, adv_rates_transfer_mean_p, adv_rates_transfer_var_p, t_stat_transfer_p, p_value_transfer_p = get_advantage_rate_var_transfer(transfer_df_p, 24)
adv_rates_transfer_c, adv_rates_transfer_mean_c, adv_rates_transfer_var_c, t_stat_transfer_c, p_value_transfer_c = get_advantage_rate_var_transfer(transfer_df_c, 24)
P_value_transfer_p_c, t_test_transfer_p_c = compare_performance_p_c(adv_rates_transfer_c, adv_rates_transfer_p)
print("Partial Group (p) in transfer phase:")
print("Mean advantage rate in transfer rate:", adv_rates_transfer_mean_p)
print("Variance of advantage rates in transfer rate:", adv_rates_transfer_var_p)
print("T-statistic value in transfer rate:", t_stat_transfer_p)
print("P-value in transfer rate:", p_value_transfer_p)

print("\nComplete Group (c)in transfer phase:")
print("Mean advantage rate in transfer rate:", adv_rates_transfer_mean_c)
print("Variance of advantage rates in transfer rate:", adv_rates_transfer_var_c)
print("T-statistic value in transfer rate:", t_stat_transfer_c)
print("P-value in transfer rate:", p_value_transfer_c)

print("Comparison between partial and complete performances in transfer phase:")
print("T-statistic value:", t_test_transfer_p_c)
print("P-value:", P_value_transfer_p_c)



adv_confidence_mean_p, adv_confidence_var_p, nonadv_confidence_mean_p, nonadv_confidence_var_p = get_adv_nonadv_confidence(transfer_df_p, 24)
adv_confidence_mean_c, adv_confidence_var_c, nonadv_confidence_mean_c, nonadv_confidence_var_c = get_adv_nonadv_confidence(transfer_df_c, 24)
print("Partial Group (p) in transfer phase:")
print("Advantages confidence mean", adv_confidence_mean_p)
print("Advantages confidence var", adv_confidence_var_p)
print("Non-Advantages confidence mean", nonadv_confidence_mean_p)
print("Non-Advantages confidence var", adv_confidence_var_p)

print("\nComplete Group (c)in transfer phase:")
print("Advantages confidence mean", adv_confidence_mean_c)
print("Advantages confidence var", adv_confidence_var_c)
print("Non-Advantages confidence mean", nonadv_confidence_mean_c)
print("Non-Advantages confidence var", nonadv_confidence_var_c)





#______________________ESTIMATION Phase_________________________
A1_A2_P_value_p, A1_A2_t_stat_p = get_P_value_A1_A2_est(estimate_df_p)
A1_A2_P_value_c, A1_A2_t_stat_c = get_P_value_A1_A2_est(estimate_df_c)
print(A1_A2_P_value_p)
print(A1_A2_t_stat_p)
print(A1_A2_P_value_c)
print(A1_A2_t_stat_c)


A1_mean_p, A1_var_p, A2_mean_p, A2_var_p, B_mean_p, B_var_p, C_mean_p, C_var_p = calc_mean_var_estimation(estimate_df_p)
A1_mean_c, A1_var_c, A2_mean_c, A2_var_c, B_mean_c, B_var_c, C_mean_c, C_var_c = calc_mean_var_estimation(estimate_df_c)
lp = [A1_var_p, A2_var_p, B_var_p, C_var_p]
lc = [A1_var_c, A2_var_c, B_var_c, C_var_c]
t_stat, p_value = stats.ttest_rel(lp, lc)






# rates
A1_rate_p, A2_rate_p, B_rate_p, C_rate_p = get_rate(transfer_df_p)
A1_rate_c, A2_rate_c, B_rate_c, C_rate_c = get_rate(transfer_df_c)


# NOT completed, bomb
A1_choice_rate_p, A2_choice_rate_p = get_choice_rate_all_iters(transfer_df_p)
A1_choice_rate_c, A2_choice_rate_c = get_choice_rate_all_iters(transfer_df_c)
iternum = 1
get_choice_rate_P_values(transfer_df_p, 24, iternum)

print("Partial A1 choice rate",  A1_choice_rate_p)
print("Partial A2 choice rate",  A2_choice_rate_p)
print("Complete A1 choice rate", A1_choice_rate_c)
print("Complete A2 choice rate", A2_choice_rate_c)




# # Mean and variances in estimations
A1_mean_p, A1_var_p, A2_mean_p, A2_var_p, B_mean_p, B_var_p, C_mean_p, C_var_p = calc_mean_var_estimation(estimate_df_p)
A1_mean_c, A1_var_c, A2_mean_c, A2_var_c, B_mean_c, B_var_c, C_mean_c, C_var_c = calc_mean_var_estimation(estimate_df_c)

# # Confidences
A1_conf_p, A2_conf_p, B_conf_p, C_conf_p, A1_conf_c, A2_conf_c, B_conf_c, C_conf_c = get_conf(transfer_df_p, transfer_df_c)



#____________________________________________PLOTS________________________________________________
figure2_plots(A1_choice_rate_p, A2_choice_rate_p, A1_choice_rate_c, A2_choice_rate_c,
              A1_mean_p, A1_var_p, A2_mean_p, A2_var_p, B_mean_p, B_var_p, C_mean_p, C_var_p,
              A1_mean_c, A1_var_c, A2_mean_c, A2_var_c, B_mean_c, B_var_c, C_mean_c, C_var_c)


figure3_plots(transfer_df_p, transfer_df_c, estimate_df_p, estimate_df_c, learning_df_p, learning_df_c)










