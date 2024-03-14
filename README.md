# GradeAna

Simple routines to make analysis plots for grades.  Designed to work with grades exported
from the GradeBook in Canvas.


Usage:

> python3 GradeAna.py [export_file.csv]

where [export_file.csv] is the entire exported gradebook from Canvas.  It will
automatically drop the "points possible" row and the Test Student row.

Expects assignment categories
   Homework
   Labs
   Quizzes (or quizzes)
   Final

Versions
--------

v1.0	17-DEC-2023	E. Prebys	Original
v2.0 	14-MAR-2024 E. Prebys   Reads exported gradebook directly.
			
