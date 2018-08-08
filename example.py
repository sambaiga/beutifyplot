from beautify import *
global_setting()

## line plot
x = np.linspace(-2,2, 500)
fig, ax = subplots()
line_plot(ax, x, x**2, label="$\\mu=2$")
line_plot(ax, x, x**3, label="$\\mu=3$")
line_plot(ax, x, x**4, label="$\\mu=3$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Graph of $x$ vs $y$")
leg=legend(ax)
savefig("figure/line_plot_1", leg)

##bar plot
x = np.random.randint(0,5, size=(1000, 1))
_, counts = np.unique(x, return_counts=True)
label = ["ARUSHA", "MWANZA", "KIGOMA", "GEITA", "DODOMA"]
fig, ax = subplots()
bar_plot(ax, label, counts)
ax.set_title("Crime distribution in 5 Region")
ax.set_ylabel("Number of Crime");
leg=legend(ax)
savefig("figure/bar_plot_1", leg)



## line plot
x = np.linspace(-2,2, 500)
fig, ax = subplots()
line_plot(ax, x, x**2, label="$\\mu=2$")
line_plot(ax, x, x**3, label="$\\mu=3$")
line_plot(ax, x, x**4, label="$\\mu=3$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Graph of $x$ vs $y$")
format_axes(ax)
leg=legend(ax)
savefig("figure/line_plot_2", leg)

##bar plot
x = np.random.randint(0,5, size=(1000, 1))
_, counts = np.unique(x, return_counts=True)
label = ["ARUSHA", "MWANZA", "KIGOMA", "GEITA", "DODOMA"]
fig, ax = subplots()
bar_plot(ax, label, counts)
ax.set_title("Crime distribution in 5 Region")
ax.set_ylabel("Number of Crime");
format_axes(ax)
leg=legend(ax)
savefig("figure/bar_plot_2", leg)