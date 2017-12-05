import numpy as np
import matplotlib.pyplot as plt

def build_plot(chart_title, n, a, c, e, o):
    # data to plot
    n_groups = 3


    # create plot
    fig, ax = plt.subplots()
    index = np.arange(3)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, n, bar_width,
                     alpha=opacity,
                     color='y',
                     label='Neuroticism')

    rects2 = plt.bar(index + bar_width, a, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Agreeableness')

    rects3 = plt.bar(index + bar_width*2, c, bar_width,
                     alpha=opacity,
                     color='m',
                     label='Conscientiousness')

    rects4 = plt.bar(index + bar_width*3, e, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Extraversion')

    rects5 = plt.bar(index + bar_width*4, o, bar_width,
                     alpha=opacity,
                     color='c',
                     label='Openness')

    plt.xlabel('Score in ' + chart_title)
    plt.ylabel('Average Interest in Personality Dimension')
    plt.title('Dimension: ' + chart_title)
    plt.xticks(index + bar_width, ('0-33.3', '33.4-66.6', '66.7-100'))
    plt.legend()

    plt.tight_layout()
    plt.show()

def normalize_data(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [x.strip('\n') for x in lines]
    for x in range(0, len(lines)):
        list = lines[x].split(',')
        list = [float(z) for z in list]
        normal_result = [0] * 10
        normal_result[0] = list[0] + list[1] + list[2] + list[3] + list[4]
        normal_result[1] = reverse_score(list[5]) + list[6] + list[7] + reverse_score(list[8]) + reverse_score(list[9])
        normal_result[2] = list[10] + reverse_score(list[11]) + list[12] + list[13] + list[14]
        normal_result[3] = list[15] + reverse_score(list[16]) + list[17] + list[18] + list[19]
        normal_result[4] = list[20] + list[21] + reverse_score(list[22]) + list[23] + list[24]
        normal_result[5] = list[25] + list[26] + list[27] + reverse_score(list[28]) + list[29]
        normal_result[6] = reverse_score(list[30]) + reverse_score(list[31]) + list[32] + reverse_score(list[33]) + reverse_score(list[34])
        normal_result[7] = list[35] + reverse_score(list[36]) + list[37] + reverse_score(list[38]) + list[39]
        normal_result[8] = reverse_score(list[40]) + list[41] + list[42] + reverse_score(list[43]) + reverse_score(list[44])
        normal_result[9] = list[45] + reverse_score(list[46]) + list[47] + reverse_score(list[48]) + reverse_score(list[49])

        for z in range(0,10):
            normal_result[z] = normal_result[z] * 5 - 25

        lines[x] = normal_result
        #print normal_result


    number_of_results = len(lines)
    return group_by_range(lines, number_of_results)

    raw_input("ENTER")

def reverse_score(answer):
    if answer == 1.0:
        return 5.0
    elif answer == 2.0:
        return 4.0
    elif answer == 3.0:
        return 3.0
    elif answer == 4.0:
        return 2.0
    elif answer == 5.0:
        return 1.0
    else: return 0

def group_by_range(results, n):
    nL = [0] * 5
    cnL = 0
    nM = [0] * 5
    cnM = 0
    nH = [0] * 5
    cnH = 0
    aL = [0] * 5
    caL = 0
    aM = [0] * 5
    caM = 0
    aH = [0] * 5
    caH = 0
    cL = [0] * 5
    ccL = 0
    cM = [0] * 5
    ccM = 0
    cH = [0] * 5
    ccH = 0
    eL = [0] * 5
    ceL = 0
    eM = [0] * 5
    ceM = 0
    eH = [0] * 5
    ceH = 0
    oL = [0] * 5
    coL = 0
    oM = [0] * 5
    coM = 0
    oH = [0] * 5
    coH = 0

    for x in results:
        #print x
        if x[0] <= 33.3:
            nL = sum_interests(nL, x)
            cnL += 1
        elif x[0] >= 33.4 and x[0] <= 66.6:
            nM = sum_interests(nM, x)
            cnM += 1
        else:
            nH = sum_interests(nH, x)
            cnH += 1

        if x[1] <= 33.3:
            aL = sum_interests(aL, x)
            caL += 1
        elif x[1] >= 33.4 and x[1] <= 66.6:
            aM = sum_interests(aM, x)
            caM += 1
        else:
            aH = sum_interests(aH, x)
            caH += 1

        if x[2] <= 33.3:
            cL = sum_interests(cL, x)
            ccL += 1
        elif x[2] >= 33.4 and x[2] <= 66.6:
            cM = sum_interests(cM, x)
            ccM += 1
        else:
            cH = sum_interests(cH, x)
            ccH += 1

        if x[3] <= 33.3:
            eL = sum_interests(eL, x)
            ceL += 1
        elif x[3] >= 33.4 and x[3] <= 66.6:
            eM = sum_interests(eM, x)
            ceM += 1
        else:
            eH = sum_interests(eH, x)
            ceH += 1

        if x[4] <= 33.3:
            oL = sum_interests(oL, x)
            coL += 1
        elif x[4] >= 33.4 and x[4] <= 66.6:
            oM = sum_interests(oM, x)
            coM += 1
        else:
            oH = sum_interests(oH, x)
            coH += 1

    nL = average_interest_sums(nL, cnL)
    nM = average_interest_sums(nM, cnM)
    nH = average_interest_sums(nH, cnH)
    aH = average_interest_sums(aH, caH)
    aM = average_interest_sums(aM, caM)
    aL = average_interest_sums(aL, caL)
    cL = average_interest_sums(cL, ccL)
    cM = average_interest_sums(cM, ccM)
    cH = average_interest_sums(cH, ccH)
    eL = average_interest_sums(eL, ceL)
    eM = average_interest_sums(eM, ceM)
    eH = average_interest_sums(eH, ceH)
    oL = average_interest_sums(oL, coL)
    oM = average_interest_sums(oM, coM)
    oH = average_interest_sums(oH, coH)


    low=[None] * 5
    med=[None] * 5
    high = [None] * 5

    low[0] = nL
    low[1] = aL
    low[2] = cL
    low[3] = eL
    low[4] = oL

    med[0] = nM
    med[1] = aM
    med[2] = cM
    med[3] = eM
    med[4] = oM

    high[0] = nH
    high[1] = aH
    high[2] = cH
    high[3] = eH
    high[4] = oH

    return low, med, high


def sum_interests(group, result):
    group[0] += result[5]
    group[1] += result[6]
    group[2] += result[7]
    group[3] += result[8]
    group[4] += result[9]
    return group

def average_interest_sums(interest_group, count):
    if count > 0:
        for x in range(0, len(interest_group)):
            interest_group[x] = interest_group[x] / count
    return interest_group

def graph_personality_data(filename):
    low, med, high = normalize_data(filename)

    title = "Neuroticism"
    n =(low[0][0],med[0][0],high[0][0])
    a =(low[0][1],med[0][1],high[0][1])
    c =(low[0][2],med[0][2],high[0][2])
    e =(low[0][3],med[0][3],high[0][3])
    o =(low[0][4],med[0][4],high[0][4])
    build_plot(title, n, a, c, e, o)

    title = "Agreeableness"
    n =(low[1][0],med[1][0],high[1][0])
    a =(low[1][1],med[1][1],high[1][1])
    c =(low[1][2],med[1][2],high[1][2])
    e =(low[1][3],med[1][3],high[1][3])
    o =(low[1][4],med[1][4],high[1][4])
    build_plot(title, n, a, c, e, o)

    title = "Conscientiousness"
    n =(low[2][0],med[2][0],high[2][0])
    a =(low[2][1],med[2][1],high[2][1])
    c =(low[2][2],med[2][2],high[2][2])
    e =(low[2][3],med[2][3],high[2][3])
    o =(low[2][4],med[2][4],high[2][4])
    build_plot(title, n, a, c, e, o)

    title = "Extraversion"
    n =(low[3][0],med[3][0],high[3][0])
    a =(low[3][1],med[3][1],high[3][1])
    c =(low[3][2],med[3][2],high[3][2])
    e =(low[3][3],med[3][3],high[3][3])
    o =(low[3][4],med[3][4],high[3][4])
    build_plot(title, n, a, c, e, o)

    title = "Openness"
    n =(low[4][0],med[4][0],high[4][0])
    a =(low[4][1],med[4][1],high[4][1])
    c =(low[4][2],med[4][2],high[4][2])
    e =(low[4][3],med[4][3],high[4][3])
    o =(low[4][4],med[4][4],high[4][4])
    build_plot(title, n, a, c, e, o)
