# This Task only has 1 Session
from utils import *

#____________Constants__________

TrainingPhase_number_of_trials = 5 # 20
LearningPhase_number_of_trials = 300
alphabet_train = ["あ", "い", "く", "け"]
alphabet_learn = ["の", "ひ", "ま", "り"]

#_______________________________


win = visual.Window(size=(1000, 700), fullscr=False, color='black') # create the window

write_text_message(win, 'Welcome to the experiment!', 0.1, (0, 0.1), 'white')
win.flip()
core.wait(3)

# Test types: 1 for partial feedback and 2 for complete feedback
write_text_message(win, 'Ask the examiner to select exp type!', 0.1, (0, 0.1), 'white')
draw_buttons_exp_type(win)
win.flip()
experimentType = wait_for_answer_experiment_type(win) # 1 for partial 2 for counterfactual
print('experiment type selected: ' +str(experimentType))

write_text_message(win, 'Training Phase', 0.1, (0, 0.1), 'white')
win.flip()
core.wait(3)

if experimentType == str(1):    # Partial feedback
 TrainingPhase_partial_feedback(win, TrainingPhase_number_of_trials, alphabet_train, 0)
 LearningPhase_partial_feedback(win, LearningPhase_number_of_trials, alphabet_learn)

elif experimentType == str(2): # Complete feedback
 TrainingPhase_complete_feedback(win, TrainingPhase_number_of_trials, alphabet_train, 0)
 LearningPhase_complete_feedback(win, LearningPhase_number_of_trials, alphabet_learn)


PostLearningPhase(win, alphabet_learn)
EstimationPhase(win, alphabet_learn)





write_text_message(win, 'End of the experiment', 0.1, (0, 0), 'white')
win.flip()
core.wait(2)
write_text_message(win, 'Thanks for participation', 0.1, (0, 0), 'white')
win.flip()
core.wait(2)

win.close()

