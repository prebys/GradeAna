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
# Usage:
#   python3 GradeAna.py 
#
# The user should have to make no changes to this file!
#
# This expects to find the file GradeAna_User, in which all of the plots are defined.
# 
#
# 17-DEC-2025  E.Prebys  MAJOR changes. 
#                            - Added a file browser to choose input file and
#                            - Moved all user definitions to the GradeAna_user.py file
# 22-MAR-2024  E.Prebys  Added check that Current Score matches Final Score
#                        If not, it means some cells are not filled.
# 21-MAR-2024  E.Prebys  Releasable version using verbatim exported file
#
# This is imported from the local file, where the plots are defined
from GradeAna_User import define_plots
# Call the routine to define the plots
columns, hists, scatters, barchart, figsize= define_plots()

print("Program will plot the following:")
print("\tHistorams:")
for h in hists:
    print(f"\t\tColumn: {h[0]}, bins={h[1]}, range={h[2]}")
print("\tScatter Plots:")
for s in scatters:
    print(f"\t\t{s[1]} vs. {s[0]}")
print("\tBar Chart:")
print(f"\t\t{barchart[0]}, range={barchart[1]}")

#
# Required imports
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd
from tkinter import filedialog
#

# Select the exported grade file
filename = filedialog.askopenfilename(
        initialdir=".",
        title="Select the exported Canvas GradeBook",
        filetypes=(("CSV Files", "*.csv"), ("All files", "*.*"))
    )

if not filename:
    print("No file selected. Exiting.")
    sys.exit()


print("Reading data from file ",filename,"...")


# Read the exported grades from Canvas. 
data = pd.read_csv(filename)
# Drop the 1 or 2 lines that are blank in the ID column because those are not valid entries
data = data[np.isnan(data['ID'])==False]

# Drop the test student
data = data[data['Student']!='Student, Test']


### Because the columns originally had weird entries at the top, they were cast 
# objects, so need to cast them as floats now and only keep those columns
data[columns] = data[columns].apply(pd.to_numeric)
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


# Make a histogram and a bar plot
f,ax = plt.subplots(2,2,figsize=figsize)

for i,h in enumerate(hists):
    row = i//2
    col = i%2
    p = ax[row][col]
    
    p.hist(data[h[0]],bins=h[1],range=h[2])
    p.set_xlabel(h[0])
    p.grid()

plt.tight_layout()
plt.show()



# Make the scatterplots
f,ax = plt.subplots(2,2,figsize=figsize)


for i,pair in enumerate(scatters):
    row = i//2
    col = i%2
    p = ax[row][col]

    p.scatter(data[pair[0]],data[pair[1]])
    p.set_xlabel(pair[0])
    p.set_ylabel(pair[1])
    p.grid()



# Descending bar plot
bar = ax[1][1]
y = np.arange(len(data[barchart[0]]))
x = sorted(data[barchart[0]])

bar.barh(y,x)
bar.set_xlim(barchart[1])
bar.set_ylim(0,len(x))
bar.xaxis.set_major_locator(MultipleLocator(10))
bar.xaxis.set_minor_locator(MultipleLocator(1))
bar.grid(True,which='major',color='b',linestyle='-')
bar.grid(True,which='minor',color='r',linestyle='--')
bar.set_xlabel(barchart[0])

plt.tight_layout()

plt.show()