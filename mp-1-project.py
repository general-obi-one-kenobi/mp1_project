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
    print('Do you want to play or not? Type "y" for yes or "n" for no.\n')
    start_quiz=input()
    if start_quiz.lower() == 'y':
        print('You must respond only with the letter of your answer choice.')
        question_1()
    else:
        print("\nThe announcer takes out a golden Audemars Piguet watch from his pocket.\nYou recognize it as YOUR AP Royal Oak that you received as a birthday\ngift from your best friend. You watch sadly as he sells the watch to a\nwealthy audience member for a large sum of money.\n")
        print('YOU LOST!\n')
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
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nYou are sent back home and you open your bank account to find that there are ZERO DOLLARS LEFT!')
        print('YOU LOST!')
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
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nThe announcer wheels in your expensive gaming setup on a rolling table.\nYou watch in horror as a large man walks on stage with a sledgehammer and destroys your setup.\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_3():
    typing_effect("Correct answer!\n\nNow for your third question: Which data type is best suited for storing a person's age in a programming language?")
    response=input('Your options are:\nA: String\nB: Integer\nC: Boolean\nD: Floating point\n\nYour answer is: ')
    if response.lower() == 'b':
        print("\033[H\033[J",end="")
        question_4()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nThe announcer brings in your LEGO UCS Millennium Falcon on a rolling\ntable. You watch as the announcer picks up the model and throws it on the\nground, causing the model to break.\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_4():
    typing_effect("Correct answer!\n\nNow for your fourth question: Which protocol is primarily responsible for transmitting web pages across the internet?")
    response=input('Your options are:\nA: Hypertext Transfer Protocol (HTTP)\nB: File Transfer Protocol (FTP)\nC: Simple Mail Transfer Protocol (SMTP)\nD: Transmission Control Protocol (TCP)\n\nYour answer is: ')
    if response.lower() == 'b':
        print("\033[H\033[J",end="")
        question_5()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer rolls in your Lamborghini Urus SUV and sets it on fire.\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_5():
    typing_effect("Correct answer!\n\nNow for your fifth question: What is the decimal equivalent of the binary number 1011?")
    response=input('Your options are:\nA: 11\nB: 67\nC:45 \nD: 12\n\nYour answer is: ')
    if response.lower() == 'a':
        print("\033[H\033[J",end="")
        question_6()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer picks up your phone and throws it on the floor. He then pulls out a gun and shoots the phone until the screen breaks.\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_6():
    typing_effect("Correct answer!\n\nNow for your sixth question: In computer science, what term is used to describe how the execution time or memory requirements of an algorithm change as the input size grows??")
    response=input('Your options are:\nA: Recursion\nB: Abstraction\nC: Debugging\nD: Complexity\n\nYour answer is: ')
    if response.lower() == 'd':
        print("\033[H\033[J",end="")
        question_7()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer connects his computer to the quiz screen and makes you watch as he hacks into your Google account. He then deletes all of your files.\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_7():
    typing_effect("Correct answer!\n\nNow for your seventh question: 
If a program's code contains an IF statement, and the condition inside the IF is False, what happens??")
    response=input('Your options are:\nA: The code under the IF statement runs anyway\nB: The program ends\nC: The program skips to the next code block after the IF statement\nD: The previous code lines loop until the IF statement is true\n\nYour answer is: ')
    if response.lower() == 'c':
        print("\033[H\033[J",end="")
        question_8()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_8():
    typing_effect("Correct answer!\n\nNow for your eighth question: ?")
    response=input('Your options are:\nA: \nB: \nC: \nD: \n\nYour answer is: ')
    if response.lower() == '':
        print("\033[H\033[J",end="")
        question_9()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_9():
    typing_effect("Correct answer!\n\nNow for your ninth question: ?")
    response=input('Your options are:\nA: \nB: \nC: \nD: \n\nYour answer is: ')
    if response.lower() == '':
        print("\033[H\033[J",end="")
        question_10()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
def question_10():
    typing_effect("Correct answer!\n\nNow for your tenth and final question: ?")
    response=input('Your options are:\nA: \nB: \nC: \nD: \n\nYour answer is: ')
    if response.lower() == '':
        print("\033[H\033[J",end="")
        print("Y-you did it. I-I can't believe it. You actually did it. You answered all of the questions correctly.\nYOU WON! Here is a million dollars.\n")
        print('YOU WON THE QUIZ GAME!\nRestart by refreshing the console and give this to a friend to try.')
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer\n')
        print('YOU LOST!')
        restart=input('Type "R" or "r" to restart:')
        if restart.lower() == 'r':
            game_start()
game_start()
