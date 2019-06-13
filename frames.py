import tkinter as tk
from tkinter import ttk
from tkinter import font
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.mplot3d import Axes3D
from solve import solveODE

class PlotFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initializePlot()
    
    def initializePlot(self):
        self.fig = Figure()
        self.axes = Axes3D(self.fig)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.axes.mouse_init()
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    def plot(self, equations, initial_point, t0, tmax, tolerance, method):
        self.axes.clear()
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.set_zlabel('z')
        self.axes.view_init(elev=30, azim=-60)
        time, points = solveODE(equations, initial_point, t0, tmax, method, tolerance)
        xs = ys = zs = 0
        if len(points) >= 1:
            xs = points[0, :]
        if len(points) >= 2:
            ys = points[1, :]
        if len(points) == 3:
            zs = points[2, :]
        if len(points) == 1:
            ys = time
            self.axes.set_ylabel('t')
            self.axes.set_zlabel('')
            self.axes.view_init(elev=90, azim=0)
        if len(points) == 2:
            zs = time
            self.axes.set_zlabel('t')
        self.axes.plot(xs, ys, zs)
        self.canvas.draw()

class InputFrame(tk.Frame):
    def __init__(self, parent, plot_frame):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.plot_frame = plot_frame
        self.widgets()
    
    def widgets(self):
        font = tk.font.Font(family='Verdana', size=14)

        self.first_line = tk.Frame(self)
        self.first_line.pack(side=tk.TOP, pady=5)
        self.x_label = tk.Label(self.first_line, text='dx/dt =', bg='misty rose', font=font)
        self.x_label.pack(side=tk.LEFT)
        self.x_entry = tk.Entry(self.first_line, font=font)
        self.x_entry.insert(tk.END, '10*(y - x)')
        self.x_entry.pack(side=tk.LEFT)

        self.second_line = tk.Frame(self)
        self.second_line.pack(side=tk.TOP, pady=5)
        self.y_label = tk.Label(self.second_line, text='dy/dt =', bg='misty rose', font=font)
        self.y_label.pack(side=tk.LEFT)
        self.y_entry = tk.Entry(self.second_line, font=font)
        self.y_entry.insert(tk.END, 'x*(28 - z) - y')
        self.y_entry.pack(side=tk.LEFT)

        self.third_line = tk.Frame(self)
        self.third_line.pack(side=tk.TOP, pady=5)
        self.z_label = tk.Label(self.third_line, text='dz/dt =', bg='misty rose', font=font)
        self.z_label.pack(side=tk.LEFT)
        self.z_entry = tk.Entry(self.third_line, font=font)
        self.z_entry.insert(tk.END, 'x*y - z*8/3')
        self.z_entry.pack(side=tk.LEFT)

        self.fourth_line = tk.Frame(self)
        self.fourth_line.pack(side=tk.TOP, pady=5)
        self.x0_label = tk.Label(self.fourth_line, text='x0 =', bg='misty rose', font=font)
        self.x0_label.pack(side=tk.LEFT)
        self.x0_entry = tk.Entry(self.fourth_line, font=font)
        self.x0_entry.insert(tk.END, '1')
        self.x0_entry.pack(side=tk.LEFT)

        self.fifth_line = tk.Frame(self)
        self.fifth_line.pack(side=tk.TOP, pady=5)
        self.y0_label = tk.Label(self.fifth_line, text='y0 =', bg='misty rose', font=font)
        self.y0_label.pack(side=tk.LEFT)
        self.y0_entry = tk.Entry(self.fifth_line, font=font)
        self.y0_entry.insert(tk.END, '1')
        self.y0_entry.pack(side=tk.LEFT)

        self.sixth_line = tk.Frame(self)
        self.sixth_line.pack(side=tk.TOP, pady=5)
        self.z0_label = tk.Label(self.sixth_line, text='z0 =', bg='misty rose', font=font)
        self.z0_label.pack(side=tk.LEFT)
        self.z0_entry = tk.Entry(self.sixth_line, font=font)
        self.z0_entry.insert(tk.END, '1')
        self.z0_entry.pack(side=tk.LEFT)

        self.seventh_line = tk.Frame(self)
        self.seventh_line.pack(side=tk.TOP, pady=5)
        self.t0_label = tk.Label(self.seventh_line, text='t0 =', bg='misty rose', font=font)
        self.t0_label.pack(side=tk.LEFT)
        self.t0_entry = tk.Entry(self.seventh_line, font=font)
        self.t0_entry.insert(tk.END, '0')
        self.t0_entry.pack(side=tk.LEFT)

        self.eiths_line = tk.Frame(self)
        self.eiths_line.pack(side=tk.TOP, pady=5)
        self.tmax_label = tk.Label(self.eiths_line, text='tmax =', bg='misty rose', font=font)
        self.tmax_label.pack(side=tk.LEFT)
        self.tmax_entry = tk.Entry(self.eiths_line, font=font)
        self.tmax_entry.insert(tk.END, '100')
        self.tmax_entry.pack(side=tk.LEFT)

        self.ninth_line = tk.Frame(self)
        self.ninth_line.pack(side=tk.TOP, pady=5)
        self.tolerance_label = tk.Label(self.ninth_line, text='tolerance =', bg='misty rose', font=font)
        self.tolerance_label.pack(side=tk.LEFT)
        self.tolerance_entry = tk.Entry(self.ninth_line, font=font)
        self.tolerance_entry.insert(tk.END, '1e-6')
        self.tolerance_entry.pack(side=tk.LEFT)

        self.tenth_line = tk.Frame(self)
        self.tenth_line.pack(side=tk.TOP, pady=5)
        self.method_label = tk.Label(self.tenth_line, text='method:', bg='misty rose', font=font)
        self.method_label.pack(side=tk.LEFT)
        self.method_combobox = ttk.Combobox(self.tenth_line, font=font, values=['RK45', 'RK23', 'Radau', 'BDF', 'LSODA'], state='readonly')
        self.method_combobox.current(0)
        self.method_combobox.pack(side=tk.LEFT)

        self.eleventh_line = tk.Frame(self)
        self.eleventh_line.pack(side=tk.TOP, pady=5)
        self.plot_button = tk.Button(self.eleventh_line, text='PLOT', command=self.plot, bg='RosyBrown2', font=font)
        self.plot_button.pack(side=tk.TOP)
    
    def plot(self):
        equations = []
        if len(self.x_entry.get()) > 0:
            equations.append(self.x_entry.get())
        if len(self.y_entry.get()) > 0:
            equations.append(self.y_entry.get())
        if len(self.z_entry.get()) > 0:
            equations.append(self.z_entry.get())

        initial_point = []
        if len(self.x0_entry.get()) > 0:
            initial_point.append(float(self.x0_entry.get()))
        if len(self.y0_entry.get()) > 0 and len(equations) >= 2:
            initial_point.append(float(self.y0_entry.get()))
        if len(self.z0_entry.get()) > 0 and len(equations) == 3:
            initial_point.append(float(self.z0_entry.get()))
        
        t0 = 0
        tmax = 100
        if len(self.t0_entry.get()) > 0:
            t0 = float(self.t0_entry.get())
        if len(self.tmax_entry.get()) > 0:
            tmax = float(self.tmax_entry.get())
        
        tolerance=1e-6
        if len(self.tolerance_entry.get()) > 0:
            tolerance = float(self.tolerance_entry.get())
        
        method=self.method_combobox.get()
        
        self.plot_frame.plot(equations, initial_point, t0, tmax, tolerance, method)