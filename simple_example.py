from numbers import Integral
import matplotlib.pyplot as plt
from saied_point_collector import collector


x_data = [0,1,2,3,4,3,2,1,2,3,4,5,4,3,2,1,2,3]
y_data = [i for i in range(len(x_data))]

fig, ax = plt.subplots(figsize=(4,16), ncols=1)

collector = collector(ax, ['mud-cake', 'wash-out', 'bit-size'], markers=['x', '+', 's'], colors=['orange', 'green', 'red'])

ax.plot(x_data, y_data)
ax.invert_yaxis()
plt.tight_layout()
plt.show()

print(collector.get_points())

picked = collector.get_points()


