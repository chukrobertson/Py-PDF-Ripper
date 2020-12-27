# Py-PDF-Ripper
v 0.11
---
This notebook takes single or multipage pdfs and turns them into pandas dataframes

Requirements:
 - tabula-py (pip3 install)
 - PyPDF2 (pip3 install)
 - working Java install (openjre/openjdk works fine on linux)

Features:
 - Takes in multipage pdfs
 - Produces pandas dataframes

Current development:

Changes:
 - Removed unused modules
 - Created directories to make the notebooks easier to use
  - put your pdf files in /PDFs
  - the notebook uses /pages for its own output from the pdf reader. We had to create real files to get the best outcome
  - CSVs you save are automatically saved to /CSVs

 - Cleaned up the comments and code
  - This was developed on Kubuntu so you might(will) encounter errors on Windows.
   - ###### I may or may not try to make it OS agnostic

Author:
chukrobertson
