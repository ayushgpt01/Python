import PyPDF2
import sys

inputs = sys.argv[1:]

# writer = PyPDF2.PdfFileWriter()                custom merger function
# def combiner(pdf_list):
#     for pdf in pdf_list:            
#         with open(pdf, 'rb') as pdf_file:
#             reader = PyPDF2.PdfFileReader(pdf_file)
#             for i in range(reader.getNumPages()):
#                 page = reader.getPage(i)
#                 writer.addPage(page)
#             with open('super.pdf', 'wb') as new_pdf:
#                 writer.write(new_pdf)

def combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')
    


combiner(inputs)