import PyPDF2

pdf = PyPDF2.PdfFileReader(open('super.pdf','rb'))
wtr = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    page.mergePage(wtr.getPage(0))
    output.addPage(page)
with open('output.pdf','wb') as new_pdf:
    output.write(new_pdf)