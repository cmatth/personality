import os
from termcolor import colored


def results_control_menu(filename):
    control = 1
    system_message = ""

    while control != 0:
        os.system('clear')
        if system_message != "":
            print "============================================"
            print "=" + system_message
            system_message = ""
        print "============================================="
        print "=               Results Menu                ="
        print "============================================="
        print "=           Enter New Survey < 1 >          ="
        print "=        Return To Main Menu < 2 >          ="
        print "============================================="
        control = raw_input("=  Command: ")

        if control == '1':
            pass
            system_message = record_result(filename)
        if control == '2':
            control = 0
        else:
            control = -1

def record_result(filename):
    import getch
    invalid_message = colored("\nInvalid input. Answer must be 1,2,3,4,5,b,q.", "red")
    os.system('clear')
    print "============================================="
    print "=                 New Survey                ="
    print "============================================="
    print "You are about to create a new record of a"
    print "personality survey. Enter the answer given"
    print "to each question in the order they appear"
    print "on the survey. If you need to go back, type"
    print "\'b\' into the prompt and you will be returned"
    print "to the previous question. There are 50 questions in"
    print "total. If you need to quit, enter \'q\' and you"
    print "will be returned to the previous menu and the"
    print "record will not be saved.\n"
    raw_input("< PRESS ENTER TO BEGIN >")

    record = [None] * 50
    i = 1

    while i <= 50:
        global i
        os.system('clear')
        print "Enter the answers to each question (1-5)."
        print "#" + str(i) + ": ",
        input = getch.getch()

        if input == 'b':
            i -= 1
            if i < 1:
                i = 1
        elif input == 'q':
            return ""
        elif input in ['1','2','3','4','5']:
            record[i-1] = input
            i += 1
        else:
            print invalid_message
            raw_input("Press Enter to continue.")

    string = ""
    for x in range(0,49):
        string += str(record[x]) + ','
    string += str(record[49])

    with open(filename, 'a') as file:
        file.write(string + '\n')

    return "Record Saved!"



