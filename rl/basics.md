# Reinforcement Learning Basics

## Main Elements

- **Policy**: the decision and planning process of the agent (its brain) - decides the actions the agent takes during each step, denoted by $\pi$.
- **Reward Function**: determines the amount of reward an agent receives after completing a action or series of actions. Reward is often given externally, but some interal reward systems exist.
- **Value Function**: determines the value of a state over the long term - fundamental to RL.
- **Environment Models**: a model represents a fully observable environment, such as representing all possible game states in tic-tac-toe. Most RL algorithms use the concept of a partially observable state, due to the number of states in an environment (e.g., more states than number of atoms in the universe).
