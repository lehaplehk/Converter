from moviepy.editor import *
import os

def Convert(file_in,file_out):
    video = VideoFileClip(file_in)
    video.audio.write_audiofile("./tmp/"+file_out)
    return file_out

if __name__ == "__main__":
    import sys
    Convert(sys.argv[1],sys.argv[2])