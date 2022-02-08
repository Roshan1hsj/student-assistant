from pytube import YouTube
from googlesearch import search
import webbrowser
def downloader():
    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)

    # Showing details
    print("Title: ", yt.title)

    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)
    # Getting the highest resolution possible
    print()

    h=input("ENTER THE RESOLUTION OF THE VIDEO (720p/360p)\nENTER (mp3) TO DOWNLOAD ONLY AUDIO\n(720p/360p/mp3): ")
    if h in "720p720P":
        ys = yt.streams.get_by_itag(22)
    elif h in "MP3mp3audio":
        ys = yt.streams.get_by_itag(140)
    else:
        ys = yt.streams.get_by_itag(18)

    # Starting download
    print("Downloading...")
    try:
        ys.download("C:\\Users\\User\\Downloads")
        print("the video is available in Downloads")
    except Exception as e:
        ys.download()
        print ("the video is available in the same location as the python project location")
    finally:
        print("Download completed!!")
        print()

    f = input("want to download another one (Y \ N): ")
    if f in "Nn":
        exit()
    else:
        youtube()

def youtube():

    print("****************************************************************************")
    print("*                                                                          *")
    print("*               YOUTUBE VIDEO DOWNLOADER                                   *")
    print("*                                                                          *")
    print("****************************************************************************")
    print()

    print ("1.DO YOU HAVE A YOUTUBE LINK\n2.OR WANT TO SEARCH THROUGH PYTHON: ")
    u=input("CHOOSE (1/2): ")
    if u == "1":
        downloader()
    elif u=="2":
        print("1.ENTER THE VIDEO NAME \n 2.OR PRESS ENTER TO OPEN YOUTUBE")

        query = input("ENTER VIDEO NAME OR PRESS (ENTER): ")
        for i in search(query+"youtube", tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(i)
        for j in search(query+"youtube", tld="co.in", num=10, stop=10, pause=2):
            print(j)

        downloader()
    else:
        print ("WRONG CHOICE!!!")
        youtube()
