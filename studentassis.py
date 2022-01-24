# importing libraries
from googlesearch import search
import time
import random
from datetime import date
import turtle
from quote import quote
import webbrowser
import csv
from pytube import YouTube


print("****************************************************************************")
print("*                                                                          *")
print("*                   WELCOME TO STUDENT ASSISTANT                           *")
print("*                                                                          *")
print("****************************************************************************")
print()


def attendance():
    myfile=open("attendance.csv","a",newline='')
    stuwriter=csv.writer(myfile)
    data=[]
    field=["NAME","CLASS","SECTION","ROLL NO","DATE"]
    data.append(field)
    a=int(input("ENTER NO. OF STUDENTS: "))
    for i in range(a):
        name=input('ENTER YOUR NAME: ')
        sect=input("ENTER YOUR CLASS: ")
        sect2=input("ENTER YOUR SECTION: ")
        roll=input('ENTER YOUR ROLL NO: ')
        dates=date.today()
        rec=[name,sect,sect2,roll,dates]
        data.append(rec)
    stuwriter.writerows(data)
    myfile.close()
    print("ATTENDANCE TAKEN SUCCESSFULLY \n IT IS IN THE SAME LOCATION AS OF THIS PYTHON FILE")
    print()
    mind()


def googlesearch():
    query = input("ENTER THE SEARCH ITEM OR THE WEBSITE YOU WANT TO OPEN: ")
    for i in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.open(i)
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)
    print()
    mind()




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
        mind()
    except Exception as e:
        print ("SOMETHING WRONG!!!",e)
        education()





def snake():
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   CONTROLS OF SNAKE GAME:--                              *")
    print("*                                                                          *")
    print("****************************************************************************")
    print()
    print("1. PRESS (w) TO MOVE UP\n2. PRESS (a) TO MOVE LEFT")
    print("3. PRESS (s) TO MOVE DOWN\n4. PRESS (d) TO MOVE RIGHT")

    delay = 0.1
    score = 0
    high_score = 0

    # Creating a window screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("blue")
    # the width and height can be put as user's choice
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # head of the snake
    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    # food in the game
    food = turtle.Turtle()
    colors = random.choice(['red', 'green', 'black'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0 High Score : 0", align="center",
              font=("candara", 24, "bold"))

    # assigning key directions
    def group():
        if head.direction != "down":
            head.direction = "up"

    def godown():
        if head.direction != "up":
            head.direction = "down"

    def goleft():
        if head.direction != "right":
            head.direction = "left"

    def goright():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    wn.listen()
    wn.onkeypress(group, "w")
    wn.onkeypress(godown, "s")
    wn.onkeypress(goleft, "a")
    wn.onkeypress(goright, "d")

    segments = []

    # Main Gameplay
    try:
        while True:
            wn.update()
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "Stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
            if head.distance(food) < 20:
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                food.goto(x, y)

                # Adding segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("orange")  # tail colour
                new_segment.penup()
                segments.append(new_segment)
                delay -= 0.001
                score += 10
                if score > high_score:
                    high_score = score
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
            # Checking for head collisions with body segments
            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()
                y = segments[index - 1].ycor()
                segments[index].goto(x, y)
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)
            move()
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"
                    colors = random.choice(['red', 'blue', 'green'])
                    shapes = random.choice(['square', 'circle'])
                    for segment in segments:
                        segment.goto(1000, 1000)
                    segment.clear()

                    score = 0
                    delay = 0.1
                    pen.clear()
                    pen.write("Score : {} High Score : {} ".format(
                        score, high_score), align="center", font=("candara", 24, "bold"))
            time.sleep(delay)
        wn.mainloop()
    except Exception:
        print()
        mind()


def twentyone():
    # Python code to play 21 Number game
    print("RULES:-----------------------------------")
    print(">>The player can choose to start first or second.")
    print(">>The list of numbers is shown before the Player takes his turn so that it becomes convenient.")
    print(">>If consecutive numbers are not given in input then the player is automatically disqualified.")
    print(">>The player loses if he gets the chance to call 21 and wins otherwise.")

    # returns the nearest multiple to 4
    def nearestMultiple(num):
        if num >= 4:
            near = num + (4 - (num % 4))
        else:
            near = 4
        return near

    def lose1():
        print("\n\nYOU LOSE !")
        print("Better luck next time !")
        print()
        mind()

    # checks whether the numbers are consecutive
    def check(xyz):
        i = 1
        while i < len(xyz):
            if (xyz[i] - xyz[i - 1]) != 1:
                return False
            i = i + 1
        return True

    # starts the game
    def start1():
        global comp
        xyz = []
        last = 0
        while True:
            print("Enter 'F' to take the first chance.")
            print("Enter 'S' to take the second chance.")
            chance = input('> ')

            # player takes the first chance
            if chance == "F":
                while True:
                    if last == 20:
                        lose1()
                    else:
                        print("\nYour Turn.")
                        print("\nHow many numbers do you wish to enter?")
                        inp = int(input('> '))

                        if inp > 0 and inp <= 3:
                            comp = 4 - inp
                        else:
                            print("Wrong input. You are disqualified from the game.")
                            lose1()

                        i, j = 1, 1

                        print("Now enter the values")
                        while i <= inp:
                            a = input('> ')
                            a = int(a)
                            xyz.append(a)
                            i = i + 1

                        # store the last element of xyz.
                        last = xyz[-1]

                        # checks whether the input
                        # numbers are consecutive
                        if check(xyz) == True:
                            if last == 21:
                                lose1()

                            else:
                                # "Computer's turn."
                                while j <= comp:
                                    xyz.append(last + j)
                                    j = j + 1
                                print("Order of inputs after computer's turn is: ")
                                print(xyz)
                                last = xyz[-1]
                        else:
                            print("\nYou did not input consecutive integers.")
                            lose1()

            # player takes the second chance
            elif chance == "S":
                comp = 1
                last = 0
                while last < 20:
                    # "Computer's turn"
                    j = 1
                    while j <= comp:
                        xyz.append(last + j)
                        j = j + 1
                    print("Order of inputs after computer's turn is:")
                    print(xyz)
                    if xyz[-1] == 20:
                        lose1()

                    else:
                        print("\nYour turn.")
                        print("\nHow many numbers do you wish to enter?")
                        inp = input('> ')
                        inp = int(inp)
                        i = 1
                        print("Enter your values")
                        while i <= inp:
                            xyz.append(int(input('> ')))
                            i = i + 1
                        last = xyz[-1]
                        if check(xyz) == True:
                            # print (xyz)
                            near = nearestMultiple(last)
                            comp = near - last
                            if comp == 4:
                                comp = 3
                            else:
                                comp = comp
                        else:
                            # if inputs are not consecutive
                            # automatically disqualified
                            print("\nYou did not input consecutive integers.")
                            # print ("You are disqualified from the game.")
                            lose1()
                print("\n\nCONGRATULATIONS !!!")
                print("YOU WON !")
                exit(0)

            else:
                print("wrong choice")

    game = True
    while game == True:
        print("Player 2 is Computer.")
        print("Do you want to play the 21 number game? (Yes / No)")
        ans = input('> ')
        if ans in 'YesyesYES':
            start1()
        else:
            print("Do you want quit the game?(yes / no)")
            nex = input('> ')
            if nex in "yesYesYES":
                print("You are quitting the game...")
                exit(0)
            elif nex == "no":
                print("Continuing...")
            else:
                print("Wrong choice")


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
        print("1.ENTER THE VIDEO NAME WITH YOUTUBE KEYWORD AT THE END \n 2.OR TYPE YOUTUBE TO MANUALLY SEARCH IN IT")

        query = input("ENTER THE SEARCH ITEM OR THE WEBSITE YOU WANT TO OPEN: ")
        for i in search(query+"youtube", tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(i)
        for j in search(query+"youtube", tld="co.in", num=10, stop=10, pause=2):
            print(j)

        downloader()
    else:
        print ("WRONG CHOICE!!!")
        youtube()


    # ask for the link from user
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
    if h in "720pP":
        ys = yt.streams.get_by_itag(18)
    elif h in "MP3mp3audio":
        ys = yt.streams.get_by_itag(140)
    else:
        ys = yt.streams.get_by_itag(22)

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
        mind()
    else:
        youtube()


def calculator():
    a=int(input("1.BASIC CALCULATOR \n2. GOOGLE CALCULATOR \nCHOOSE (1/2): "))
    if a==2:
        print("THE CALCULATOR WILL BE OPENED IN YOUR DEFAULT WEB BROWSER")
        webbrowser.open("https://www.google.com/search?q=google+calculator&oq=google+calculator&aqs=chrome..69i57j0i433i512j0i512l8.7785j0j7&sourceid=chrome&ie=UTF-8", new=1)
    else:
        # This function adds two numbers
        def add(x, y):
            return x + y

        # This function subtracts two numbers
        def subtract(x, y):
            return x - y

        # This function multiplies two numbers
        def multiply(x, y):
            return x * y

        # This function divides two numbers
        def divide(x, y):
            return x / y

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        while True:
            # take input from the user
            choice = input("Enter choice(1/2/3/4): ")

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))

                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation in "noNONo":
                    break

            else:
                print("Invalid Input")


def rating():
    res = quote('short',limit=1)
    r = int(input("PLEASE, RATE THIS PROGRAM OUT OF 5\nENTER YOUR CHOICE (1/2/3/4/5): "))
    if (r>5 or r<1):
        print("CHOOSE A NUMBER FROM 1 T0 5")
        rating()
    elif (r==1 or r==2):
        print("SORRY FOR THE INCONVENIENCE, WE WILL TRY TO IMPROVE YOUR EXPERIENCE")
    else:
        print("THANK YOU FOR CHOOSING STUDENT ASSISTANT")
        print()
        for d in res:
            print(d['quote'])
            print("BY---", d['author'])

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
        elif c == "2":
            snake()
        elif c == "3":
            twentyone()
        elif c == "4":
            print("ENTER THE NAME OF THE GAME OR THE GENRE OF GAME LIKE\nACTION\nADVENTURE\nMYSTERY/PUZZLE")
            googlesearch()
        elif c == "5":
            youtube()
        elif c == "6":
            calculator()
        elif c == "7":
            googlesearch()
        else:
            rating()




print("****************************************************************************")
print("*                                                                          *")
print("*                   ATTENDANCE SECTION                                     *")
print("*                                                                          *")
print("****************************************************************************")
print()

a=input("PLEASE GIVE YOUR ATTENDANCE\n PLEASE PRESS n IF ALREADY GIVEN \n>>>(y/n) : ")

if a in "yYOKok":
    attendance()
else:
    mind()
