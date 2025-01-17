import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pyplot import imread


img = imread("src/data/SF_map_very_small.jpeg")

fig = plt.figure()
# fig.set_dpi(100)
fig.set_size_inches(15, 15)

ax = plt.axes(xlim=(0, 20), ylim=(0, 20))
patch = plt.Circle((5, -5), 0.75, fc='y')


def init():
    patch.center = (20, 20)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x = 10 + 3 * np.sin(np.radians(i))
    y = 10 + 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.imshow(img, zorder=0,  extent=[0.1, 20.0, 0.1, 20.0])
print(f'Writing animation to disk, please be patient.')
anim.save('the_movie.mp4', writer = 'ffmpeg', fps=30)
print(f'Animation saved!')
# plt.show()

"""
TODO 
Update resultution: https://stackoverflow.com/questions/14666439/how-to-set-the-image-resolution-for-animations
"""
