from googlesearch import search
import webbrowser
import os
def directory():
    cwd = os.getcwd()
    print("THE DOWNLOADED FILE IS AVAILABLE IN: {0}".format(cwd))
    webbrowser.open(str(cwd))



def downloader():
    link = input("Enter the link of YouTube video you want to download:  ")
    h=input("ENTER (mp4) FOR VIDEO\nENTER (mp3) TO DOWNLOAD ONLY AUDIO\n(mp4/mp3): ")
    try:
        if h in "mp4MP4video":
            video = YoutubeDL({'outtmpl': '%(title)s.%(ext)s',
                               'format': 'mp4',
                               "preferredquality": '22'})
            video.extract_info(link)
            directory()

        elif h in "MP3mp3audio":
            audio = YoutubeDL({'outtmpl': '%(title)s.%(ext)s', 'format': 'bestaudio'})
            audio.extract_info(link)
            directory()

    except Exception as e:
        print ("Something Wrong\nError-",e,"\nDOWNLOAD ONLINE\n")
        webbrowser.open("https://y2mate.is/en65/")



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

youtube()
