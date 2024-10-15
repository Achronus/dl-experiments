from enum import Enum
import random


class AgentAction(Enum):
    """Agent movement increments: `(row, col)`."""

    LEFT = (0, -1)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    UP = (-1, 0)


class GridTile(Enum):
    _FLOOR = 0
    ROBOT = 1
    TARGET = 2

    def __str__(self):
        return self.name[0]


class WarehouseRobot:
    def __init__(self, rows: int = 4, cols: int = 4, seed: int | None = None) -> None:
        self.rows = rows
        self.cols = cols
        self.seed = seed

        self.grid = self._reset_grid()

        self.reset()

    def _reset_grid(self) -> list:
        """Creates an empty grid filled with _FLOOR tiles."""
        grid = []

        for _ in range(self.rows):
            row = [GridTile._FLOOR] * self.cols
            grid.append(row)

        return grid

    def _update_grid(self) -> None:
        """Updates the grid with the current positions of the agent and target."""
        self.grid = self._reset_grid()

        self.grid[self.agent_pos[0]][self.agent_pos[1]] = GridTile.ROBOT
        self.grid[self.target_pos[0]][self.target_pos[1]] = GridTile.TARGET

    def reset(self) -> None:
        """Reset the warehouse grid."""
        random.seed(self.seed)

        self.agent_pos = [0, 0]
        self.target_pos = [
            random.randint(1, self.rows - 1),
            random.randint(1, self.cols - 1),
        ]

        self._update_grid()

    def act(self, action: AgentAction) -> bool:
        """
        Moves the robot depending on the given action, keeping it in grid.

        Returns:
            done (bool): True if reached target position. Otherwise, False
        """
        row, col = action.value

        self.agent_pos[0] = max(0, min(self.rows - 1, self.agent_pos[0] + row))
        self.agent_pos[1] = max(0, min(self.cols - 1, self.agent_pos[1] + col))

        self._update_grid()

        return self.agent_pos == self.target_pos

    def render(self) -> None:
        """Prints the current grid."""
        for row in self.grid:
            print("".join(str(f"{tile} ") for tile in row))
        print()
