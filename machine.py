emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh hello")

def say(phrase):
    print(f"{phrase} {emoticon}")

main()