#!/bin/python3

# Import modules needed for this
import tabula as tb
from PyPDF2 import PdfFileReader
import pandas as pd
import glob
import os
pdfs = os.listdir("./PDFs/")
print(pdfs)
# This cell gets a list of pages in the pdf. We cannot rely on readng the file as a whole :(
# We will pass this list into the next cell.
infile = "PDFs/"+input("What pdf to convert? ")
# Get number of pages from pdf infile
pdf = PdfFileReader(open(infile,'rb'))
numPages = pdf.getNumPages()

# Get a list of pages to pass into the reader loop
tmpPages = []
for i in range(numPages):
    tmpPages.append(i++1)
    
print("There are ",len(tmpPages),"pages.")

#####

# This loops over the main pdf file page by page, saving each page as a csv in the /pages directory
# THIS MIGHT TAKE SOME TIME IF THE FILE IS LARGE
print(len(tmpPages)," pages to be converted.") # Here is our list of pages.

# This for loop takes the list of pages in the PDF from the previous cell.
# This loop also converts the PDF into individual CSVs and saves them to /pages
for i in tmpPages:
    print("Converting page: "+str(i))
    tb.convert_into(infile,
                    "pages/page-"+str(i)+".csv",
                    guess=True,
                    output_format="CSV",
                    stream=True,
                    pages=i,
                    silent=True
                    )
        
print("Done!")

#####

# This cell takes the CSVs from the previous cell and converts them into one DataFrame
path = r'pages/'
all_files = glob.glob(path + "*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, names=['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7'], index_col=0, header=None)
    li.append(df)

frame = pd.concat(li, ignore_index=False)

# IF you need it....
# You'll probably need it.
frame.reset_index(inplace=True)

# Here we can export the DataFrame we created as a CSV.
# This cell will prompt you to enter a filename. (.csv) added automatically ;)
saveName = input("Give it a meaningful name: ")
frame.to_csv('CSVs/'+saveName+'.csv', index=False, encoding='utf-8')
os.system('rm -r pages/*')