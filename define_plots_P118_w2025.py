# This routine defines the histograms and scatter plots the user is interested in
# Define 4 histograms and 3 scatter plots.
# Will also make a descending bar chart of the final grade.
# This should be the only file the user needs to edit
#
# Versions:
# 17-DEC-2025  E.Prebys  This is the version for P118
# 17-DEC-2025  E.Prebys  Original, separated from GradeAna.py
#
def define_plots():
    # Define and columns we are interested in or might be interested in.
    # This list will be used to convert these columns to numerical values
    #
    # The indices of this list will be used to define the histograms and
    # scatter plots
    cols = ['Homework Final Score',		# 0
               'Labs Final Score',		# 1
               'Quizzes Final Score',	# 2
               'Final Final Score',		# 3
               'Final Score']			# 4

    # Define four histograms format [column index,bins,range]
    hists = [[0,50,(0.,100.)],
            [1,50,(0.,100.)],
            [2,50,(0.,100.)],
            [3,50,(0.,100.)]]

    # Define 3 scatter plots based on the histogram definitions above
    scatters = [[0,3],
                [1,3],
                [2,3]]

    # Define what you want to bar chart, as well as the x range
    barchart = [4,(40.,100.)]

    # Individual figure size 
    figsize = (8,6)

    return cols, hists, scatters, barchart, figsize

