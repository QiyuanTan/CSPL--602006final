import time
import remi_test4

env = remi_test4.env(num_good=100, num_adversaries=0, num_obstacles=0, num_food=0, max_cycles=5e1, num_forests=0,
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

message_history.to_csv('message_history.csv')
message_history
