from matplotlib import markers
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pyrsistent import v
from saied_point_collector._collector import collector

fig, ax = plt.subplots()

lines = [
    '1407', '1306', '1205', '1105',
    '1004', '900', '802', '703',
    '604', '504', '405', '303', '206'
]
markers = [
    'x', 'x', 'x', 'x', 'x', 'x',
    'x', 'x', 'x', 'x', 'x', 'x','x'
]
markers_colors = [
    'red', 'tab:blue', 'green', 'c', 'm',
    'tab:orange', 'tab:purple', 'w', 'k', 'y',
    'yellow', 'tab:brown', 'tab:pink',
]


collector = collector(ax, classes=lines, markers=markers, colors=markers_colors)

img = mpimg.imread('pick.jpg')
imgplot = ax.imshow(img, aspect="auto",  extent=[1500,0,3500,0])


plt.axvline(x=1407)
plt.axvline(x=1306)
plt.axvline(x=1205)
plt.axvline(x=1105)
plt.axvline(x=1004)
plt.axvline(x=900)
plt.axvline(x=802)
plt.axvline(x=703)
plt.axvline(x=604)
plt.axvline(x=504)
plt.axvline(x=405)
plt.axvline(x=303)
plt.axvline(x=206)


plt.show()

print(collector.get_points())

