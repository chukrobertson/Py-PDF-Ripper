# Py-PDF-Ripper
---
This notebook/script takes single or multipage pdfs and turns them into pandas dataframes with options to export to a csv. This was developed on Kubuntu and Manjaro so you will encounter errors on Windows. I'll review any PRs and be grateful for it :)

Requirements:
 - tabula-py (python3 -m pip install tabula-py)
 - PyPDF2 (python3 -m pip install PyPDF2)
 - pandas (python3 -m pip install pandas)
 - working Java install (openjre/jdk works fine on linux)

Notes:
 - If you use this in a virtual environment(venv), you'll error finding java and it won't work.
 - I don't run this in a venv since theres so few modules.

Features:
 - Notebook:
   - Takes in multipage pdfs
   - prompts user for number of columns and column names
   - Produces pandas dataframes
   - exports csv

 - pdfrip:
   - Takes in multipage pdfs
   - prompts user for number of columns and column names
   - produces pandas dataframe
   - exports dataframe as csv

Changes:
 - Cleaner code
 - Prompts for number of columns and column names
 - Script updated and moved to /scripts

Curent development:
 - Cleaning

Future development:
 - Probably a tkinter GUI
 - ##### I may or may not try to make it OS agnostic

Author:
chukrobertson
