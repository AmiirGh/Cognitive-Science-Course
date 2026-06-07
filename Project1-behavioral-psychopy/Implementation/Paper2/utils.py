from psychopy import visual, core, event
import matplotlib.pyplot as plt
import os
import random
import math


def draw_pie_chart(win, ratio, pos):
    labels = ['label_red', 'label_green']
    colors = ['red', 'green']

    fig, ax = plt.subplots(facecolor='black')
    ax.pie(ratio, labels=labels, colors=colors, autopct='', startangle=90, radius=1)
    ax.axis('equal')
    plt.savefig('pie_chart.png', facecolor=fig.get_facecolor(), edgecolor='white')
    plt.close(fig)

    image_path = os.path.abspath("pie_chart.png")
    image = visual.ImageStim(win, image=image_path, pos=pos, size=(1.3, 1.3))
    image.draw()

def write_text_message(win, text, height, position):
    text = visual.TextStim(win, text=text, color='white', height=height, pos=position)
    text.draw()

def wait_for_answer(win, accept_pos):
    while True:
        key_events = event.getKeys()
        if key_events:
            if 'left' in key_events:
                if accept_pos[0]<0:
                    print('Accepted')
                elif accept_pos[0]>0:
                    print('Denied')
                return '0'
                break
            elif 'right' in key_events:
                if accept_pos[0] < 0:
                    print('Denied')
                elif accept_pos[0] > 0:
                    print('Accepted')
                return '1'
                break
            elif key_events[0] in ['q', 'escape']:
                win.close()
                core.quit()
                break

def draw_buttons(win):
    accept_pos = (+0.3, -0.3)
    deny_pos = (-0.3, -0.3)

    # Randomly choose the position for the buttons
    if random.choice([True, False]):
        accept_pos, deny_pos = deny_pos, accept_pos

    rect1 = visual.Rect(win, pos=accept_pos, width=0.3, height=0.2, fillColor='black', lineColor='white', lineWidth=2)
    rect2 = visual.Rect(win, pos=deny_pos, width=0.3, height=0.2, fillColor='black', lineColor='white', lineWidth=2)
    rect1.draw()
    rect2.draw()

    button1 = visual.ButtonStim(win, pos=accept_pos, text='Accept', size=(0.3, 0.2), fillColor='black')
    button2 = visual.ButtonStim(win, pos=deny_pos, text='Deny', size=(0.3, 0.2), fillColor='black')
    button1.draw()
    button2.draw()
    return accept_pos, deny_pos

def draw_buttons2(win, accept_pos, deny_pos):
    rect1 = visual.Rect(win, pos=accept_pos, width=0.3, height=0.2, fillColor='black', lineColor='white', lineWidth=2)
    rect2 = visual.Rect(win, pos=deny_pos, width=0.3, height=0.2, fillColor='black', lineColor='white', lineWidth=2)
    rect1.draw()
    rect2.draw()

    button1 = visual.ButtonStim(win, pos=accept_pos, text='Accept', size=(0.3, 0.2), fillColor='black')
    button2 = visual.ButtonStim(win, pos=deny_pos, text='Deny', size=(0.3, 0.2), fillColor='black')
    button1.draw()
    button2.draw()



def draw_user_answer(win, user_answer):
    if user_answer == '0':
        rect = visual.Rect(win, pos=(-0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='yellow', lineWidth=8)
        rect.draw()
    if user_answer == '1':
        rect = visual.Rect(win, pos=(+0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='yellow', lineWidth=8)
        rect.draw()

def draw_user_answer_obs(win, user_answer, accept_pos):
    if user_answer == '0':
        if accept_pos[0] > 0:
            rect = visual.Rect(win, pos=(-0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='yellow', lineWidth=8)
        elif accept_pos[0] < 0:
            rect = visual.Rect(win, pos=(+0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='yellow', lineWidth=8)
        rect.draw()
    if user_answer == '1':
        if accept_pos[0] > 0:
            rect = visual.Rect(win, pos=(+0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='yellow',
                               lineWidth=8)
        elif accept_pos[0] < 0:
            rect = visual.Rect(win, pos=(-0.3, -0.3), width=0.3, height=0.2, fillColor='black', lineColor='yellow',
                               lineWidth=8)
        rect.draw()


def draw_rectangle(win, pos, width, height):
    rect = visual.Rect(win, pos=pos, width=width, height=height, fillColor='black', lineColor='white', lineWidth=2)
    rect.draw()

def generate_self_rewards():
    reward_probabilities = [0.3] * 9 + [0.4] * 9 + [0.5] * 8
    reward_probabilities.append(1)
    reward_probabilities.append(1)

    reward_magnitude = []
    reward_magnitude.extend(range(17, 51, (50 - 17) // 8))
    reward_magnitude.extend(range(12, 47, (47 - 12) // 8))
    reward_magnitude.extend(range(14, 45, 4))
    reward_magnitude.append(20)
    reward_magnitude.append(30)
    #print(reward_probabilities)
    #print(reward_magnitude)
    combined = list(zip(reward_probabilities, reward_magnitude))
    random.shuffle(combined)
    reward_probabilities, reward_magnitude = zip(*combined)
    #print(reward_probabilities)
    #print(reward_magnitude)
    return reward_probabilities, reward_magnitude


def generate_risk_averse_rewards():
    reward_probabilities, reward_magnitude = generate_self_rewards()
    alpha = -0.005 # Negative value for risk averse
    beta = 0.3
    utilities = []
    q_gambles = []
    U_sure = 10 * 1
    answers = []

    for data_point in zip(reward_probabilities, reward_magnitude):
        # U(x) = E(x) + alpha* V(x)
        utility = data_point[0] * data_point[1] + alpha * ((data_point[1] ** 2) * (data_point[0] * (1 - data_point[0])))
        utilities.append(utility)
        q_gamble = 1 / (1 + math.exp(-beta * (utility - U_sure)))
        random_value = random.random()
        if random_value > q_gamble:
            answers.append(0)
        else:
            answers.append(1)
        q_gambles.append(q_gamble)
        #print(q_gamble)
    return q_gambles, reward_magnitude, answers


def generate_risk_seeker_rewards():
    reward_probabilities, reward_magnitude = generate_self_rewards()
    alpha = +0.02  # Positive value for risk averse
    beta = 0.3
    utilities = []
    q_gambles = []
    U_sure = 10 * 1
    answers = []
    for data_point in zip(reward_probabilities, reward_magnitude):
        # U(x) = E(x) + alpha* V(x)
        utility = data_point[0] * data_point[1] + alpha * ((data_point[1] ** 2) * (data_point[0] * (1 - data_point[0])))
        utilities.append(utility)
        q_gamble = 1 / (1 + math.exp(-beta * (utility - U_sure)))
        # print(data_point)
        # print(q_gamble)
        random_value = random.random()
        if random_value > q_gamble:
            answers.append(0)
        elif random_value <= q_gamble:
            answers.append(1)
        q_gambles.append(q_gamble)

    return q_gambles, reward_magnitude, answers

def generate_risk_pred_rewards(): # 18 points .  3 section all 6
    reward_probabilities, reward_magnitude = generate_self_rewards()
    alpha = 0  # Positive value for risk averse
    beta = 0.3
    utilities = []
    q_gambles = []
    U_sure = 10 * 1
    for data_point in zip(reward_probabilities, reward_magnitude):
        # U(x) = E(x) + alpha* V(x)
        utility = data_point[0] * data_point[1] + alpha * ((data_point[1] ** 2) * (data_point[0] * (1 - data_point[0])))
        utilities.append(utility)
        q_gamble = 1 / (1 + math.exp(-beta * (utility - U_sure)))
        # print(data_point)
        # print(q_gamble)

        q_gambles.append(q_gamble)

    return q_gambles, reward_magnitude

#
# def probs_risk_averse():



# def probs_risk_seeking():


