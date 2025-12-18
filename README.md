# GradeAna

Simple routines to make analysis plots for grades.  Designed to work with grades exported
from the GradeBook in Canvas.

The program will make two pages of plots:

* Page 1:
  * four histograms
* Page 2:
  *  three scatter plots
  * On horizontal bar chart, to be used to determin grade cuts
  
The columns to be used are defined in GradeAna_User.py.  The user should not have to
edit GradeAna.py at all.

Usage:

> python3 GradeAna.py 

A file browser will allow you to choose the export file.

There are two example export file/user python files included:

* P118 from Winter 2025
* P40 from Fall 2025

The student names and ID numbers have been redacted.
The correct GradeAna_User file must be copied to GradeAna_User.py prior to using it.


Versions
--------

v1.0	17-DEC-2023	E. Prebys	Original
v2.0 	14-MAR-2024 E. Prebys   Reads exported gradebook directly.
v3.0    17-DEC-2025 E. Prebys	Major changes.  Moved user stuff to GradeAna_User
_
			
