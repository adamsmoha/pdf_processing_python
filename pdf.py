import PyPDF2

# read file as binary
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
