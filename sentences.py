import random

quantities = [1,2,3,4]
tenses = ["past","future","present"]
quantity = random.choice(quantities)
tense = random.choice(tenses)

def main():

    get_determiner(quantity)
    get_noun(quantity)
    get_verb(quantity,tense)
    get_preposition()
    get_prepositional_phrase(quantity)
    get_adjective()
    get_adverb()
    get_another_prepositional_phrase(quantity)
    

def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    cap_word = word.capitalize()
    return cap_word
  


def get_noun(quantity):

    if quantity ==1:
        words = [ "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = [ "birds", "boys", "cars", "cats", "children",  "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == ("past"):
        words =[ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]

    elif tense =="present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = [  "drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]

    elif tense =="future":
        words= [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk","will walk",
         "will write"]

    word = random.choice(words)
    return word

def get_preposition():
    
    words = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):

    det=get_determiner(quantity)
    noun_1 = get_noun(quantity)
    preposition = get_preposition()
    verb = get_verb(quantity,tense)
    noun_2 = get_noun(quantity)
    print(f'{det} {noun_1} {verb} {preposition} {noun_2}' )


def get_adjective():

    words = ["good","bad","cute","smart","ugly","interesting","funny","noisy","big","soft","great","hard","cold"]

    word = random.choice(words)

    return word

def get_adverb():

    words =["suddenly","carefully","rapidly","slowly","proudly","humbly","seriously","unconsciously"]
   
    word = random.choice(words)

    return word


def get_another_prepositional_phrase(quantity):

    det=get_determiner(quantity)
    det_2 = get_determiner(quantity)
    noun_1 = get_noun(quantity)
    preposition = get_preposition()
    preposition_2 = get_preposition()
    verb = get_verb(quantity,tense)
    noun_2 = get_noun(quantity)
    noun_3 = get_noun(quantity)
    adj = get_adjective()
    adv = get_adverb()

    print(f'{det} {adj} {noun_1} {preposition_2} {det_2.lower()} {noun_3} {verb} {adv} {preposition} {noun_2}' )


    


main()

