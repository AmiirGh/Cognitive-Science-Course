from scipy.optimize import minimize
import numpy as np
import pandas as pd


def read_csv_files_to_df():
    data_file_path = 'Paper2_data_python/T.csv'
    data_df = pd.read_csv(data_file_path)
    return data_df

def Utility_E_V(params, sure_gain, risk_gain, risk_prob):
    alpha, beta = params
    U_gamble = risk_gain * risk_prob + alpha * (risk_gain ** 2 * risk_prob * (1 - risk_prob))
    U_sure = sure_gain
    return U_gamble, U_sure

def q_gamble_E_V(params, sure_gain, risk_gain, risk_prob):
    alpha, beta = params
    U_g, U_s = Utility_E_V(params, sure_gain, risk_gain, risk_prob)
    return 1 / (1 + np.exp(-beta * (U_g - U_s)))

def likelihood_E_V(params, sure_gain, risk_gain, risk_prob, choices):
    alpha, beta = params
    # U_gamble = risk_gain*risk_prob + alpha * (risk_gain**2 * risk_prob * (1-risk_prob))
    U_g, U_s = Utility_E_V(params, sure_gain, risk_gain, risk_prob)
    q_gamble = 1/(1+np.exp(-beta*(U_g - U_s)))
    log_likelihood = np.sum(choices * np.log(q_gamble) + (1 - choices) * np.log(1 - q_gamble))
    return -log_likelihood


def estimate_parameters_E_V(data, likelihood_E_V):
    participant_sessions = []

    for participant in range(65, 97):
        for session in [1, 3, 6, '1+3+5']:  # Iterate over sessions (1, 3, 5 and all three sessions)
            if session != '1+3+5':
                data2 = data[(data['participant'] == participant) & (data['session'] == session)]
            else:
                data2 = data[data['participant'] == participant]

            if not data2.empty:
                sure_gain = data2['sure_gain'].values
                risk_gain = data2['risk_gain'].values
                risk_prob = data2['risk_prob'].values
                choices = data2['chosen'].values

                initial_params = np.array([0, 0])

                res = minimize(likelihood_E_V, initial_params, args=(sure_gain, risk_gain, risk_prob, choices), method='L-BFGS-B')

                alpha, beta = res.x

                if session == 6:
                    session = 5
                participant_sessions.append({'participant': participant, 'session': session, 'alpha': alpha, 'beta': beta})
            else:
                participant_sessions.append({'participant': participant, 'session': session, 'alpha': np.nan, 'beta': np.nan})

    result_df = pd.DataFrame(participant_sessions)
    return result_df


















def Utility_rho(params, sure_gain, risk_gain, risk_prob):
    rho, beta = params
    U_gamble = risk_prob * (risk_gain**rho)
    U_sure = (1-risk_prob) * (sure_gain**rho)
    return U_gamble, U_sure

def q_gamble_rho(params, sure_gain, risk_gain, risk_prob):
    rho, beta = params
    U_g, U_s = Utility_rho(params, sure_gain, risk_gain, risk_prob)
    return 1 / (1 + np.exp(-beta * (U_g - U_s)))
def likelihood_rho(params, sure_gain, risk_gain, risk_prob, choices):
    rho, beta = params
    U_g, U_s = Utility_rho(params, sure_gain, risk_gain, risk_prob)
    q_gamble = 1/(1+np.exp(-beta*(U_g - U_s)))
    log_likelihood = np.sum(choices * np.log(q_gamble) + (1 - choices) * np.log(1 - q_gamble))
    return -log_likelihood






def estimate_parameters_rho(data, likelihood_rho):
    participant_sessions = []

    for participant in range(65, 97):
        for session in [1, 3, 6, '1+3+5']:  # Iterate over sessions (1, 3, 5 and all three sessions)
            if session != '1+3+5':
                data2 = data[(data['participant'] == participant) & (data['session'] == session)]
            else:
                data2 = data[data['participant'] == participant]

            if not data2.empty:
                sure_gain = data2['sure_gain'].values
                risk_gain = data2['risk_gain'].values
                risk_prob = data2['risk_prob'].values
                choices = data2['chosen'].values

                initial_params = np.array([0, 0])

                res = minimize(likelihood_rho, initial_params, args=(sure_gain, risk_gain, risk_prob, choices), method='Nelder-Mead')

                rho, beta = res.x

                if session == 6:
                    session = 5
                participant_sessions.append({'participant': participant, 'session': session, 'rho': rho, 'beta': beta})
            else:
                participant_sessions.append({'participant': participant, 'session': session, 'rho': rho, 'beta': beta})

    result_df = pd.DataFrame(participant_sessions)
    return result_df



def get_utility_E_V_accuracy(data, results):
    filtered_results = results[results['session'] == '1+3+5']
    correct_prediction_rates = []
    for participant in range(65, 97):
        participant_row = filtered_results[filtered_results['participant'] == participant]
        alpha = participant_row['alpha'].item()
        beta = participant_row['beta'].item()

        participant_data = data[data['participant'] == participant]
        predicted_choices = []
        for index, row in participant_data.iterrows():
            risk_prob = row['risk_prob']
            risk_gain = row['risk_gain']
            sure_gain = row['sure_gain']
            params = [alpha, beta]
            q_gamble = q_gamble_E_V(params, sure_gain, risk_gain, risk_prob)
            if q_gamble > 0.5:
                predicted_choice = 1
            else:
                predicted_choice = 0

            predicted_choices.append(predicted_choice)

        participant_data['predicted_choice'] = predicted_choices
        number_of_participant_rows = len(participant_data)
        number_of_correct_predictions = len(participant_data[participant_data['chosen'] == participant_data['predicted_choice']])
        participant_correct_prediction_rate = number_of_correct_predictions / number_of_participant_rows
        correct_prediction_rates.append(participant_correct_prediction_rate)


    return np.mean(correct_prediction_rates)









def get_utility_rho_accuracy(data, results):
    filtered_results = results[results['session'] == '1+3+5']
    correct_prediction_rates = []
    for participant in range(65, 97):
        participant_row = filtered_results[filtered_results['participant'] == participant]
        rho = participant_row['rho'].item()
        beta = participant_row['beta'].item()

        participant_data = data[data['participant'] == participant]
        predicted_choices = []
        for index, row in participant_data.iterrows():
            risk_prob = row['risk_prob']
            risk_gain = row['risk_gain']
            sure_gain = row['sure_gain']
            params = [rho, beta]
            q_gamble = q_gamble_rho(params, sure_gain, risk_gain, risk_prob)
            if q_gamble > 0.5:
                predicted_choice = 1
            else:
                predicted_choice = 0

            predicted_choices.append(predicted_choice)

        participant_data['predicted_choice'] = predicted_choices
        number_of_participant_rows = len(participant_data)
        number_of_correct_predictions = len(participant_data[participant_data['chosen'] == participant_data['predicted_choice']])
        participant_correct_prediction_rate = number_of_correct_predictions / number_of_participant_rows
        correct_prediction_rates.append(participant_correct_prediction_rate)


    return np.mean(correct_prediction_rates)

