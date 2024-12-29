import matplotlib.pyplot as plt
import numpy as np

dimension = 20

game = np.zeros([dimension, dimension])
game[5][10] = 1
game[6][10] = 1
game[6][11] = 1
game[7][11] = 1
game[7][9] = 1

"""
This game shall take place on a taurus.

The only other rules I will use for the game of life below are as follows (from Wikipedia):
1. Live cell with < 2 live neighbors dies
2. Live cell with 2 or 3 live neighbors lives
3. Live cell > 3 neighbors dies
4. Dead cell with 3 live neighbors is resurrected
"""

def tick():
# Main loop, encode 'i' as the horizontal axis and 'j' the vertical axis -- we're gonna do this the dumb way for now.
  nextGame = np.zeros([dimension, dimension])

  for i in range(dimension):
    for j in range(dimension):
      global game
      neighbors = game[(i - 1) % dimension][(j + 1) % dimension] + game[i % dimension][(j + 1) % dimension] + game[(i + 1) % dimension][(j + 1) % dimension]
      neighbors += game[(i - 1) % dimension][j % dimension] + game[(i + 1) % dimension][j % dimension]
      neighbors += game[(i - 1) % dimension][(j - 1) % dimension] + game[i % dimension][(j - 1) % dimension] + game[(i + 1) % dimension][(j - 1) % dimension]

      match neighbors:
        case 2:
          nextGame[i][j] = game[i][j]
        case 3:
          nextGame[i][j] = 1
        case _:
          nextGame[i][j] = 0
  
  game = nextGame

from matplotlib.animation import PillowWriter

fig, ax = plt.subplots()

ax.set_title("Game of Life")
mesh = ax.pcolormesh(game, cmap="inferno")

writer = PillowWriter(fps=14)

with writer.saving(fig, "out.gif", 100):
  for i in range(200):
    mesh.set_array(game)
    writer.grab_frame()
    tick()
  
