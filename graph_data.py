import numpy as np
import matplotlib.pyplot as plt


number_of_results = 0
reversed_answers = [6,9,10,12,17,23,29,31,32,34,35,37,39,41,44,45,47,49,50]

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
                     label='Extroversion')

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
        raw_results = file.readlines()
        raw_results = [x.strip('\n') for x in raw_results]
    for x in range(0, len(raw_results)):
        list = raw_results[x].split(',')
        list = [float(z) for z in list]

        record_score = score_record(list, reversed_answers)

        for z in range(0,10):
            record_score[z] = record_score[z] * 5 - 25

        raw_results[x] = record_score
        #print record_score

    global number_of_results
    number_of_results = len(raw_results)

    return group_by_trait_and_score(raw_results)


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

    title = "Extroversion"
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

    global number_of_results
    title = "Desirability of Personality Traits (n = " + str(number_of_results) + ")"
    n =(low[0][0]+med[0][0]+high[0][0]) / 3
    a =(low[1][1]+med[1][1]+high[1][1]) / 2
    c =(low[2][2]+med[2][2]+high[2][2]) / 3
    e =(low[3][3]+med[3][3]+high[3][3]) / 3
    o =(low[4][4]+med[4][4]+high[4][4]) / 3
    all = (n, a, c, e, o)
    overall_interests_plot(title, all)

def overall_interests_plot(chart_title, all):
    n_groups = 5


    # create plot
    fig, ax = plt.subplots()
    index = np.arange(5)
    bar_width = 0.4
    opacity = 0.8

    rects1 = plt.bar(index, all, bar_width,
                     alpha=opacity,
                     color=('y','g','m','b','c'))

    plt.xlabel('Dimension')
    plt.ylabel('Average Expressed Interest')
    plt.title(chart_title)
    plt.xticks(index, ('Neuroticism', 'Agreeableness', 'Conscientiousness', 'Extroversion', 'Openness'))
    plt.legend()

    plt.tight_layout()
    plt.show()

def score_record(record, rev_score):
    composite_scores = [0] * 10
    for x in range(0,len(record),5):
        for y in range(0,5):
            if (x + y + 1) in rev_score:
                composite_scores[x / 5] += reverse_score(record[x + y])
            else:
                composite_scores[x / 5] += record[x + y]
    return composite_scores

def group_by_trait_and_score(results):
    low  = [[0 for i in range(5)] for j in range(5)]
    med  = [[0 for i in range(5)] for j in range(5)]
    high = [[0 for i in range(5)] for j in range(5)]

    low_counts  = [0] * 5
    med_counts  = [0] * 5
    high_counts = [0] * 5

    for result in results:
        for x in range(0,5):
            if result[x] <= 33.3:
                low[x] = sum_interests(low[x], result)
                low_counts[x] += 1
            elif result[x] > 66.6:
                high[x] = sum_interests(high[x], result)
                high_counts[x] += 1
            else:
                med[x] = sum_interests(med[x], result)
                med_counts[x] += 1

    low = average_score_group(low, low_counts)
    med = average_score_group(med, med_counts)
    high = average_score_group(high, high_counts)

    return low, med, high

def average_score_group(group, counts):
    for x in range(0,len(group)):
        group[x] = average_interest_sums(group[x], counts[x])
    return group
