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
    print('The host announces:\n"Answer ALL TEN QUESTIONS CORRECTLY or...\nyou FAIL THE QUIZ and something REALLY BAD will happen to you.\nDO YOU WANT TO PLAY OR NOT?"\n')
    time.sleep(0.5)
    print('Do you want to play or not? Type "y" for yes or "n" for no.')
    start_quiz=input()
    if start_quiz.lower() == 'y':
        print('Your first question is: This is a method of scamming characterized by\npersuasive or urgent messages through call, text, or email. What is this?\n')
        response=input('Your options are:\nA: freaking\nB: fracking\nC: fishing\nD: phishing\n\nYour answer is:')
        if response.lower() == 'd' or response.lower() == 'phishing':
            print("\033[H\033[J",end="")
            typing_effect('Correct answer!\n\nNow for your second question:')
            response=input('Your options are:\nA: \nB: \nC: \nD: =\n\nYour answer is:')
            if response.lower() == '' or response.lower() == '':
                print("\033[H\033[J",end="")
                typing_effect('Correct answer!\n\nNow for your third question:')
                response=input('Your options are:\nA: \nB: \nC: \nD: =\n\nYour answer is:')
                if response.lower() == '' or response.lower() == '':
                    print("\033[H\033[J",end="")
                    typing_effect('Correct answer!\n\nNow for your fourth question:')
                    response=input('Your options are:\nA: \nB: \nC: \nD: =\n\nYour answer is:')
                    if response.lower() == '' or response.lower() == '':
                        print("\033[H\033[J",end="")
                        typing_effect('Correct answer!\n\nNow for your fifth question:')
                    else:
                        print("\033[H\033[J",end="")
                        typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nYou are th.')
                        print('YOU DIED!')
                        restart=input('Type "R" or "r" to restart:')
                        if restart.lower() == 'r':
                            game_start()
                else:
                    print("\033[H\033[J",end="")
                    typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nYou are th.')
                    print('YOU DIED!')
                    restart=input('Type "R" or "r" to restart:')
                    if restart.lower() == 'r':
                        game_start()
            else:
                print("\033[H\033[J",end="")
                typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nYou are th.')
                print('YOU DIED!')
                restart=input('Type "R" or "r" to restart:')
                if restart.lower() == 'r':
                    game_start()
        else:
            print("\033[H\033[J",end="")
            typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nYou are sent back home and you open your bank account to find that there are ZERO DOLLARS LEFT!')
            print('YOU LOSE!')
            restart=input('Type "R" or "r" to restart:')
            if restart.lower() == 'r':
                game_start()
    else:
        typing_effect("The announcer pulls out a gun and shoots you.\n")
        typing_effect('YOU DIED!\n')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
                game_start()
game_start()
        
