import time
import random
import turtle


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
    except Exception as e:
        print("\n")




def twentyone():
    # Python code to play 21 Number game
    print()
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
        exit()

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
                break
            elif nex == "no":
                print("Continuing...")
            else:
                print("Wrong choice")
