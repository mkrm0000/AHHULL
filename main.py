import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import _converter_code

f_path = ""


def __init_window():
    # Create a tkinter window
    window = tk.Tk()
    window.title("File Input Program")
    window.geometry("640x600")
    return window

window = __init_window()
#adding window title
tk.Label(window, text="AHHull" , font=("Helvetica", 14, "bold") , pady=5).pack()

def lbp_n_wl():
    lbp = lbp_var.get()
    wl_space = wl_var.get()
    #setting lbp and wl
    _converter_code.lbp = lbp
    _converter_code.wl_spacing = wl_space
    print("LBP : " + _converter_code.lbp)
    print("WL_Spacing : " + _converter_code.wl_spacing)

lbp_var_text = tk.Label(window, text="Input LBP :", font=("Helvetica", 10) , pady=5)
lbp_var_text.pack()
lbp_var = tk.Entry(window)
lbp_var.pack()
wl_var_text = tk.Label(window, text="Input WL Spacing :", font=("Helvetica", 10) , pady=5)
wl_var_text.pack()
wl_var = tk.Entry(window)
wl_var.pack()


# Create a label and an entry widget for file input
label_file_path = tk.Label(window, text="Select a .csv file:" , pady=5, font=("Helvetica", 10))
label_file_path.pack()


def _3d_plotting(points , wl , stl ):
    w_lines = [i for i in wl]
    s_lines = [i for i in stl]
    
    # Create a frame to contain the 3D plot
    frame = ttk.Frame(window)
    frame.pack(expand=tk.YES, fill=tk.BOTH , pady=10 )
    # Create a 3D plot
    fig = plt.figure(figsize=(1, 1))
    ax = fig.add_subplot(111, projection='3d')
    # (points)
    x = [ i[0] for i in points] 
    y = [ i[1] for i in points] 
    z = [ i[2] for i in points] 
    ax.scatter(x, y, z, c='r', marker='.', label="Vertices") #shawing points
    #this loop is for showing waterplane lines
    for pt in w_lines:
        xx = [ i[0] for i in pt]
        yy = [ i[1] for i in pt]
        zz = [ i[2] for i in pt]
        ax.plot(xx , yy , zz , marker=' ',linewidth=0.5, linestyle='-')
    #this loop is for showing station lines
    for pt in s_lines:
        xx = [ i[0] for i in pt]
        yy = [ i[1] for i in pt]
        zz = [ i[2] for i in pt]
        ax.plot(xx , yy , zz , marker=' ',linewidth=0.5, linestyle='-')
    # Calculate the range of data in each axis
    x_range = max(x) - min(x)
    y_range = max(y) - min(y)
    z_range = max(z) - min(z)
    max_range = max(x_range, y_range, z_range)
    # Set equal aspect ratio for all axes
    ax.set_xlim([min(x), min(x) + x_range])
    ax.set_ylim([min(y), min(y) + y_range])
    ax.set_zlim([min(z), min(z) + z_range])
    ax.grid(True, linestyle='-', linewidth=0.5)
    plt.axis("equal")
    # Add basic controls (pan, zoom, and rotate)
    ax.view_init(elev=20, azim=30)
    ax.set_clip_on(True)
    # Create a canvas to display the 3D plot within the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(expand=tk.YES, fill=tk.BOTH)



def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Offset Data CSV", "*.csv"), ("All Files", "*.*")])
    f_path = file_path
    def startfunc():
        lbp_n_wl()
        tk.Label(window, text="Left Mouse Click to Move \nMiddle Mouse Button to Drag/Pan \nRight Mouse Button to Zoom in or out" , font=("Helvetica", 10) , pady=4).pack()
        points , wl , stl = _converter_code.run(f_path)

        lbp_var_text.destroy()
        lbp_var.destroy()
        wl_var_text.destroy()
        wl_var.destroy()

        label_file_path.destroy()
        browse_button.destroy()
        start_button.destroy()
        _3d_plotting(points , wl , stl )
        make_dxf_label = tk.Label(window, text="Exported DXF for Autocad" , padx=200)
        make_dxf_label.pack( pady=10 )
        tk.Label(window, text="AHHull is a small program to visualize Offset Data Table in 3D \nMade by Ismam Labib and Mokarrom Hossain\nBSMRMU NAOE-06" , font=("Helvetica", 8) , pady=2).pack()
    # Create a button to start processing
    start_button = tk.Button(window, text="Start" , pady=5, padx= 50)
    start_button['command']=startfunc
    start_button.pack()
# Create a button to open a file dialog
browse_button = tk.Button(window, text="Browse", pady=5, padx= 25)
browse_button['command']=open_file 
browse_button.pack()

#ismam and mokarrom from bsmrmu - naoe 06


# Main loop to run the tkinter application
window.mainloop()
