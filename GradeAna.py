#
# Python routine to read a csv file and make histograms and bar charts
# for grades
#
import numpy as np
import matplotlib
from matplotlib import pyplot
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import pandas as pd

data = pd.read_csv('totals.csv')

# Make a histogram and a bar plot

f,p = pyplot.subplots(2,2)

histhw = p[0][0]  # Homework Histogram
histlab = p[0][1]  # lab histogram
histquiz = p[1][0]  # quiz historgram
histfinal = p[1][1] # Final histogram



# Histogram
histhw.hist(data['hw'],50,(0.,100.))
histhw.set_xlabel('Homework')

histlab.hist(data['lab'],50,(0,100.))
histlab.set_xlabel('Lab')

histquiz.hist(data['quiz'],50,(0,100.))
histquiz.set_xlabel('Quiz')

histfinal.hist(data['final'],50,(0.,100.))
histfinal.set_xlabel('Final')

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


fvsl.scatter(data['lab'],data['final'])
fvsl.set_xlabel('Lab')
fvsl.set_ylabel('Final')

fvsq.scatter(data['quiz'],data['final'])
fvsq.set_xlabel('Quiz')
fvsq.set_ylabel('Final')

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
