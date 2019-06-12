import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.mplot3d import Axes3D
from solve import solveODE

class PlotFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
    
    def widgets(self):
        self.text = tk.Text(self)
    
    def plot(self):
        self.fig = Figure(figsize=(5, 5), dpi=100)
        points = solveODE(['10*(y - x)', 'x*(28 - z) - y', 'x*y - z*8/3'], [1, 1, 1], 0, 10, 'dopri5', 1e-6).T
        print(points.shape)
        self.fig.add_subplot(111, projection='3d').plot3D(points[0, :], points[1, :], points[2, :])
        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0)

class InputFrame(tk.Frame):
    def __init__(self, parent, plot_frame):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.plot_frame = plot_frame
        self.widgets()
    
    def widgets(self):
        self.first_line = tk.Frame(self)
        self.first_line.pack(side=tk.TOP)
        self.x_label = tk.Label(self.first_line, text='dx/dt =')
        self.x_label.pack(side=tk.LEFT)
        self.x_entry = tk.Entry(self.first_line)
        self.x_entry.pack(side=tk.LEFT)

        self.second_line = tk.Frame(self)
        self.second_line.pack(side=tk.TOP)
        self.y_label = tk.Label(self.second_line, text='dy/dt =')
        self.y_label.pack(side=tk.LEFT)
        self.y_label = tk.Entry(self.second_line)
        self.y_label.pack(side=tk.LEFT)

        self.third_line = tk.Frame(self)
        self.third_line.pack(side=tk.TOP)
        self.z_label = tk.Label(self.third_line, text='dz/dt =')
        self.z_label.pack(side=tk.LEFT)
        self.z_label = tk.Entry(self.third_line)
        self.z_label.pack(side=tk.LEFT)

        self.fourth_line = tk.Frame(self)
        self.fourth_line.pack(side=tk.TOP)
        self.plot_button = tk.Button(self.fourth_line, text='PLOT', command=self.plot)
        self.plot_button.pack(side=tk.TOP)
    
    def plot(self):
        self.plot_frame.plot()