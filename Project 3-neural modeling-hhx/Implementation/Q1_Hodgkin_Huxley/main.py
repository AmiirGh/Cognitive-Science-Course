# Cognitive Science
# HW3
# Hodgkin-Huxley model implementation
# Amir Ghraghabi
# 810102217

from utils import *

C_m = 1.0  # membrane capacitance (in uF/cm^2)
g_Na = 120.0  # maximum sodium conductance (in mS/cm^2)
g_K = 36.0  # maximum potassium conductance (in mS/cm^2)
g_Na_t = g_Na
g_K_t = g_K
    

g_L = 0.3  # leak conductance (in mS/cm^2)
E_Na = 50.0  # sodium reversal potential (in mV)
E_K = -77.0  # potassium reversal potential (in mV)
E_L = -54.4  # leak reversal potential (in mV)
dt = 0.01  # time step (in ms)
time = np.arange(0, 60, dt)  # time array (in ms)
V = -65.0  # initial membrane potential (in mV)
m = 0.05  # initial sodium activation gating variable
h = 0.6  # initial sodium inactivation gating variable
n = 0.32  # initial potassium activation gating variable

I_inj = 5  # injected current (in uA/cm^2)
start_time = 10.0  # start time of current injection (in ms)
end_time = 20.0  # end time of current injection (in ms)
start_time2 = 35.0  # start time of current injection (in ms)
end_time2 = 45.0  # end time of current injection (in ms)

V_trace = []
m_trace = []
h_trace = []
n_trace = []
gNa_trace = []
gK_trace = []
INa_trace = []
IK_trace = []
IL_trace = []

I_inj_array = []
for i in range(len(time)):
    if start_time <= time[i] <= end_time:
        I = I_inj
    elif start_time2 <= time[i] <= end_time2:
        I = 4*I_inj
    else:
        I = 0.0
    I_inj_array.append(I)

    alpha_m = get_alpha_m(V)
    beta_m = get_beta_m(V)
    alpha_h = get_alpha_h(V)
    beta_h = get_beta_h(V)
    alpha_n = get_alpha_n(V)
    beta_n = get_beta_n(V)

    m += dt * (alpha_m * (1 - m) - beta_m * m)
    h += dt * (alpha_h * (1 - h) - beta_h * h)
    n += dt * (alpha_n * (1 - n) - beta_n * n)

    g_Na_t = g_Na * (m**3) * h
    g_K_t = g_K * (n**4)

    I_Na = g_Na_t *  (V - E_Na)
    I_K = g_K_t *  (V - E_K)
    I_L = g_L * (V - E_L)

    # I_Na = g_Na * m ** 3 * h * (V - E_Na)
    # I_K = g_K * n ** 4 * (V - E_K)
    # I_L = g_L * (V - E_L)

    dV = (I - I_K - I_Na - I_L) / C_m
    V += dt * dV

    V_trace.append(V)
    m_trace.append(m)
    h_trace.append(h)
    n_trace.append(n)

    gNa_trace.append(g_Na_t)
    gK_trace.append(g_K_t)

    INa_trace.append(I_Na)
    IK_trace.append(I_K)
    IL_trace.append(I_L)


# Plotting
plot_min_current_vs_duration()
plot_hh_model(time, V_trace, I_inj_array, m_trace, h_trace, n_trace, gNa_trace, gK_trace, INa_trace, IK_trace, IL_trace)






