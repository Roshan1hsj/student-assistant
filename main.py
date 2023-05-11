# importing libraries
from edu import*
from calc import*
from attendance import*
from game import*
from rate import*

def mind():
    print("WHAT'S ON YOUR MIND TODAY: \n1.STUDY TIME(HAVE DOUBTS OR WANT NOTES)")
    print("2.PLAY SNAKE GAME:\n3.PLAY ANOTHER OFFLINE GAME-21\n4.PLAY ONLINE GAMES")
    print("5.WANT TO DOWNLOAD SOME YOUTUBE VIDEOS \n6.HAVING PROBLEMS IN CALCULATIONS ")
    print("7.SEARCH WEB THROUGH PYTHON \n8.RATE THIS PROGRAM")
    c = input("SO WHAT'S TODAY PLAN (1/2/3/4/5/6/7/8): ")
    if c not in "12345678s":
        print ("INVALID INPUT CHOOSE ONE FROM (1/2/3/4/5/6/7/8)")
        mind()
    else:
        if c == "1":
            education()
            mind()
        elif c == "2":
            snake()
            mind()
        elif c == "3":
            twentyone()
            mind()
        elif c == "4":
            print("ENTER THE NAME OF THE GAME OR THE GENRE OF GAME LIKE\nACTION\nADVENTURE\nMYSTERY/PUZZLE\n")
            query = input("ENTER THE GAME NAME OR PRESS (ENTER) TO DIRECTLY OPEN A GAME SITE: ")
            for i in search(query+"online game", tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(i)
            for j in search(query+"online game", tld="co.in", num=10, stop=10, pause=2):
                print(j)
            print()
            mind()

        elif c == "5":
            youtube()
            mind()

        elif c == "6":
            calculator()
            mind()
        elif c == "7":
            googlesearch()
            mind()
        else:
            rating()


print("****************************************************************************")
print("*                                                                          *")
print("*                   WELCOME TO STUDENT ASSISTANT                           *")
print("*                                                                          *")
print("****************************************************************************")
print()
print("****************************************************************************")
print("*                                                                          *")
print("*                   ATTENDANCE SECTION                                     *")
print("*                                                                          *")
print("****************************************************************************")
print()

a=input("PLEASE GIVE YOUR ATTENDANCE\n PLEASE PRESS n IF ALREADY GIVEN \n>>>(y/n) : ")
if a in "yYOKok":
    attendance()
    mind()
else:
    print()
    mind()





