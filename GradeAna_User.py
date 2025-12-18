# This routine defines the histograms and scatter plots the user is interested in
# Define 4 histograms and 3 scatter plots.
# Will also make a descending bar chart of the final grade.
# This should be the only file the user needs to edit
#
# Versions:
# 17-DEC-2025  E.Prebys  This is the version for P40, fall 2025
# 17-DEC-2025  E.Prebys  Original, separated from GradeAna.py
#
def define_plots():
    # Define and columns we are interested in or might be interested in.
    # This list will be used to convert these columns to numerical values
    #
    # The indices of this will be used to define the subsequent plots
    #
    cols = ['Labs Final Score',				    # 0
               'Quizzes Final Score',			# 1
               'Lab Attendance Final Score',	# 2
               'Midterm Final Score',			# 3
               'Final Final Score',				# 4
               'Final Score']					# 5

    # Define four histograms format [column index,bins,range]
    hists = [[0,50,(0.,100.)],
            [1,50,(0.,100.)],
            [3,50,(0.,100.)],
            [4,50,(0.,100.)]]

    # Define 3 scatter plots based on the column definitions above
    scatters = [[1,4],
                [2,4],
                [3,4]]

    # Define what you want to bar chart, as well as the x range
    barchart = [5,(40.,100.)]

    # Individual figure size. Should not be smaller than (6,6)
    figsize = (8,6)

    return cols, hists, scatters, barchart, figsize

