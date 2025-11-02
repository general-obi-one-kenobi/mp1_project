import sys
import time
def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
def game_start():
    print("\033[H\033[J",end="")
    print('You wake up to find yourself in a strange room wearing only your pajamas and\nnone of the valuables you keep on your person. You look around and find\nthat you are in a trivia game run by black-hat hackers\nwith ties to the mafia. You wonder: "Is this because I helped stop some\nransomware?"\n')
    time.sleep(0.5)
    print('The host announces:\n"Answer ALL TEN QUESTIONS CORRECTLY or...\nyou FAIL THE QUIZ and something REALLY BAD will happen to you.\nDO YOU WANT TO PLAY OR NOT?"\n')
    time.sleep(0.5)
    print('Do you want to play or not? Type "y" for yes or "n" for no.')
    start_quiz=input()
    if start_quiz.lower() == 'y':
        print('You must respond only with the letter of your answer choice.')
        question_1()
    else:
        print("The announcer takes out a golden Audemars Piguet watch from his pocket.\nYou recognize it as YOUR AP Royal Oak that you received as a birthday\ngift from your best friend. You watch sadly as he sells the watch to a\nwealthy audience member for a large sum of money.\n")
        print('YOU LOSE!\n')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
                game_start()
def question_1():
    typing_effect('\nYour first question: This is a method of scamming characterized by\npersuasive or urgent messages through call, text, or email. What is this?\n')
    response=input('Your options are:\nA: freaking\nB: fracking\nC: fishing\nD: phishing\n\nYour answer is: ')
    if response.lower() == 'd':
        print("\033[H\033[J",end="")
        question_2()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nYou are sent back home and you open your bank account to find that there are ZERO DOLLARS LEFT!')
        print('YOU LOSE!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_2():
    typing_effect('Correct answer!\n\nNow for your second question: What component of a computer is responsible for executing instructions and performing calculations?\n')
    response=input('Your options are:\nA: Hard Disk Drive\nB: Motherboard\nC: CPU\nD: RAM\nYour answer is: ')
    if response.lower() == 'c':
        print("\033[H\033[J",end="")
        question_3()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nThe announcer wheels in your expensive gaming setup on a rolling table.\nYou watch in horror as a large man walks on stage with a sledgehammer and destroys your setup\n')
        print('YOU LOSE!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_3():
    typing_effect("Correct answer!\n\nNow for your third question: Which data type is best suited for storing a person's age in a programming language?")
    response=input('Your options are:\nA: String\nB: Integer\nC: Boolean\nD: Floating point\n\nYour answer is: ')
    if response.lower() == 'b':
        print("\033[H\033[J",end="")
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ! \nThe announcer brings in your LEGO UCS Millennium Falcon on a rolling\ntable. You watch as the announcer picks up the model and throws it on the\nground, causing the model to break.')
        print('YOU LOSE!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
game_start()
