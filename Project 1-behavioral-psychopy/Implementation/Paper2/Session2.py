# Session 2 and 4
# This session contains predict, observe and self-trial

# Imports
from utils import *


#____________Constants__________
piePos = (0, 0.5)
reward_prob_self,        reward_mag_self                            = generate_self_rewards()
reward_prob_risk_averse, reward_mag_risk_averse, risk_averse_answer = generate_risk_averse_rewards()
reward_prob_risk_seeker, reward_mag_risk_seeker, risk_seeker_answer = generate_risk_seeker_rewards()


reward_prob_risk_pred,   reward_mag_risk_pred,                      = generate_risk_pred_rewards()

number_of_trials_pred = len(reward_prob_risk_pred) // 3
number_of_trials_obs  = len(reward_prob_risk_averse) // 2
number_of_trials_self = len(reward_prob_self) // 2
number_of_trials_pred = 3 # For testing purposes
number_of_trials_obs  = 3 # For testing purposes
number_of_trials_self = 3 # For testing purposes

answers_pred1 = []
answers_pred2 = []
answers_pred3 = []
answers_obs1 = []
answers_obs2 = []
answers_obs3 = []
answers_self1 = []
answers_self2 = []
answers_self3 = []
predSection = 0
obsSection  = 0
selfSection = 0
#_______________________________

win = visual.Window(size=(1000, 700), fullscr=False, color='black') # create the window


write_text_message(win, 'Welcome to the experiment!', 0.1, (0, 0.1))
write_text_message(win, 'Session 2', 0.1, (0, 0))
win.flip()
core.wait(4)
write_text_message(win, 'Press the space bar when you are ready', 0.1, (0, -0.1))
win.flip()
event.waitKeys(keyList=['space'])





#____________________________________Prediction1_________________________________#
# First Predict Section which is for risk pred (neutral)
predSection = 1
number_of_trials = number_of_trials_pred
write_text_message(win, 'Prediction 1 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
number_of_trials_pred = 5
print("Prediction 1 starts:")
       # range(            0,                              6        )
for i in range((predSection-1)*number_of_trials_pred, predSection*number_of_trials_pred):
    reward = reward_mag_risk_pred[i]
    prob   = reward_prob_risk_pred[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_pred1.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("First pred is done")





#____________________________________Observation1_________________________________#
write_text_message(win, 'Observation 1 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
image = visual.ImageStim(win, image='ManLookingAtComp.png')
image.draw()
win.flip()
core.wait(2)
obsSection = 1 # Risk averse
print("Observation 1 starts:")
for i in range((obsSection-1)*number_of_trials_obs, obsSection*number_of_trials_obs):
    reward = reward_mag_risk_averse[i]
    prob = reward_prob_risk_averse[i]
    ratio = [1 - prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = risk_averse_answer[i]
    core.wait(1)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    draw_user_answer_obs(win, str(answer), accept_pos)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(3)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Observation 1 ends:")





#____________________________________Self Trial1_________________________________#
write_text_message(win, 'Self trial 1 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
selfSection = 1
print("Self trial 1 starts:")
for i in range((selfSection-1)*number_of_trials_self, selfSection*number_of_trials_self):
    reward = reward_mag_self[i]
    prob = reward_prob_self[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_self1.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Self trial 1 ends:")




#____________________________________Observation2_________________________________#
write_text_message(win, 'Observation 2 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
image = visual.ImageStim(win, image='ManLookingAtComp.png')
image.draw()
win.flip()
core.wait(2)
obsSection = 2 # Risk seeker
print("Observation 2 starts:")
for i in range((obsSection-1)*number_of_trials_obs, obsSection*number_of_trials_obs):
    reward = reward_mag_risk_seeker[i]
    prob   = reward_prob_risk_seeker[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = risk_seeker_answer[i]
    core.wait(1)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer_obs(win, str(answer), accept_pos)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(3)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Observation 2 ends:")






#____________________________________Self Trial2_________________________________#
write_text_message(win, 'Self trial 2 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
selfSection = 2
print("Self trial 2 starts:")
for i in range((selfSection-1)*number_of_trials_self, selfSection*number_of_trials_self):
    reward = reward_mag_self[i]
    prob = reward_prob_self[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_self2.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != selfSection*number_of_trials_self:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Self trial 2 ends:")







#____________________________________Prediction2_________________________________#
write_text_message(win, 'Prediction 2 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
predSection = 2
print("Prediction 2 starts:")
       # range(            6,                              12        )
for i in range((predSection-1)*number_of_trials, predSection*number_of_trials):
    reward = reward_mag_risk_pred[i]
    prob   = reward_prob_risk_pred[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_pred2.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Prediction 2 ends:")






#____________________________________Observation3_________________________________#
write_text_message(win, 'Observation 3 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
image = visual.ImageStim(win, image='ManLookingAtComp.png')
image.draw()
win.flip()
core.wait(2)
obsSection = 3 # Risk averse
obsSection = 1 # It is changd to 1 because the first half must be used
print("Observation 3 starts:")
for i in range((obsSection-1)*number_of_trials_obs, obsSection*number_of_trials_obs):
    reward = reward_mag_risk_averse[i]
    prob = reward_prob_risk_averse[i]
    ratio = [1 - prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = risk_averse_answer[i]
    core.wait(1)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    draw_user_answer_obs(win, str(answer), accept_pos)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(3)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Observation 3 ends:")





#____________________________________Self Trial3_________________________________#
write_text_message(win, 'Self trial 3 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
selfSection = 3
selfSection = 1 # It is changd to 1 because the first half must be used
print("Self trial 3 starts:")
for i in range((selfSection-1)*number_of_trials_self, selfSection*number_of_trials_self):
    reward = reward_mag_self[i]
    prob = reward_prob_self[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_self1.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != selfSection*number_of_trials_self:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Self trial 3 end")






#____________________________________Observation4_________________________________#
write_text_message(win, 'Observation 4 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
image = visual.ImageStim(win, image='ManLookingAtComp.png')
image.draw()
win.flip()
core.wait(2)
obsSection = 4 # Risk seeker
obsSection = 2 # It is changd to 2 because the second half must be used
print("Observation 3 starts:")
#____________________________________Observation4_________________________________#
for i in range((obsSection-1)*number_of_trials_obs, obsSection*number_of_trials_obs):
    reward = reward_mag_risk_seeker[i]
    prob = reward_prob_risk_seeker[i]
    ratio = [1 - prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = risk_seeker_answer[i]
    core.wait(1)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    draw_user_answer_obs(win, str(answer), accept_pos)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(3)
    if i != obsSection*number_of_trials_obs:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Observation 3 ends")





#____________________________________Self Trial4_________________________________#
write_text_message(win, 'Self trial 4 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
selfSection = 4
selfSection = 2
print("Self trial 4 starts:")
for i in range((obsSection-1)*number_of_trials_obs, obsSection*number_of_trials_obs):
    reward = reward_mag_self[i]
    prob = reward_prob_self[i]
    ratio = [1 - prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_self1.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$' + str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != selfSection * number_of_trials_self:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Self trial 4 ends")







#____________________________________Prediction3_________________________________#
write_text_message(win, 'Prediction 3 is about to start', 0.1, (0, -0.1))
win.flip()
core.wait(2)
predSection = 3
print("Prediction 3 starts:")
       # range(            12,                              18        )
for i in range((predSection-1)*number_of_trials, predSection*number_of_trials):
    reward = reward_mag_risk_pred[i]
    prob   = reward_prob_risk_pred[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers_pred3.append(answer)

    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    draw_user_answer(win, answer)
    draw_buttons2(win, accept_pos, deny_pos)
    win.flip()
    core.wait(1)
    if i != number_of_trials:
        write_text_message(win, '+', 0.3, (0, 0))
        win.flip()
        core.wait(1)
print("Prediction 3 ends:")



write_text_message(win, 'End of session 2', 0.1, (0, 0))
win.flip()
core.wait(2)
write_text_message(win, 'Thanks for participation', 0.1, (0, 0))
win.flip()
core.wait(2)


