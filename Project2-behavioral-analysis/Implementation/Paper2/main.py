# Main file of stimulating paper 1 results
# Student
    # Amir Gharghabi
    # 810102217

from utils import *

data = read_csv_files_to_df()
data = data[data['session'].isin([1, 3, 6])]

results_utility_E_V = estimate_parameters_E_V(data, likelihood_E_V)  # The estimate alpha and beta for all participants
                                                                     # in the sessions 1, 3, 5 and all together
                                                                     # Utility function E and V


results_utility_rho = estimate_parameters_rho(data, likelihood_rho)  # The estimate rho and beta for all participants
                                                                     # in the sessions 1, 3, 5 and all together
                                                                     # Utility rho (exponential)


acc_E_V = get_utility_E_V_accuracy(data, results_utility_E_V)
acc_rho = get_utility_rho_accuracy(data, results_utility_rho)

print(f"E_V utility function accuracy is:  {acc_E_V}")
print(f"Exponential utility function accuracy is: {acc_rho}")




