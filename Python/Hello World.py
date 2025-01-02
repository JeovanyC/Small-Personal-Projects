import string, time, random

hw = "Hello World"


def main ():
    current_Guess = "".join(random.choice(string.ascii_letters + " ") for i in range(len(hw)))
    while True:
        if current_Guess == hw:
            print ('''
Hello World!!!
''')
            break
        else:
            print(current_Guess)
            current_Guess = random_w(hw, current_Guess)
            time.sleep(0.02)



def random_w (hw, current_Guess):
    guess = list(current_Guess)
    for i in range(len(hw)):
        if guess[i] == hw[i]:
            continue
        else:
            guess[i]= random.choice(string.ascii_letters + " ")
    return "".join(guess)


if __name__ == "__main__":
    main()