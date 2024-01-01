#For file manipulation
import os
#for pdf data extraction
import pdfplumber

#File in Directory
myFile = r'N:\7-PDF Clients Files\2018 PDF Tax Copy\Kumberly Moscoso 2018.pdf'

#Working Directory
dir1 = r'N:\7-PDF Clients Files\2018 PDF Tax Copy'
os.chdir(dir1)

#List all files in working directory
fList = []
for f in os.listdir():
    fList.append(f)

print(fList)


for f in fList:
    with pdfplumber.open(f) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
    data = text.split('\n')
    target = data[10]
    delete = target[-12:]
    target = target.replace(delete, '')
    fileName = target + ' 2019' + '.pdf'
    for fi in os.listdir():
        if (os.path.basename(fi) != fileName) & (os.path.isfile(fileName) == True):
            fileName = fileName.replace(fileName[-4:], ' (2)' + '.pdf')
    os.rename(f, fileName)

# #PDF Data Extractor
# with pdfplumber.open(myFile) as pdf:
#     page = pdf.pages[0]
#     text = page.extract_text()
#
# print(text)
# data = text.split('\n')
#
# target = data[11]
# #'John Doe 55-55-5555'
#
# delete = target[-12:]
# target = target.replace(delete, '')
#
# print(target)
#
# os.rename(f, tartget + '.pdf')
#
