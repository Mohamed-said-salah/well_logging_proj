
__all__ = [
    "collector",
]
from numbers import Integral

import numpy as np
from matplotlib.backend_bases import MouseButton
from matplotlib.cbook import CallbackRegistry


class collector:
    def __init__(
        self,
        ax,
        classes,
        init_class=None,
        markers=None,
        marker_size=10,
        marker_width=2,
        colors=None,
        legend_bbox=(1.04, 1),
        legend_loc="upper left",
        pick_dist=10,
        **line_kwargs,
    ):
        """
        Parameters
        ----------
        ax : matplotlib axis
        classes : int or list
        init_class : int, or str, optional
            The initial class to use, otherwise will be the first
            class in *classes*
        markers : list
            The marker styles to use.
        colors : list
        legend_bbox : tuple
            bbox to use for the legend
        legend_loc : str or int
            loc to use for the legend
        pick_dist : int
            Picker distance for legend
        """
        if isinstance(classes, Integral):
            self._classes = list(range(classes))
        else:
            self._classes = classes

        if init_class is None:
            self._current_class = self._classes[0]
        else:
            if init_class not in self._classes:
                raise ValueError(
                    f"init_class must be a valid class. Got {init_class} "
                    f"while valid classes are {self._classes}"
                )
            self._current_class = init_class

        if colors is None:
            colors = [None] * len(self._classes)
        if markers is None:
            markers = ["o"] * len(self._classes)

        self.ax = ax
        self._lines = {}
        linestyle = line_kwargs.pop("linestyle", "")
        for i, c in enumerate(self._classes):
            (self._lines[c],) = self.ax.plot(
                [],
                [],
                color=colors[i],
                marker=markers[i],
                markersize = marker_size,
                mew=marker_width,
                label=c,
                linestyle=linestyle,
                **line_kwargs,
            )
        self._leg = self.ax.legend(bbox_to_anchor=legend_bbox, loc=legend_loc)
        self._leg_artists = {}
        self._class_leg_artists = {}
        for legline, legtext, klass in zip(
            self._leg.get_lines(), self._leg.get_texts(), self._classes
        ):
            legline.set_picker(pick_dist)
            legtext.set_picker(pick_dist)
            self._leg_artists[legtext] = klass
            self._leg_artists[legline] = klass
            try:
                # mpl < 3.5
                self._class_leg_artists[klass] = (legline, legline._legmarker, legtext)
            except AttributeError:
                self._class_leg_artists[klass] = (legline, legtext)

        self._fig = self.ax.figure
        self._fig.canvas.mpl_connect("button_press_event", self._clicked)
        self._fig.canvas.mpl_connect("pick_event", self._on_pick)
        self._points = {c: [] for c in self._classes}
        self._update_legend_alpha()
        self._observers = CallbackRegistry()

    def get_points(self):
        return {k: np.asarray(v) for k, v in self._points.items()}

    def set_points(self, points):

        # check all keys first so we don't partially overwrite data
        for k in points.keys():
            if k not in self._classes:
                raise ValueError(f"class {k} is not in {self._classes}")

        for k, v in points.keys():
            self._points[k] = list(v)
        self._observers.process('pos-set', self.get_points())

    def _on_pick(self, event):
        # On the pick event, find the original line corresponding to the legend
        # proxy line, and toggle its visibility.
        try:
            klass = self._leg_artists[event.artist]
        except KeyError:
            # some pick event not on our legend
            return
        self._current_class = klass
        self._update_legend_alpha()
        self._observers.process('class-changed', klass)

    def _update_legend_alpha(self):
        for c in self._classes:
            alpha = 1 if c == self._current_class else 0.2
            for a in self._class_leg_artists[c]:
                a.set_alpha(alpha)
        self._fig.canvas.draw()

    def _has_cbs(self, name):
        
        try:
            return len(self._observers.callbacks[name]) > 0
        except KeyError:
            return False

    def _clicked(self, event):
        if not self._fig.canvas.widgetlock.available(self):
            return
        if event.inaxes is self.ax:
            if event.button is MouseButton.LEFT:
                self._points[self._current_class].append((event.xdata, event.ydata))
                self._update_points(self._current_class)
                self._observers.process(
                    'point-added',
                    (event.xdata, event.ydata),
                    self._current_class,
                )
            elif event.button is MouseButton.RIGHT:
                pos = self._points[self._current_class]
                if len(pos) == 0:
                    return
                dists = np.linalg.norm(
                    np.asarray([event.xdata, event.ydata])[None, None, :]
                    - np.asarray(pos)[None, :, :],
                    axis=-1,
                )
                idx = np.argmin(dists[0])
                removed = pos.pop(idx)
                self._update_points(self._current_class)
                self._observers.process(
                    'point-removed',
                    removed,
                    self._current_class,
                    idx,
                )

    def _update_points(self, klass=None):
        if klass is None:
            klasses = self._classes
        else:
            klasses = [klass]
        for c in klasses:
            new_off = np.array(self._points[c])
            if new_off.ndim == 1:
                # no points left
                new_off = np.zeros([0, 2])
            self._lines[c].set_data(new_off.T)
        self._fig.canvas.draw()

    def on_point_added(self, func):
        
        return self._observers.connect('point-added', lambda *args: func(*args))

    def on_point_removed(self, func):
    
        return self._observers.connect('point-removed', lambda *args: func(*args))

    def on_class_changed(self, func):
    
        self._observers.connect('class-changed', lambda klass: func(klass))

    def on_points_set(self, func):
    
        return self._observers.connect('pos-set', lambda pos_dict: func(pos_dict))
