import random
from sentences import get_adjective, get_adverb, get_another_prepositional_phrase, get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pytest

quantities = [1,2,3,4]
tenses = ["past","future","present"]
quantity = random.choice(quantities)
tense = random.choice(tenses)

def main():
    test_get_determiner()
    test_get_noun()
    test_get_verb()
    test_get_preposition
    test_get_prepositional_phrase()
    test_get_adjective()
    test_get_adverb()
    test_get_another_prepositional_phrase()



def test_get_determiner():

    single_determiners = ["A", "One", "The"]

    for _ in range(4):

        word = get_determiner(1)

        assert word in single_determiners

   

    plural_determiners = ["Some", "Many", "The"]

    for _ in range(4):

        word = get_determiner(2)

        assert word in plural_determiners

def test_get_noun():

    single_words= [ "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_words

    plural_words = [ "birds", "boys", "cars", "cats", "children",  "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        word = get_noun(2)
        assert word in plural_words


def test_get_verb():

    past_tense_words = [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        word = get_verb(0, "past")
        assert word in past_tense_words

    present_tense_single =  ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    present_tense_multiple =  ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
         word = get_verb(1, "present")
         assert word in present_tense_single
         word = get_verb(2, "present")
         assert word in present_tense_multiple
    

    future_tense = [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk","will walk",
       "will write"]
    for _ in range(4):
         word = get_verb(1,"future")
         assert word in future_tense

def test_get_preposition():
    words = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    word = get_preposition()
    assert word in words

def test_get_prepositional_phrase():
    
    for _ in range(4):
        det=get_determiner(quantity)
        noun_1 = get_noun(quantity)
        preposition = get_preposition()
        verb = get_verb(quantity,tense)
        noun_2 = get_noun(quantity)
        
        phrases =[f'{det} {noun_1} {verb} {preposition} {noun_2}']
        phrase = get_prepositional_phrase(quantity)
        
        return phrase

    assert phrase in phrases


def test_get_adjective():

    words = ["good","bad","cute","smart","ugly","interesting","funny","noisy","big","soft","great","hard","cold"]

    word = get_adjective()
    assert word in words


def test_get_adverb():

     words =["suddenly","carefully","rapidly","slowly","proudly","humbly","seriously","unconsciously"]

     word = get_adverb()

     assert word in words
    

def test_get_another_prepositional_phrase():
    for _ in range(4):
        det=get_determiner(quantity)
        det_2 = get_determiner(quantity)
        noun_1 = get_noun(quantity)
        preposition = get_preposition()
        preposition_2 = get_preposition()
        verb = get_verb(quantity,tense)
        noun_2 = get_noun(quantity)
        noun_3 = get_noun(quantity)
    
        phrases = [f'{det} {noun_1} {preposition_2} {det_2.lower()} {noun_3} {verb} {preposition} {noun_2}' ]
        phrase = get_another_prepositional_phrase(quantity)

        return phrase
    
    assert phrase in phrases






pytest.main(["-v", "--tb=line", "-rN", __file__])