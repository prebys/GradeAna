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
    # This list MUST include 'Current Score' and 'Final Score', because they will be used to check for
    # missing values
    #
    columns = ['Homework Final Score',
               'Labs Final Score',
               'Quizzes Final Score',
               'Final Final Score',
               'Current Score',
               'Final Score']

    # Define four histograms format [column name',bins,range]
    hists = [['Homework Final Score',50,(0.,100.)],
            ['Quizzes Final Score',50,(0.,100.)],
            ['Labs Final Score',50,(0.,100.)],
            ['Final Final Score',50,(0.,100.)]]

    # Define 3 scatter plots based on the histogram definitions above
    scatters = [['Homework Final Score','Final Final Score'],
                ['Labs Final Score','Final Final Score'],
                ['Quizzes Final Score','Final Final Score']]

    # Define what you want to bar chart, as well as the x range
    barchart = ['Final Score',(40.,100.)]

    # Individual figure size
    figsize = (8,8)

    return columns, hists, scatters, barchart, figsize

