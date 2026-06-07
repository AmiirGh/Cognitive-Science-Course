from psychopy import visual, core, event
import matplotlib.pyplot as plt
import os
import random
import numpy as np
import itertools


def write_text_message(win, text, height, position, color):
    text = visual.TextStim(win, text=text, color=color, height=height, pos=position)
    text.draw()

def wait_for_answer_experiment_type(win):
    while True:
        key_events = event.getKeys()
        if key_events:
            if '1' in key_events:
                print('selected 1')
                return '1'
            elif '2' in key_events:
                print('selected 2')
                return '2'
            elif key_events[0] in ['q', 'escape']:
                win.close()
                core.quit()

def wait_for_answer(win, PostLearnFlag):
    timer = core.Clock()  # Create a timer
    while timer.getTime() < 4.0 or PostLearnFlag:  # Wait for a maximum of 4 seconds
        key_events = event.getKeys()
        if key_events:
            if 'left' in key_events:
                print('Selected left')
                return 'left'
            elif 'right' in key_events:
                print('Selected right')
                return 'right'
            elif key_events[0] in ['q', 'escape']:
                win.close()
                core.quit()

    print('Late')  # If no key is pressed within 4 seconds
    return 'late'

def get_A1_sample():
    mean = 64
    std_dev = 13
    sample = np.random.normal(mean, std_dev)
    return sample

def get_A2_sample():
    return get_A1_sample()

def get_B_sample():
    mean = 54
    std_dev = 13
    sample = np.random.normal(mean, std_dev)
    return sample

def get_C_sample():
    mean = 44
    std_dev = 13
    sample = np.random.normal(mean, std_dev)
    return sample

def get_sample(side, selectedChar, alphabet_train):
    if side == 'right':
        if selectedChar == alphabet_train[0]:
            sample = get_A1_sample()
        elif selectedChar == alphabet_train[1]:
            sample = get_A2_sample()
        elif selectedChar == alphabet_train[2]:
            sample = get_B_sample()
        elif selectedChar == alphabet_train[3]:
            sample = get_C_sample()
    elif side == 'left':
        if selectedChar == alphabet_train[0]:
            sample = get_A1_sample()
        elif selectedChar == alphabet_train[1]:
            sample = get_A2_sample()
        elif selectedChar == alphabet_train[2]:
            sample = get_B_sample()
        elif selectedChar == alphabet_train[3]:
            sample = get_C_sample()
    return int(sample)

def draw_buttons_exp_type(win):
    rect1 = visual.Rect(win, pos=(+0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='white', lineWidth=2)
    rect2 = visual.Rect(win, pos=(+-0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='white', lineWidth=2)
    rect1.draw()
    rect2.draw()

    button1 = visual.ButtonStim(win, pos=(-0.3, -0.3), text='1', size=(0.3, 0.2), fillColor='black')
    button2 = visual.ButtonStim(win, pos=(+0.3, -0.3), text='2',   size=(0.3, 0.2), fillColor='black')
    button1.draw()
    button2.draw()

def draw_rectangle(win, pos, width, height):
    rect = visual.Rect(win, pos=pos, width=width, height=height, fillColor='black', lineColor='blue', lineWidth=6)
    rect.draw()

def draw_bar_with_lines(win):
    # Constants
    bar_start = (-0.7, -0.2)
    bar_end = (0.7, -0.2)
    num_lines = 10
    line_spacing = (bar_end[0] - bar_start[0]) / num_lines
    bar = visual.Line(win, start=bar_start, end=bar_end, lineColor='white', lineWidth=5)
    bar.draw()
    write_text_message(win, '0', 0.1, (-0.7, -0.35), 'white')
    write_text_message(win, '100', 0.1, (0.7, -0.35), 'white')

    for i in range(num_lines + 1):
        line_x = bar_start[0] + i * line_spacing
        if i == 0 or i == num_lines:
            line_start = (line_x, -0.12)
            line_end = (line_x, -0.28)
        else:
            line_start = (line_x, -0.15)
            line_end = (line_x, -0.25)
        line = visual.Line(win, start=line_start, end=line_end, lineColor='white', lineWidth=2)
        line.draw()


def draw_bar_with_lines_est(win):
    # Constants
    bar_start = (-0.8, 0)
    bar_end = (0.8, 0)
    num_lines = 10
    line_spacing = (bar_end[0] - bar_start[0]) / num_lines
    bar = visual.Line(win, start=bar_start, end=bar_end, lineColor='white', lineWidth=6)
    bar.draw()
    write_text_message(win, '0', 0.2, (-0.8, -0.3), 'white')
    write_text_message(win, '100', 0.2, (0.8, -0.3), 'white')

    for i in range(num_lines + 1):
        line_x = bar_start[0] + i * line_spacing
        if i == 0 or i == num_lines:
            line_start = (line_x, -0.15)
            line_end = (line_x, +0.15)
        else:
            line_start = (line_x, -0.1)
            line_end = (line_x, +0.1)
        line = visual.Line(win, start=line_start, end=line_end, lineColor='white', lineWidth=3)
        line.draw()

def mouse_response(win):
    draw_bar_with_lines(win)
    bar_start = (-0.7, -0.2)
    bar_end = (0.7, -0.2)
    mouse = event.Mouse()

    while True:
        mouse.clickReset()
        while not any(mouse.getPressed()):
            # Wait for a mouse click
            pass

        # Get the current mouse position
        mouse_pos = mouse.getPos()

        # Calculate the value based on the mouse position within the bar range
        value = ((mouse_pos[0] - bar_start[0]) / (bar_end[0] - bar_start[0])) * 100
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        circle_pos = (value/100 * 1.4 - 0.7, -0.2)
        circle = visual.Circle(win, pos=circle_pos, radius=0.02, fillColor='blue')
        circle.draw()

        print('value selected is: '+ str(int(value)))
        win.flip()
        core.wait(2)
        return value

def mouse_response_est(win):
    draw_bar_with_lines_est(win)
    bar_start = (-0.8, 0)
    bar_end = (0.8, 0)
    mouse = event.Mouse()

    while True:
        mouse.clickReset()
        while not any(mouse.getPressed()):
            # Wait for a mouse click
            pass

        # Get the current mouse position
        mouse_pos = mouse.getPos()

        # Calculate the value based on the mouse position within the bar range
        value = ((mouse_pos[0] - bar_start[0]) / (bar_end[0] - bar_start[0])) * 100
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        circle_pos = (value/100 * 1.6 -0.8, 0)
        circle = visual.Circle(win, pos=circle_pos, radius=0.04, fillColor='blue')
        circle.draw()

        print('value selected is: '+ str(int(value)))
        win.flip()
        core.wait(2)
        return value


def Check_A1_A2(texts, alphabet, reward, counter_reward):
    row = [0, 0]
    if texts[0] == alphabet[0]:
        row[0] = reward
    if texts[0] == alphabet[1]:
        row[1] = counter_reward
    if texts[1] == alphabet[0]:
        row[0] = reward
    if texts[1] == alphabet[1]:
        row[1] = counter_reward

    return np.array(row).reshape(1, 2)

def TrainingPhase_partial_feedback(win, number_of_trials, alphabet, train_or_learn):
    # train_or_learn is 0 for train and 1 for learn
    Expected_values = np.empty((0, 2))

    for i in range(number_of_trials):
        write_text_message(win, ' ', 0.4, (0.4, 0), 'white')
        win.flip()
        core.wait(1)
        texts = random.sample(alphabet, 2)
        write_text_message(win, texts[0], 0.4, (0.4, 0),  'white')
        write_text_message(win, texts[1], 0.4, (-0.4, 0), 'white')
        win.flip()
        answer = wait_for_answer(win, 0)

        if answer == 'right':
            draw_rectangle(win, (+0.4, 0), 0.4, 0.5)
            reward = get_sample('right', texts[0], alphabet)
            write_text_message(win, str(reward), 0.2, (+0.4, -0.35), 'blue')  # Reward value

            counter_reward = get_sample('left', texts[1], alphabet)
            ev_row = Check_A1_A2(texts, alphabet, reward, counter_reward)
            Expected_values = np.append(Expected_values, ev_row, axis=0)
        elif answer == 'left':
            draw_rectangle(win, (-0.4, 0), 0.4, 0.5)
            reward = get_sample('left', texts[1], alphabet)
            write_text_message(win, str(reward), 0.2, (-0.4, -0.35), 'blue')  # Reward value

            counter_reward = get_sample('left', texts[1], alphabet)
            ev_row = Check_A1_A2(texts, alphabet, reward, counter_reward)
            Expected_values = np.append(Expected_values, ev_row, axis=0)
        elif answer == 'late':
            write_text_message(win, 'Too late!', 0.2, (0, 0), 'white')
            win.flip()
            core.wait(2)
        elif answer == 'q' or answer == 'escape':
            win.close()
            core.quit()
            break

        if answer != 'late':
            write_text_message(win, texts[0], 0.4, (0.4, 0), 'white')
            write_text_message(win, texts[1], 0.4, (-0.4, 0), 'white')
            win.flip()
            core.wait(2)


        mean_col1 = np.mean(Expected_values[:, 0][Expected_values[:, 0] != 0])
        mean_col2 = np.mean(Expected_values[:, 1][Expected_values[:, 1] != 0])

        if abs(mean_col1 - mean_col2) < 1 and i > 100:
            if train_or_learn == 1:  # Its learning phase
                break  # break the loop cause the mean value of A1 and A2 are somehow equal
                # and its been at least 100 trials



def TrainingPhase_complete_feedback(win, number_of_trials, alphabet, train_or_learn):
    # train_or_learn is 0 for train and 1 for learn
    Expected_values = np.empty((0, 2))
    for i in range(number_of_trials):
        texts = random.sample(alphabet, 2)
        write_text_message(win, ' ', 0.4, (0.4, 0), 'white')
        win.flip()
        core.wait(1)

        write_text_message(win, texts[0], 0.4, (0.4, 0),  'white')
        write_text_message(win, texts[1], 0.4, (-0.4, 0), 'white')
        win.flip()
        answer = wait_for_answer(win, 0)

        if answer == 'right':
            draw_rectangle(win, (+0.4, 0), 0.4, 0.5)
            reward = get_sample('right', texts[0], alphabet)
            counter_reward = get_sample('left', texts[1], alphabet)
            write_text_message(win, str(reward), 0.2, (+0.4, -0.35), 'blue') #Reward value
            write_text_message(win, str(counter_reward), 0.2, (-0.4, -0.35), 'blue') #counterReward value
        elif answer == 'left':
            draw_rectangle(win, (-0.4, 0), 0.4, 0.5)
            reward = get_sample('left', texts[1], alphabet)
            counter_reward = get_sample('left', texts[1], alphabet)
            write_text_message(win, str(reward), 0.2, (+0.4, -0.35), 'blue')  # Reward value
            write_text_message(win, str(counter_reward), 0.2, (-0.4, -0.35), 'blue')  # counterReward value
        elif answer == 'late':
            write_text_message(win, 'Too late!', 0.2, (0, 0), 'white')
            win.flip()
            core.wait(2)
        elif answer == 'q' or answer == 'escape':
            win.close()
            core.quit()
            break
        if answer != 'late':
            write_text_message(win, texts[0], 0.4, (0.4, 0), 'white')
            write_text_message(win, texts[1], 0.4, (-0.4, 0), 'white')
            win.flip()
            core.wait(2)

        mean_col1 = np.mean(Expected_values[:, 0][Expected_values[:, 0] != 0])
        mean_col2 = np.mean(Expected_values[:, 1][Expected_values[:, 1] != 0])

        if abs(mean_col1 - mean_col2) < 1 and i > 100:
            if train_or_learn == 1: # Its learning phase
                break # break the loop cause the mean value of A1 and A2 are somehow equal
                      # and its been at least 100 trials

def LearningPhase_partial_feedback(win, number_of_trials, alphabet):
    write_text_message(win, 'Learning phase', 0.1, (0, 0.1), 'white')
    win.flip()
    core.wait(3)
    TrainingPhase_partial_feedback(win, number_of_trials, alphabet, 1)

def LearningPhase_complete_feedback(win, number_of_trials, alphabet):
    write_text_message(win, 'Learning phase', 0.1, (0, 0.1), 'white')
    win.flip()
    core.wait(3)
    TrainingPhase_complete_feedback(win, number_of_trials, alphabet, 1)


def PostLearningPhase(win, alphabet):
    # Post learning phase doesn't need any page to inform the participant
    pairs = list(itertools.combinations(alphabet, 2))
    print(pairs)
    for i in range(1): # This 1 here must change to 4
        random.shuffle(pairs)
        for pair in pairs:
            write_text_message(win, ' ', 0.4, (0.4, 0), 'white')
            win.flip()
            core.wait(1)
            write_text_message(win, pair[0], 0.4, (0.4, 0), 'white')
            write_text_message(win, pair[1], 0.4, (-0.4, 0), 'white')
            win.flip()
            answer = wait_for_answer(win, 1)

            if answer == 'right':
                draw_rectangle(win, (+0.4, 0), 0.4, 0.5)
            elif answer == 'left':
                draw_rectangle(win, (-0.4, 0), 0.4, 0.5)
            elif answer == 'late':
                write_text_message(win, 'Too late!', 0.2, (0, 0), 'white')
                win.flip()
                core.wait(2)

            elif answer == 'q' or answer == 'escape':
                win.close()
                core.quit()
                break
            if answer != 'late':
                write_text_message(win, pair[0], 0.4, (0.4, 0), 'white')
                write_text_message(win, pair[1], 0.4, (-0.4, 0), 'white')
                win.flip()
                core.wait(2)
                draw_bar_with_lines(win)
                win.flip()
                mouse_response(win)
                win.flip()

def EstimationPhase(win, alphabet):
    # Estimation phase will have 16 trials which consists of 4 trials for each charcater
    for i in range(2):
        random.shuffle(alphabet)
        for char in alphabet:
            print(char)
            write_text_message(win, char, 0.5, (0.0, 0), 'white')
            win.flip()
            core.wait(4)
            draw_bar_with_lines_est(win)
            win.flip()
            mouse_response_est(win)
            win.flip()










