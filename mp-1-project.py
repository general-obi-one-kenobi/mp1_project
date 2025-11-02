import sys
import time
def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
def start_game():
    print("\033[H\033[J",end="")
    print('This is a game about a wealthy white-hat hacker who is forced to complete\na dangerous quiz. Type "start" and press enter to start the game.')
    start_input=input('Type "start" here and press enter: ')
    if start_input.lower() == 'start':
        start()
    else:
        start_game()
def start():
    print("\033[H\033[J",end="")
    print('You wake up to find yourself strapped to a chair in a strange room\nwearing only your pajamas and none of the valuables you keep on your\nperson. You look around and find that you are in a trivia game run by\nblack-hat hackers with ties to the mafia. You wonder: "Is this because I helped stop some ransomware?"\n')
    time.sleep(0.5)
    print('The host announces:\n\n"Answer ALL TEN QUESTIONS CORRECTLY or...\nyou FAIL THE QUIZ and something REALLY BAD will happen to you.\nDO YOU WANT TO PLAY OR NOT?"\n')
    time.sleep(0.5)
    print('Do you want to play or not? Type "y" for yes or "n" for no. Press enter\nto confirm answer selection for all questions including this one.\n')
    start_quiz=input()
    if start_quiz.lower() == 'y':
        print('\nYou must respond only with the letter of your answer choice.')
        question_1()
    else:
        print("\nThe announcer takes out a golden Audemars Piguet watch from his pocket.\nYou recognize it as YOUR AP Royal Oak that you received as a birthday\ngift from your best friend. You watch sadly as he sells the watch to a\nwealthy audience member for a large sum of money.\n")
        print('YOU LOSE!\n')
        restart=input('Press enter to restart: ')
        if restart.lower() == 'r':
                start()
        else:
            start()
def question_1():
    print('\nYour first question: This is a method of scamming characterized by\npersuasive or urgent messages through call, text, or email. What is this?\n')
    response=input('Your options are:\nA: freaking\nB: fracking\nC: fishing\nD: phishing\n\nYour answer is: ')
    if response.lower() == 'd':
        print("\033[H\033[J",end="")
        question_2()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nYou are sent back home and you open your bank account to find that there are ZERO DOLLARS LEFT!')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_2():
    print('Correct answer!\n\nNow for your second question: What component of a computer is responsible\nfor executing instructions and performing calculations?\n')
    response=input('Your options are:\nA: Hard Disk Drive\nB: Motherboard\nC: CPU\nD: RAM\nYour answer is: ')
    if response.lower() == 'c':
        print("\033[H\033[J",end="")
        question_3()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nThe announcer wheels in your expensive gaming setup on a rolling table.\nYou watch in horror as a large man walks on stage with a sledgehammer and destroys your setup.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
def question_3():
    print("Correct answer!\n\nNow for your third question: Which data type is best suited for storing a\nperson's age in a programming language?\n")
    response=input('Your options are:\nA: String\nB: Integer\nC: Boolean\nD: Floating point\n\nYour answer is: ')
    if response.lower() == 'b':
        print("\033[H\033[J",end="")
        question_4()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nThe announcer brings in your LEGO UCS Millennium Falcon on a rolling\ntable. You watch as the announcer picks up the model and throws it on the\nground, causing the model to break.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_4():
    print("Correct answer!\n\nNow for your fourth question: Which protocol is primarily responsible for\ntransmitting web pages across the internet?\n")
    response=input('Your options are:\nA: Hypertext Transfer Protocol (HTTP)\nB: File Transfer Protocol (FTP)\nC: Simple Mail Transfer Protocol (SMTP)\nD: Transmission Control Protocol (TCP)\n\nYour answer is: ')
    if response.lower() == 'a':
        print("\033[H\033[J",end="")
        question_5()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer rolls in your Lamborghini Urus SUV and sets it on fire.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_5():
    print("Correct answer!\n\nNow for your fifth question: What is the decimal equivalent of the binary\nnumber 1011?\n")
    response=input('Your options are:\nA: 11\nB: 67\nC: 45 \nD: 12\n\nYour answer is: ')
    if response.lower() == 'a':
        print("\033[H\033[J",end="")
        question_6()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer picks up your phone and throws it on the floor. He then pulls out a gun and shoots the phone until the screen breaks.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_6():
    print("Correct answer!\n\nNow for your sixth question: In computer science, what term is used to\ndescribe how the execution time or memory requirements of an algorithm\nchange as the input size grows?\n")
    response=input('Your options are:\nA: Recursion\nB: Abstraction\nC: Debugging\nD: Complexity\n\nYour answer is: ')
    if response.lower() == 'd':
        print("\033[H\033[J",end="")
        question_7()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer connects his computer to the quiz screen and makes you watch as he hacks into your Google account. He then deletes all of your files and projects.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_7():
    print("Correct answer!\n\nNow for your seventh question: If a program's code contains an IF\nstatement, and the condition inside the IF is False, what happens?\n")
    response=input('Your options are:\nA: The code under the IF statement runs anyway\nB: The program ends\nC: The program skips to the next code block after the IF statement\nD: The previous code lines loop until the IF statement is true\n\nYour answer is: ')
    if response.lower() == 'c':
        print("\033[H\033[J",end="")
        question_8()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer brings all of your robotics projects into the room and throws them into a trash compactor, which crushes the robots.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_8():
    print("Correct answer!\n\nNow, for the last three questions, let's up the ante a little bit.\nFor your eighth question: A malicious program disguised as a legitimate\none (like a free game or utility) is commonly known as what type of malware?\n")
    response=input('Your options are:\nA: Trojan horse\nB: Rootkit\nC: Worm\nD: Spyware\n\nYour answer is: ')
    if response.lower() == 'a':
        print("\033[H\033[J",end="")
        question_9()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\nThe announcer projects a live feed of your house on the screen and makes you watch as his associates set it on fire. The house is empty, so no one is hurt.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_9():
    print("Correct answer!\n\nNow for your ninth question: What is the main function of an operating\nsystem (OS)?\n")
    response=input("Your options are:\nA: Storing the user's files\nB: Connecting the computer to the internet\nC: Allowing all of a computer's parts to communicate\nD: Allowing hackers to access your files\n\nYour answer is: ")
    if response.lower() == 'c':
        print("\033[H\033[J",end="")
        question_10()
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer releases you from the chair and drags your dog into the room. He then pulls his gun out of his pocket and shoots the dog.\nYou begin to cry as the injured dog crawls tries to crawl towards you.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
def question_10():
    print("Correct answer!\n\nNow for your tenth and final question. Answer carefully, because this\nquestion is the most unforgiving of them all: If a FOR loop is set to\nexecute 5 times, and an IF statement inside the loop causes a break\ncommand to execute on the 3rd iteration, how many times will the loop's body complete execution?\n")
    response=input('Your options are:\nA: 2\nB: 3\nC: 6\nD: 7\n\nYour answer is: ')
    if response.lower() == 'a':
        print("\033[H\033[J",end="")
        typing_effect("'Y-you did it. I-I can't believe it. You actually did it. You answered\nall of the questions correctly. YOU WON! Here is a million dollars for\nyour ability to keep a cool head under pressure.' You are released from the chair and are given a check for a million dollars. You are then sent back home to enjoy your life.\n")
        print('YOU WIN THE QUIZ GAME!\nRestart by refreshing the console and give this to a friend to try.')
    else:
        print("\033[H\033[J",end="")
        typing_effect('Wrong answer. YOU FAILED THE QUIZ!\n The announcer releases you from the chair and drags your dog into the room. He then pulls his gun out of his pocket and shoots you. You watch your dog crying as you lose consciousness.\n')
        print('YOU LOSE!')
        restart=input('Press enter to restart: ')
        if restart.lower() == '':
            start()
        else:
            start()
start_game()
