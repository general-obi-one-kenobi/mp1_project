import sys
import time
def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
def game_start():
    print("\033[H\033[J",end="")
    print('You wake up to find yourself in a trivia game run by black-hat hackers\nwith ties to the mafia. You wonder: "Is this because I helped stop some\nransomware?"\n')
    time.sleep(0.5)
    print('The announcer states:\nAnswer ALL TEN QUESTIONS CORRECTLY or...\nyou FAIL THE QUIZ and something REALLY BAD will happen to you\n')
    time.sleep(0.5)
    print('Your first question is: This is a method of scamming characterized by\npersuasive or urgent messages through call, text, or email. What is this?\n')
    response1=input('Your options are:\nA: freaking\nB: fracking\nC: fishing\nD: phishing\n\nYour answer is:')
    if response1.lower() == 'd' or response1 == 'phishing':
        print("\033[H\033[J",end="")
        typing_effect('Correct answer!\n\nNow for your second question:')
        response2=input('Your options are:\nA: \nB: \nC: \nD: \n\nYour answer is:')
    else:
        print("\033[H\033[J",end="")
        typing_effect('\nWrong answer. YOU FAILED THE QUIZ! \nYou are sent back home and you open your bank account to find that there are ZERO DOLLARS LEFT!')
        print('YOU LOSE!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
game_start()
        
