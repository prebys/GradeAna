# GradeAna

Simple routines to make analysis plots for grades.  Designed to work with grades exported
from the GradeBook in Canvas.

The program will make two pages of plots:

* Page 1:
  * four histograms
* Page 2:
  *  three scatter plots
  * On horizontal bar chart, to be used to determin grade cuts
  
The program will automatically create 'GradeAna1.png' and 'GradeAna2.png' from these
pages.
  
The columns to be used are defined in GradeAna_User.py file.  The file can have any name
ending in .py and is selected at run time. The user should not have to
edit GradeAna.py at all.

Usage:

> python3 GradeAna.py 

File browsers will allow you to choose both the configuration file and the grade file.

There are two example export file/user python files included:

* P118 from Winter 2025
* P40 from Fall 2025

The student names and ID numbers have been redacted.

Known problems:

* On MacOS, you get the warning: 
    * The class 'NSOpenPanel' overrides the method identifier.  This method is implemented by class 'NSWindow'
    * It can be ignored.

Versions
--------

v1.0	17-DEC-2023	E. Prebys	Original
v2.0 	14-MAR-2024 E. Prebys   Reads exported gradebook directly.
v3.0    17-DEC-2025 E. Prebys	Major changes.  Moved user stuff to GradeAna_User
v4.0	18-DEC-2025 E. Prebys   Made configuration file selectable.  Use indices instead
                                of names for the plots.
        19-DEC-2025 E. Prebys   Made figures resizeable.  Fixed Windows problems.
			
