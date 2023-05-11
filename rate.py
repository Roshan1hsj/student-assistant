from quote import quote
def rating():
    try:
        res = quote('quote', limit=1)
        r = int(input("PLEASE, RATE THIS PROGRAM OUT OF 5\nENTER YOUR CHOICE (1/2/3/4/5): "))
        if (r > 5 or r < 1):
            print("CHOOSE A NUMBER FROM 1 T0 5")
            rating()
        elif (r == 1 or r == 2):
            print("SORRY FOR THE INCONVENIENCE, WE WILL TRY TO IMPROVE YOUR EXPERIENCE")
        else:
            print("THANK YOU FOR CHOOSING STUDENT ASSISTANT")
            print()
            for d in res:
                print(d['quote'])
                print("BY---", d['author'])
    except Exception as e:
        print ("SOMETHING WRONG!!!, ",e)

