import os
import record_results as r
import graph_data as g

control_action = 1

while control_action != 0:
    os.system('clear')
    print "PERSONALITY AND ATTRACTION SURVEY MANAGEMENT"
    print "============================================="
    print "=         Record New Results < R >          ="
    print "=          Generate Graphs < G >            ="
    print "=              Quit  < Q >                  ="
    print "============================================="
    control_action = raw_input("=  Command: ")


    if control_action == 'Q':
        os.system('clear')
        control_action = 0

    elif control_action == 'R':
        r.results_control_menu("personality_results.txt")

    elif control_action ==  'G':
        g.graph_personality_data("personality_results.txt")

    else:
        control_action = -1


