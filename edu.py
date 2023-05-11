from googlesearch import search
import webbrowser

def googlesearch():
    query = input("ENTER THE SEARCH ITEM OR THE WEBSITE YOU WANT TO OPEN: ")
    for i in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.open(i)
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)
    print()





def education():
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   STUDY MODE ACTIVATED                                   *")
    print("*                                                                          *")
    print("****************************************************************************")
    print()
    print("ENTER YOUR DOUBTS REGARDING A TOPIC OR\nENTER THE NAME WEBSITE YOU WANT TO STUDY IN")
    try:
        query = input("ENTER TOPIC OR DOUBTS: ")
        for i in search(query, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(i)
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(j)

    except Exception as e:
        print ("SOMETHING WRONG!!!",e)
        education()
