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


#fig = Figure(figsize=(5, 4), dpi=200)
#fig.add_subplot(111).plot(solveODE(['x**2', 'x - y'], [1, 1], 0, 10, 'dopri5', 1e-6))

#canvas = FigureCanvasTkAgg(fig, master=main_window)  # A tk.DrawingArea.
#canvas.draw()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#toolbar = NavigationToolbar2Tk(canvas, main_window)
#toolbar.update()
#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


#def on_key_press(event):
#    print("you pressed {}".format(event.key))
#    key_press_handler(event, canvas, toolbar)


#canvas.mpl_connect("key_press_event", on_key_press)


#def _quit():
#    main_window.quit()     # stops mainloop
#    main_window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


#button = tk.Button(master=main_window, text="Quit", command=_quit)
#button.pack(side=tk.BOTTOM)

main_window.mainloop()