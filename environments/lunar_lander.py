import gymnasium as gym

env = gym.make("LunarLander-v3", render_mode="human")

observation, info = env.reset()

print("Initial observation:", observation)
print("Observation space:", env.observation_space)
print("Action space:", env.action_space)

for _ in range(1000):
    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    # print("Action:", action)
    # print("Reward:", reward)
    # print("Observation:", observation)

    if terminated or truncated:
        observation, info = env.reset()

env.close()