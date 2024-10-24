from PIL import Image
import os

def convertImage(file_in,file_out,types):
    img_png = Image.open(file_in) 
    if types == ".jpg":
        img_png = img_png.convert('RGB')
    img_png.save(file_out+types)
    return file_out
    

if __name__ == "__main__":
    import sys
    convertImage(sys.argv[1],sys.argv[2],sys.argv[3])
