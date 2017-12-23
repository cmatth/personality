import pytest
import sys
sys.path.append('/home/casey/PycharmProjects/personality_results/')
import graph_data as g

def test_reverse_score_correct_on_one_through_five():
    assert g.reverse_score(5) == 1
    assert g.reverse_score(4) == 2
    assert g.reverse_score(3) == 3
    assert g.reverse_score(2) == 4
    assert g.reverse_score(1) == 5

def test_reverse_score_returns_zero_on_invalid_input():
    assert g.reverse_score('monkey') == 0
    assert g.reverse_score([3,4,5]) == 0
    assert g.reverse_score(-1) == 0
    assert g.reverse_score(100) == 0

def test_score_record_with_reverse_scores():
    record = [4,4,1,1,1,3,4,4,1,1,4,2,5,5,5,5,2,3,5,5,5,5,3,
              4,4,1,1,2,3,1,1,1,4,1,1,4,3,2,2,3,2,4,4,2,3,4,3,4,3,2]
    questions_to_reverse = [6,9,10,12,17,23,29,31,32,34,35,37,39,41,44,45,47,49,50]
    correct_reversed = [11,21,23,22,21,8,24,16,19,18]
    assert g.score_record(record, questions_to_reverse) == correct_reversed

def test_average_interest_sums_with_group_of_four():
    interests = [4,8,12,16,20]
    count = 4
    assert g.average_interest_sums(interests,count) == [1,2,3,4,5]

def test_average_interest_group_with_empty_group():
    interests = []
    count = 4
    assert g.average_interest_sums(interests, count) == []

def test_average_interest_group_with_group_of_one():
    interests = [1,2,3,4,5]
    count = 1
    assert g.average_interest_sums(interests,count) == interests

def test_sum_interest_with_expected():
    group = [0,0,0,0,0]
    result = [0,0,0,0,0,1,1,1,1,1]
    assert g.sum_interests(group, result) == [1,1,1,1,1]

def test_group_by_trait_and_score():
    data = []
    data.append([10,10,10,10,10,1,1,1,1,1]) # low scorer
    data.append([99,99,99,99,99,1,1,1,1,1]) # high scorer
    data.append([50,50,50,50,50,1,1,1,1,1]) # med scorer
    r1, r2, r3 = g.group_by_trait_and_score(data)

    print r1
    print r2
    print r3

    assert r1[0],r1[1] == [1,1,1,1,1]
    assert r1[2],r1[3] == [1,1,1,1,1]
    assert r1[4] == [1,1,1,1,1]

    assert r2[0],r2[1] == [1,1,1,1,1]
    assert r2[2],r2[3] == [1,1,1,1,1]
    assert r2[4] == [1,1,1,1,1]

    assert r3[0],r3[1] == [1,1,1,1,1]
    assert r3[2],r3[3] == [1,1,1,1,1]
    assert r3[4] == [1,1,1,1,1]

def test_normalize_data():
    filename = "test/test_data.txt"
    low, med, high = g.normalize_data(filename)
    assert low == [[27.5, 90.0, 52.5, 67.5, 62.5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                   [15.0, 100.0, 65.0, 70.0, 75.0], [40.0, 85.0, 50.0, 65.0, 60.0]]
    assert med == [[15.0, 100.0, 65.0, 70.0, 75.0], [0, 0, 0, 0, 0], [40.0, 85.0, 50.0, 65.0, 60.0],
                   [40.0, 85.0, 50.0, 65.0, 60.0], [0, 0, 0, 0, 0]]
    assert high == [[0, 0, 0, 0, 0],
                    [23.333333333333332, 93.33333333333333, 56.666666666666664, 68.33333333333333, 66.66666666666667],
                    [15.0, 97.5, 60.0, 70.0, 70.0], [15.0, 95.0, 55.0, 70.0, 65.0], [15.0, 97.5, 60.0, 70.0, 70.0]]

def test_average_score_group():
    test = [[5 for i in range(5)] for j in range(5)]
    avg = [[1 for i in range(5)] for j in range(5)]
    counts = [5,5,5,5,5]
    assert g.average_score_group(test, counts) == avg

def test_separete_by_trait_and_score_group():
    low  = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    med  = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    high = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    expected = ((1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5))
    assert g.separate_by_trait_and_score_group(0, low, med, high) == expected
    assert g.separate_by_trait_and_score_group(1, low, med, high) == expected
    assert g.separate_by_trait_and_score_group(2, low, med, high) == expected
    assert g.separate_by_trait_and_score_group(3, low, med, high) == expected
    assert g.separate_by_trait_and_score_group(4, low, med, high) == expected

def test_build_plot():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    data = ((1,3,5),(1,3,5),(1,3,5),(1,3,5),(1,3,5))
    title = 'test'
    position = 1
    g.build_plot(fig,position,title,data)

def test_graph_personality_data():
    import matplotlib.pyplot as plt
    import time
    plt.close('all')
    g.graph_personality_data('test/test_data.txt')
    time.sleep(3)
    plt.close()
