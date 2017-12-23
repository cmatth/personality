import numpy as np
import matplotlib.pyplot as plt

# py.test -f --cov . test/

number_of_results = 0
reversed_answers = [6,9,10,12,17,23,29,31,32,34,35,37,39,41,44,45,47,49,50]

def build_plot(fig, position, chart_title, scores):
    # data to plot
    n_groups = 3


    # create plot
    fig.add_subplot(2,3,position)
    index = np.arange(3)
    bar_width = 0.15
    opacity = 0.8

    rects1 = plt.bar(index, scores[0], bar_width,
                     alpha=opacity,
                     color='y',
                     label='Neuroticism')

    rects2 = plt.bar(index + bar_width, scores[1], bar_width,
                     alpha=opacity,
                     color='g',
                     label='Agreeableness')

    rects3 = plt.bar(index + bar_width*2, scores[2], bar_width,
                     alpha=opacity,
                     color='m',
                     label='Conscientiousness')

    rects4 = plt.bar(index + bar_width*3, scores[3], bar_width,
                     alpha=opacity,
                     color='b',
                     label='Extroversion')

    rects5 = plt.bar(index + bar_width*4, scores[4], bar_width,
                     alpha=opacity,
                     color='c',
                     label='Openness')

    plt.xlabel('Score in ' + chart_title)
    plt.ylabel('Average Interest in Personality Dimension')
    plt.title('Dimension: ' + chart_title)
    plt.xticks(index + bar_width, ('0-33.3', '33.4-66.6', '66.7-100'))

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

    fig = plt.figure()

    title = "Neuroticism"
    scores = separate_by_trait_and_score_group(0,low,med,high)
    build_plot(fig, 1, title, scores)

    title = "Agreeableness"
    scores = separate_by_trait_and_score_group(0, low, med, high)
    build_plot(fig, 2, title, scores)

    title = "Conscientiousness"
    scores = separate_by_trait_and_score_group(0, low, med, high)
    build_plot(fig, 3, title, scores)

    title = "Extroversion"
    scores = separate_by_trait_and_score_group(0, low, med, high)
    build_plot(fig, 4, title, scores)

    title = "Openness"
    scores = separate_by_trait_and_score_group(0, low, med, high)
    build_plot(fig, 5, title, scores)

    global number_of_results
    title = "Desirability of Personality Traits (n = " + str(number_of_results) + ")"
    n =(low[0][0]+med[0][0]+high[0][0]) / 3
    a =(low[1][1]+med[1][1]+high[1][1]) / 2
    c =(low[2][2]+med[2][2]+high[2][2]) / 3
    e =(low[3][3]+med[3][3]+high[3][3]) / 3
    o =(low[4][4]+med[4][4]+high[4][4]) / 3
    all = (n, a, c, e, o)
    overall_interests_plot(fig, 6, title, all)
    plt.show()

def overall_interests_plot(fig, position, chart_title, all):
    # create plot
    fig.add_subplot(2,3,6)
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

def separate_by_trait_and_score_group(trait_index, low, med, high):
    n =(low[trait_index][0],med[trait_index][0],high[trait_index][0])
    a =(low[trait_index][1],med[trait_index][1],high[trait_index][1])
    c =(low[trait_index][2],med[trait_index][2],high[trait_index][2])
    e =(low[trait_index][3],med[trait_index][3],high[trait_index][3])
    o =(low[trait_index][4],med[trait_index][4],high[trait_index][4])
    return (n,a,c,e,o)