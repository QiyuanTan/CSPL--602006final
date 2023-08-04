import time
import remi_test4
import re

env = remi_test4.env(num_good=10, num_adversaries=0, num_obstacles=0, num_food=0, max_cycles=5e2, num_forests=0,
                     render_mode='human')
env.reset()

n = 1
for agent in env.agent_iter():
    if n % 10 == 0:
        print(f'----------step{int(n / 10)}----------')
    observation, reward, termination, truncation, info = env.last()
    if termination or truncation:
        action = None
    else:
        action = env.action_space(agent).sample()
    # this is where you would insert your policy
    env.step(action)
    n += 1
    for inf in info:
        message_history = info[inf]
    # time.sleep(0.5)
env.close()

message_history.to_csv('message_history.csv', index=False)
# read the csv file and reformat it with regular expressions
context = open('message_history.csv', 'r').read().replace('sender,receiver\n', '').replace(',', ';').replace('agent_',
                                                                                                             '')

# write the csv file
with open('reformatted_message_history.csv', 'w') as f:
    f.write(context)
    f.close()
