import tkinter as tk
from frames import PlotFrame, InputFrame

main_window = tk.Tk()
main_window.title('ODE visualization')
main_window.config(bg='misty rose')

plot_frame = PlotFrame(parent=main_window)
plot_frame.config(height=500, width=500, bg='white')
plot_frame.pack(side=tk.LEFT)

input_frame = InputFrame(parent=main_window, plot_frame=plot_frame)
input_frame.config(height=500, width=500, bg='misty rose')
input_frame.pack(side=tk.RIGHT)

main_window.mainloop()