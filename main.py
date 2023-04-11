#Extract text from pdf

import spacy
from PyPDF2 import PdfReader

nlp = spacy.load('en_core_web_lg')

def text_from_pdf():
    reader = PdfReader(f'data/paper1.pdf')
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    data = text_from_pdf()
    #print((data))    #39590 characters
    tokens = nlp(data)
    #print(len(tokens))  #7785 tokens
