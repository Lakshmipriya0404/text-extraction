#Extract text from pdf

from PyPDF2 import PdfReader

def text_from_pdf(filepath):
    reader = PdfReader(filepath)
    new_text = ''
    for page in reader.pages:
        text = page.extract_text()
        # Removing footer content from each page
        lines = text.split('\n')
        lines = lines[2:]
        lines[0] = lines[0][32:]
        new_text += '\n'.join(lines)
    return new_text
    

if __name__ == "__main__":
    filePath = f'data/paper1.pdf'
    data = text_from_pdf(filePath)
    print(data)  
