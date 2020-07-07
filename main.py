import pyttsx3
import PyPDF2

pdf_book = open('progit.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_book)
pdf_pages = pdf_reader.numPages
print(pdf_pages)
pdf_audio = pyttsx3.init()
for num in range(7, pdf_pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    pdf_audio.say(text)
    pdf_audio.runAndWait()