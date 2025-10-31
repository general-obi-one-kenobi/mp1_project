import sys
import time
def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

typing_effect('You wake up to find yourself in a trivia game run by black-hat hackers\nwith ties to the mafia. You wonder: "Is this because I helped stop some\nransomware?"\n\nThe announcer states:\nAnswer all ten questions correctly or...\nyou FAIL THE QUIZ and something REALLY BAD will happen to you\n\nYour first question is: This is a method of scamming characterized by persuasive or urgent messages through call, text, or email. What is this?\n')
print("\033[H\033[J",end="")
response1=input('Your options are:\nA: freaking\nB: fracking\nC: fishing\nD: phishing\n\nYour answer is: ')
if response1 == 'D' or 'd' or 'phishing':
    print("\033[H\033[J",end="")
    typing_effect('Correct answer!\n\nNow for question number two.')
else:
    print("\033[H\033[J",end="")
    typing_effect('\nWrong answer. YOU FAILED THE QUIZ! \nYou are sent back home and you open your bank account to find that there are ZERO DOLLARS LEFT')
