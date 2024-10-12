# Reinforcement Learning Basics

## Main Elements

- **Policy**: the decision and planning process of the agent (its brain) - decides the actions the agent takes during each step, denoted by $\pi$.
- **Reward Function**: determines the amount of reward an agent receives after completing a action or series of actions. Reward is often given externally, but some interal reward systems exist.
- **Value Function**: determines the value of a state over the long term - fundamental to RL.
- **Environment Models**: a model represents a fully observable environment, such as representing all possible game states in tic-tac-toe. Most RL algorithms use the concept of a partially observable state, due to the number of states in an environment (e.g., more states than number of atoms in the universe).

## Markov Decision Process (MDP)

A discrete-time stochastic control process.

- **Discrete**: time moves forward in finite intervals:

    $$
    t \in {1, 2, 3, \cdots}
    $$

- **Stochastic**: future states depend only partially on the actions taken
- **Control process**: based on decision making to reach the target state

Mathematical components: $(S, A, R, P)$,:

- $S$: set of possible states of the task
- $A$: set of actions that can be taken in each of the states
- $R$ set of rewards for each state-action $(s, a)$ pair
- $P$: the probabilities of passing from each state to another when taking each possible action

MDPs have no memory. The next state depends only on the current state, not on the previous ones. This process is known as a *Markov process* and fulfills the *Markov Property*.

$$
P[S_{t+1} | S_t = s_t] = P[S_{t+1} | S_t = s_t, S_{t-1} = s_{t-1}, \cdots, S_0 = s_0]
$$

MDPs are an extension of *Markov Chains*, MDPs introduce *actions* and *rewards*.

### Types of MDPs

- **Finite**: the number of $S$, $A$ and $R$ are finite.
- **Infinite**: one or more of the number of $S$, $A$, and $R$ is infinite.
- **Episodic**: MDPs last for a finite set of rounds with a terminal state.
- **Continuous**: MDPs have no terminal state and continue forever.
