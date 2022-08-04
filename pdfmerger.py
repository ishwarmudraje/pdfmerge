from PyPDF2 import PdfMerger
from os import listdir, path

folder1 = "E:\\pdf_combine\\"

filelist = listdir(folder1)

merger = PdfMerger()

for file in filelist:
    merger.append(path.join(folder1, file))

merger.write("E:\\pdf_combine\\all.pdf")
merger.close()