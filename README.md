# Py-PDF-Ripper
---
This notebook/script takes single or multipage pdfs and turns them into pandas dataframes with options to export to a csv. This was developed on Kubuntu and Manjaro so you will encounter errors on Windows. I'll review any PRs and be grateful for it :)

Requirements:
 - tabula-py (pip3 install)
 - PyPDF2 (pip3 install)
 - working Java install (openjre/openjdk works fine on linux)

Features:
 - Notebook:
   - Takes in multipage pdfs
   - Produces pandas dataframes
   - exports csv

 - pdfrip:
   - Takes in multipage pdfs
   - produces pandas dataframe
   - exports dataframe as csv

Changes:
 - Removed unused modules
 - Created directories to make the notebooks easier to use
   - put your pdf files in /PDFs
   - the notebook/script uses /pages for its own output from the pdf reader. We had to create real files to get the best outcome
   - exported CSVs are automatically saved to /CSVs
 - Cleaned up the comments and code

Current development:
 - adding inputs to script for more interactivity with the way the dataframe is created.
   - adding number of columns question
   - adding naming of columns questions

Future development:
 - Probably a tkinter GUI
 - ##### I may or may not try to make it OS agnostic

Author:
chukrobertson
