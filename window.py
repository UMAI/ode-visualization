import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from solve import solveODE
from frames import PlotFrame, InputFrame

main_window = tk.Tk()
main_window.title('ODE visualization')
        
plot_frame = PlotFrame(parent=main_window)
plot_frame.config(height=500, width=500, bg='white')
plot_frame.pack(side=tk.LEFT)

input_frame = InputFrame(parent=main_window, plot_frame=plot_frame)
input_frame.config(height=500, width=300, bg='green')
input_frame.pack(side=tk.RIGHT)

main_window.mainloop()