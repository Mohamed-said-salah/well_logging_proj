
## LAS -->> 

from welly import Project
import matplotlib.pyplot as plt
from saied_point_collector import collector

## reading wells files
wells = Project.from_las('my_wells/*.las')

## selecting sepecific well
well = wells[-4]

curve_name = 'CALI'

fig, ax = plt.subplots(figsize=(4, 18), ncols = 1)

collector = collector(ax, ["event", "dehk"], markers=["x", "+"], colors=['orange', 'red'])

## getting specific tool data from well
rhob = well.get_curve(curve_name)
bs = well.get_curve('BS')




if rhob is not None:
    ax = rhob.plot(ax = ax, c='blue')
    ax = bs.plot(ax= ax, c='black')
ax.set_title(f"{curve_name} for\n{well.header.name}")

plt.tight_layout()

plt.show()

print(collector.get_points())
print(f"type of get_positions: {type(collector.get_points())}")

my_dict = collector.get_points()

# print("event: ", my_dict['event'][0][0])
# print("dehk", my_dict['dehk'][0][0])

for record in my_dict['event']:
    for axis in record:
        print(axis)



#------------------------------------------------------------------------

### ** < old failed method > 

# from welly import Project, Well
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backend_bases import MouseButton
# from time import sleep

# wells = Project.from_las('my_wells/*.las')

# well = wells[-4]

# curve_name = 'CALI'

# fig, ax = plt.subplots(figsize=(4, 18), ncols = 1)


# rhob = well.get_curve(curve_name)
# bs = well.get_curve('BS')


# if rhob is not None:
#     ax = rhob.plot(ax = ax, c='red')
#     ax = bs.plot(ax= ax, c='black')
# ax.set_title(f"{curve_name} for\n{well.header.name}")

# lst = []

# def on_move(event):
#     # get the x and y pixel coords
#     x, y = event.x, event.y
#     if event.inaxes:
#         ax = event.inaxes  # the axes instance
#         # print('data coords %f %f' % (event.xdata, event.ydata))
        
        
# def on_click(event):
#     if event.button is MouseButton.LEFT:
#         lst.append(f"x={event.x}, y={event.y}")
#         print('disconnecting callback')
#         plt.disconnect(binding_id)


# try:

#     print(rhob[0])
# except:
#     print('failed !')

# try:
#     print(rhob[-1])
# except:
#     print('failed!')


# plt.xlim(4,8)
# plt.ylim(-0.5,2.5)

# binding_id = plt.connect('motion_notify_event', on_move)
# plt.connect('button_press_event', on_click)

# print(lst)

### ** </ old failed method>

#-----------------------------------------------------------------------------

### ** <failed zooming method>

## ! next libirary ((mpl_interactions)) must be installed with pip*
# from mpl_interactions import zoom_factory, panhandler

# fig, ax = plt.subplots(constrained_layout=True)

# zoom_factory(ax)
# ph = panhandler(fig, button=2)

# ax.use_sticky_edges = True

### ** </failed zooming method>

