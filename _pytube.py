from pytubefix import YouTube
from pytubefix.cli import on_progress

def Download(link,file_out):
    yt = YouTube(link, on_progress_callback = on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download("./tmp/",filename=file_out)
    return file_out

if __name__ == "__main__":
    import sys
    Download(sys.argv[1])