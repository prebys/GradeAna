#
# Python routine to read the exported grades from Canvas and make some diagnostic plots
#
# Usage:
#   python3 GradeAna.py [export_file.csv]
#
# Expects assignment categories
#   Homework
#   Labs
#   Quizzes (or quizzes)
#   Final
# 21-MAR-2024  E.Prebys  Releasable version using verbatim exported file
# 22-MAR-2024  E.Prebys  Added check that Current Score matches Final Score
#                        If not, it means some cells are not filled.
#
import sys
import numpy as np
import matplotlib
from matplotlib import pyplot
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd

if (len(sys.argv)>1):
    filename = sys.argv[1]
else:
    filename = 'totals.csv'
    
print("Reading data from file ",filename,"...")

# Read the exported grades from Canvas. 
data = pd.read_csv(filename)
# Drop the 1 or 2 lines that are blank in the ID column because those are not valid entries
data = data[np.isnan(data['ID'])==False]

# Drop the test student
data = data[data['Student']!='Student, Test']

# Give the columns I use simpler names.  Note that 
# I have sometimes not capitalized "Quizzes"
data.rename(columns={'Homework Final Score':'hw',
                    'Labs Final Score': 'lab',
                    'Quizzes Final Score': 'quiz',
                    'quizzes Final Score': 'quiz',
                    'Final Final Score': 'final',
                    'Current Score': 'current',
                    'Final Score':'total'},inplace=True)


# Because the columns originally had weird entries at the top, they were cast 
# objects, so need to cast them as floats now and only keep those columns
data = data[['hw','lab','quiz','final','current','total']].apply(pd.to_numeric)
# Only look at students who took the final
data = data[data['final']>0.]

# Check that the current score is equal to the final score.  If not, some entries
# are blank
data_check = data[data['current']!=data['total']]
nbad = len(data_check)
if(nbad==0):
	print("All values for Current Score match Final Score. Looks good!")
else:
	print("Found %d rows where Current Score doesn't match Final Score!"%(nbad))
	print("This usually means some grade entries are missing!")

# How many usable records?
print("Found a total of %d usable student records."%(len(data)))


# Make a histogram and a bar plot
f,p = pyplot.subplots(2,2)

histhw = p[0][0]  # Homework Histogram
histlab = p[0][1]  # lab histogram
histquiz = p[1][0]  # quiz historgram
histfinal = p[1][1] # Final histogram



# Histogram
histhw.hist(data['hw'],50,(0.,100.))
histhw.set_xlabel('Homework')
histhw.grid()

histlab.hist(data['lab'],50,(0,100.))
histlab.set_xlabel('Lab')
histlab.grid()

histquiz.hist(data['quiz'],50,(0,100.))
histquiz.set_xlabel('Quiz')
histquiz.grid()

histfinal.hist(data['final'],50,(0.,100.))
histfinal.set_xlabel('Final')
histfinal.grid()

#pyplot.show()
f,p = pyplot.subplots(2,2)


fvsh = p[0][0] # Final vs HW
fvsl = p[0][1] # Final vs lab
fvsq = p[1][0] # Final vs quizz
bar = p[1][1]  # Total Bar Chart


#histtotal.hist(data['total'],20,(60.,100.))
#histtotal.set_xlabel('Total')

# p[0].hist(data['Total'],15,(70.,100.))
fvsh.scatter(data['hw'],data['final'])
fvsh.set_xlabel('Homework')
fvsh.set_ylabel('Final')
fvsh.grid()


fvsl.scatter(data['lab'],data['final'])
fvsl.set_xlabel('Lab')
fvsl.set_ylabel('Final')
fvsl.grid()

fvsq.scatter(data['quiz'],data['final'])
fvsq.set_xlabel('Quiz')
fvsq.set_ylabel('Final')
fvsq.grid()

# Descending bar plot
y = np.arange(len(data['total']))
x = sorted(data['total'])

bar.barh(y,x)
bar.set_xlim(40.,100.)
bar.set_ylim(0,len(x))
bar.xaxis.set_major_locator(MultipleLocator(10))
bar.xaxis.set_minor_locator(MultipleLocator(1))
bar.grid(True,which='major',color='b',linestyle='-')
bar.grid(True,which='minor',color='r',linestyle='--')
bar.set_xlabel('Total')


pyplot.show()
