# Session 1, 3 and 5
# This session only contains self trial

from utils import *
import matplotlib.pyplot as plt
import os
#____________Constants__________
piePos = (0, 0.5)
reward_probabilities, reward_magnitude = generate_self_rewards()

#_______________________________



win = visual.Window(size=(1000,700), fullscr=False, color='black') # create the window

write_text_message(win, 'Welcome to the experiment!', 0.1, (0, 0.1))
write_text_message(win, 'Session 1', 0.1, (0, 0))
win.flip()
core.wait(1)
write_text_message(win, 'Welcome to the experiment!', 0.1, (0, 0.1))
write_text_message(win, 'Session 1', 0.1, (0, 0))
write_text_message(win, 'Self trial', 0.1, (0, -0.2))
win.flip()
core.wait(3)
write_text_message(win, 'Make your Choice', 0.2, (0, 0.3))
write_text_message(win, 'Press the space bar when you are ready', 0.1, (0, -0.1))
win.flip()
event.waitKeys(keyList=['space'])

answers = []
rewards = []
greenRatios = []

# Main Loop for trials
# number_of_trials = len(reward_probabilities)
number_of_trials = 10 # len(reward_probabilities)
for i in range(0, number_of_trials):
    reward = reward_magnitude[i]
    prob = reward_probabilities[i]
    ratio = [1-prob, prob]
    draw_pie_chart(win, ratio, piePos)
    draw_rectangle(win, (0.15, 0.8), 0.2, 0.2)
    write_text_message(win, '$'+str(reward), 0.15, (0.15, 0.8))
    accept_pos, deny_pos = draw_buttons(win)
    win.flip()
    answer = wait_for_answer(win, accept_pos)

    answers.append(answer)
    rewards.append(reward)
    greenRatios.append(ratio[1])

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


write_text_message(win, 'End of session 1', 0.1, (0, 0))
win.flip()
core.wait(2)
write_text_message(win, 'Thanks for participation', 0.1, (0, 0))
win.flip()
core.wait(2)

print('answers')
print(answers)
print('rewards')
print(rewards)
print('greenRatios')
print(greenRatios)


win.close()
core.quit()


