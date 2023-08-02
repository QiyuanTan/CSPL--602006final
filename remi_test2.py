import time
import remi_test4

env = remi_test4.env(num_good=4, num_adversaries=0, num_obstacles=0, num_food=2, max_cycles=25, num_forests=0, render_mode='human')

env.reset()
for agent in env.agent_iter():
    observation, reward, termination, truncation,  info = env.last()
    if termination or truncation:
        action = None
    else:
        action = env.action_space(agent).sample()
# this is where you would insert your policy
    env.step(action)
    time.sleep(0.15)

env.close()
