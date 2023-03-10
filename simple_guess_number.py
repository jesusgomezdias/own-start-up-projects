mport random

# generate random number
NUM = int(random.randint(0, 20))

# we indicate the number of the player
USER_NUM = 0

# we initialise the maximum number of attempts
INTENTOS = int(6)

# if the user is different from the generated number AND the attempts are different from 0 continuous
while USER_NUM != NUM and INTENTOS != 0:
    # request number
    USER_NUM = int(input("give me a number"))

    if USER_NUM != NUM:
        # for each repetition it subtracts 1 from the initial counter.
        INTENTOS -= 1
        print("ERROR", NUM, "you have", INTENTOS, "attempts left")
    if INTENTOS == 0:
        print("sorry, you have exhausted the number of attempts allowed.")
    if USER_NUM == NUM:
        print("correct, the number was the", NUM)


        

    



    

