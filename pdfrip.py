#!/bin/python3
# Import modules needed for this
import tabula as tb
from PyPDF2 import PdfFileReader
import pandas as pd
import glob
import os
pdfs = os.listdir("PDFs/")
print(pdfs)
infile = "PDFs/"+input("What pdf to convert? ")
# This gets a list of pages in the pdf.
# tabula-py missed pages when using the "all" in the read function.
# To get around this I used PyPDF2 to count the pages in the multi-page pdf.
# Then use that integer to pass into "pages"
pdf = PdfFileReader(open(infile,'rb'),strict=False,warndest=None)
numPages = pdf.getNumPages() # Get number of pages from pdf infile
print("There are ",numPages," pages to be converted.\n") # Here is our list of pages.
# This loop converts the PDF into individual CSVs and saves them to /pages
for i in range(numPages):
    print("Converting page: "+str(i++1))
    tb.convert_into(infile,
                    "pages/page-"+str(i++1)+".csv",
                    guess=True,
                    output_format="CSV",
                    stream=True,
                    pages=i++1,
                    silent=True
                    )
print("Done!")
colNum = int(input("How many columns?\n"))
colNames = []
for i in range(colNum):
    colNames.append(str(input("Column"+str(i++1)+":")))
# This takes the CSVs from the previous cell and converts them into one DataFrame
path = r'pages/'
all_files = glob.glob(path + "*.csv")
li = []
for filename in all_files:
    df = pd.read_csv(filename,
                     names=colNames,
                     index_col=0,
                     header=None)
    li.append(df)
frame = pd.concat(li, ignore_index=False) # Create one dataframe from many
frame.reset_index(inplace=True) # Give it an index at 0
os.system('rm -r pages/*.csv') # Remove the files in /pages because we are done
saveName = input("Type a name for your csv.\n.csv added automatically\n: ") # Prompt for savename
frame.to_csv('CSVs/'+saveName+'.csv', index=0, encoding='utf-8') # Create the csv