import string, time, random

hw = "Hello World"


def random_w(hw, guess):
    guess = list(guess)  # Corrigido: você quer usar 'guess' como argumento, não 'current_Guess'
    for i in range(len(hw)):
        if guess[i] == hw[i]:
            continue
        else:
            guess[i] = random.choice(string.ascii_letters + " ")
    return "".join(guess)  # Corrigido: 'return' deve estar fora do loop


def main():
    current_Guess = "".join(random.choice(string.ascii_letters + " ") for i in range(len(hw)))  # Inicializa com uma tentativa aleatória
    
    while True:
        print(current_Guess)
        current_Guess = random_w(hw, current_Guess)  # Atualiza a tentativa usando a função 'random_w'
        
        if current_Guess == hw:
            print('''

With that; I say... *huf *huf

Hello World!!!
''')
            break


if __name__ == "__main__":
    main()
