def get_guess():
    guess = int(input("Enter a guest: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        return "Correct!"
    else:
        return "Incorrect!"

print(main())