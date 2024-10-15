import random
from agent import WarehouseRobot, AgentAction


def main() -> None:
    agent = WarehouseRobot()
    agent.render()

    for i in range(25):
        action = random.choice(list(AgentAction))

        done = agent.act(action)
        agent.render()

        if done:
            print(f"Success! After {i+1} steps.")
            break


if __name__ == "__main__":
    main()
