# Import modules needed for this
from PyPDF2 import PdfFileReader
import tabula as tb
import pandas as pd
import glob
import os
import time

# This gets a list of pages in the pdf.
# tabula-py missed pages when using the "all" in the read function.
# To get around this I used PyPDF2 to count the pages in the multi-page pdf.
# Then use that integer to pass into "pages"
pdfs = os.listdir("../PDFs/")
print(pdfs)
infile = '../PDFs/'+input("What file to open: ")
colNum = int(input("How many columns?\n"))
colNames = []
for i in range(colNum):
    colNames.append(str(input("Column"+str(i)+":")))

# Get number of pages from pdf infile
pdf = PdfFileReader(open(infile,'rb'),strict=False, warndest=None)
numPages = pdf.getNumPages()
print("There are ",numPages," pages to be converted.")
# This loops over the main pdf file page by page, saving each page as a csv in the /pages directory
# THIS MIGHT TAKE SOME TIME IF THE FILE IS LARGE
start_time=time.time()
for i in range(numPages):
    print("Converting page: "+str(i++1))
    tb.convert_into(infile, "../pages/page-"+str(i++1)+".csv",
                    guess=True,
                    output_format="CSV",
                    stream=True,
                    pages=i++1,
                    silent=True
                    )
# This loop takes the CSVs from the previous cell and converts them into one DataFrame
path = r'../pages/'
all_files = glob.glob(path + "*.csv")
li = []
for filename in all_files:
    df = pd.read_csv(filename, names = colNames, index_col=0, header=None)
    li.append(df)
    
frame = pd.concat(li, ignore_index=False)
os.system('rm -r ../pages/*.csv')
frame.reset_index(inplace=True)
end_time=time.time()-start_time
print("\nDone!\n")
print("Time to run: ",round(end_time),"seconds.")

# Here we can export the DataFrame we created as a CSV.
saveName = input("Type a name for your csv.\n.csv added automatically\n: ")
frame.to_csv('../CSVs/'+saveName+'.csv', index=0, encoding='utf-8')