from pdf2docx import Converter
import os

def convertPdfToDocx(file_in,file_out):
    cv = Converter(file_in)
    cv.convert(file_out, start=0, end=None)
    cv.close()
    return file_out
    

if __name__ == "__main__":
    import sys
    convertPdfToDocx(sys.argv[1],sys.argv[2])
