#
# Python routine to read the exported grades from Canvas and make the following plots
# on two four plot pages
#
#  Page 1:
#      Four histograms of columns of your choice
#  Page 2:
#      Three scatter plots of columns of your choice
#      On descending horizontal bar chart, usually of the Final score, to be used for grade
#      cuts.
#
# These will be automatically saved to 'GradeAna1.png' and GradeAna2.png'
#
# Usage:
#   python3 GradeAna.py 
#
# The user should have to make no changes to this file!
#
# This expects to find the file GradeAna_User, in which all of the plots are defined.
# 
#
#
# 18-DEC-2025  E.Prebys  Changed to use tkinter for plots to stop annoying ghost window
#                        Rearranged code a bit to make it more readable. 
# 17-DEC-2025  E.Prebys  MAJOR changes. 
#                            - Added a file browser to choose input file and
#                            - Moved all user definitions to the GradeAna_user.py file
# 22-MAR-2024  E.Prebys  Added check that Current Score matches Final Score
#                        If not, it means some cells are not filled.
# 21-MAR-2024  E.Prebys  Releasable version using verbatim exported file
#
# All required imports.
import sys
import importlib.util
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import *
from tkinter import filedialog
###################################################################################
# Main steering routine
def GradeAna():

    # Load the plot definitions
    cols, hists, scatters, barchart, figsize=GetPlotDefinitions()

    print("Program will plot the following:")
    print("\tHistorams:")
    for h in hists:
        print(f"\t\tColumn: {cols[h[0]]}, bins={h[1]}, range={h[2]}")
    print("\tScatter Plots:")
    for s in scatters:
        print(f"\t\t{cols[s[1]]} vs. {cols[s[0]]}")
    print("\tBar Chart:")
    print(f"\t\t{cols[barchart[0]]}, range={barchart[1]}")



    # Select the exported grade file
    filename = GetGradeFile()


    print("Reading data from file ",filename,"...")


    # Read the exported grades from Canvas. 
    data = pd.read_csv(filename)
    # Drop the 1 or 2 lines that are blank in the ID column because those are not valid entries
    data = data[np.isnan(data['ID'])==False]
    # Drop the test student
    data = data[data['Student']!='Student, Test']


    ### Because the columns originally had weird entries at the top, they were cast 
    # objects, so need to cast them as floats now and only keep those columns
    data[cols] = data[cols].apply(pd.to_numeric)
    # Make sure to include 'Current Score' and 'Final Score', even if they're not in the list
    data[['Current Score','Final Score']] = data[['Current Score','Final Score']].apply(pd.to_numeric)

    # Only look at students who took the final
    data = data[data['Final Final Score']>0.]


    # Check that the current score is equal to the final score.  If not, some entries are blank
    data_check = data[data['Current Score']!=data['Final Score']]
    nbad = len(data_check)
    if(nbad==0):
	    print("All values for Current Score match Final Score. Looks good!")
    else:
	    print(f"Found the folling {nbad} rows where Current Score doesn't match Final Score (This usually means some grade entries are missing):")
	    for name in data_check['Student']:
		    print('\tName: ',name)

    # How many usable records?
    print("Found a total of %d usable student records."%(len(data)))


    # Make a histograms
    f,ax = plt.subplots(2,2,figsize=figsize)

    for i,h in enumerate(hists):
        row = i//2
        col = i%2
        p = ax[row][col]
    
        p.hist(data[cols[h[0]]],bins=h[1],range=h[2])
        p.set_xlabel(cols[h[0]])
        p.grid()
    # Now start the tkinter window.  For some reason if I do this before the filedialog
    # it causes trouble.    
    plt.tight_layout()
    # Use the resizable version of Tk()
    root = ResizeableTk(f,"Histograms")
    f.savefig('GradeAna1.png')
    
    # root.mainloop()

    # Make the scatterplots
    f,ax = plt.subplots(2,2,figsize=figsize)


    for i,pair in enumerate(scatters):
        row = i//2
        col = i%2
        p = ax[row][col]

        p.scatter(data[cols[pair[0]]],data[cols[pair[1]]])
        p.set_xlabel(cols[pair[0]])
        p.set_ylabel(cols[pair[1]])
        p.grid()



    # Descending bar plot
    bar = ax[1][1]
    y = np.arange(len(data[cols[barchart[0]]]))
    x = sorted(data[cols[barchart[0]]])

    bar.barh(y,x)
    bar.set_xlim(barchart[1])
    bar.set_ylim(0,len(x))
    bar.xaxis.set_major_locator(MultipleLocator(10))
    bar.xaxis.set_minor_locator(MultipleLocator(1))
    bar.grid(True,which='major',color='b',linestyle='-')
    bar.grid(True,which='minor',color='r',linestyle='--')
    bar.set_xlabel(cols[barchart[0]])
    
    plt.tight_layout()
    root = ResizeableTk(f,"Scatter Plots and Bar Chart")

   f.savefig('GradeAna2.png')


    root.mainloop()
#####################################################################################
# Routine to load plot definitions from GradeAna_User file
#
def GetPlotDefinitions():
    #
    # Choose the file with the file dialog
    #
    filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select Histogram Definition File",
            filetypes=(("Python Files", "*.py"), ("All files", "*.*"))
        )

    if not filename:
        print("No file selected.  Using 'GradeAna_User.py")
        filename = 'GradeAna_User.py'

    print(f"Loading definitions from file {filename}")
    #
    #  These next lines load a module based on a file path.
    #  I don't pretend to understand this.  I just asked ChatGPT
    spec = importlib.util.spec_from_file_location("GradeAna_User", filename)
    mymodule = importlib.util.module_from_spec(spec)
    sys.modules["GradeAna_User"] = mymodule
    spec.loader.exec_module(mymodule)

    # Call the routine to define the plots
    return mymodule.define_plots()

#####################################################################################
# Routine to get grade file
#
def GetGradeFile():
    filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select the exported Canvas GradeBook",
            filetypes=(("CSV Files", "*.csv"), ("All files", "*.*"))
        )

    if not filename:
        print("No file selected. Using 'grades.csv'")
        filename='grades.csv'
    return filename
#####################################################################################
#
# Resizable Tk windows
#
class ResizeableTk(Tk):
    def __init__(self,fig,title):
        super().__init__()

        self.title(title)

        # Make the window grid expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create matplotlib Figure
        self.fig = fig
        # Embed in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()

        widget = self.canvas.get_tk_widget()
        widget.grid(row=0, column=0, sticky="nsew")

        # Optional: improve layout on resize
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        # Recalculate layout on resize
        self.fig.tight_layout()
        self.canvas.draw_idle()
####################################################################################
# Execute the main loop    
if __name__ == "__main__":
    GradeAna()
    