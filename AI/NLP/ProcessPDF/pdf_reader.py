import pymupdf

class PDFReader:
    def __init__(self, fname):
        self.fname = fname
        
    def read_pdf(self, fname=None):
        with pymupdf.open(fname if fname != None else self.fname) as f:
            text = ""
            for page in f:  # Iterate through pages
                text += page.get_text()  # Extract text
                
            return text