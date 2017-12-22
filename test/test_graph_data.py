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

