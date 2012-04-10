from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"
    
def test_peek():
    #one word
    line1 = "bear"
    word_tuples1 = lexicon.scan(line1)
    word_type1 = parser.peek(word_tuples1)
    assert_equal("noun", word_type1)

    #multiple words
    #actually this only check the first word i.e. bear
    line2 = "bear ate the princess"
    word_tuples2 = lexicon.scan(line2)
    assert_equal("noun", parser.peek(word_tuples2)) 

def test_match():
    #one word
    line1 = "bear"
    word_tuples1 = lexicon.scan(line1)
    assert_equal("bear", parser.match(word_tuples1, 'noun')[1])
    #Here we should get a None for any type since there is nothing in the word_list
    assert_equal(None, parser.match(word_tuples1, 'noun'))

    #multiple words
    #note that parser.match will 'cut' tupples one by one
    line2 = "bear eat the princess"
    word_tuples2 = lexicon.scan(line2)
    assert_equals(4, len(word_tuples2))
    assert_equal("bear", parser.match(word_tuples2, "noun")[1])
    assert_equals(3, len(word_tuples2))
    assert_equal("eat", parser.match(word_tuples2, "verb")[1])
    assert_equals(2, len(word_tuples2))
    assert_equal("the", parser.match(word_tuples2, 'stop')[1])
    assert_equals(1, len(word_tuples2))
    assert_equal("princess", parser.match(word_tuples2, 'noun')[1])
    assert_equals(0, len(word_tuples2))
    
def test_skip():
    #one word
    line1 = "bear"
    word_tuples1 = lexicon.scan(line1)
    parser.skip(word_tuples1, "verb")
    assert_equal(1, len(word_tuples1))
    parser.skip(word_tuples1, 'noun')
    assert_equal(0, len(word_tuples1))

    #multiple words
    line2 = "princess eat the princess" # eww
    word_tuples2 = lexicon.scan(line2)
    assert_equal(4, len(word_tuples2))
    parser.skip(word_tuples2, "verb")
    assert_equal(4, len(word_tuples2)) # no change
    parser.skip(word_tuples2, "noun")
    assert_equal(3, len(word_tuples2)) # chopped one i.e. princess
    parser.skip(word_tuples2, "verb")
    assert_equal(2, len(word_tuples2)) # chopped one i.e. eat 
    parser.skip(word_tuples2, "verb")
    assert_equal(2, len(word_tuples2)) # chopped none  
    parser.skip(word_tuples2, "stop")
    assert_equal(1, len(word_tuples2)) # chopped one i.e. the   

    
def test_parse_sentence():
    # standard subject-verb-object
    line1 = "bear eat the princess"
    word_list1 = lexicon.scan(line1)
    parsed_sentence1 = parser.parse_sentence(word_list1)
    assert_equal("bear", parsed_sentence1.subject)
    assert_equal("eat", parsed_sentence1.verb)
    assert_equal("princess", parsed_sentence1.object)
    
    # only verb-object
    line2 = "eat the bear"
    word_list2 = lexicon.scan(line2)
    parsed_sentence2 = parser.parse_sentence(word_list2)
    assert_equal("player", parsed_sentence2.subject)
    assert_equal("eat", parsed_sentence2.verb)
    assert_equal("bear", parsed_sentence2.object)
    
    # random stop word
    line3 = "the bear eat the the princess"
    word_list3 = lexicon.scan(line3)
    parsed_sentence3 = parser.parse_sentence(word_list3)
    assert_equal("bear", parsed_sentence3.subject)
    assert_equal("eat", parsed_sentence3.verb)
    assert_equal("princess", parsed_sentence3.object)

    
def test_parse_sentence_fail():
    # incorrect subject-subject-verb-object
    line1 = "bear bear eat the princess"
    word_list1 = lexicon.scan(line1)
    assert_raises(parser.ParserError, parser.parse_sentence, word_list1)
    
    # incorrect subject-verb-verb-object
    line2 = "bear eat eat the princess"
    word_list2 = lexicon.scan(line2)
    assert_raises(parser.ParserError, parser.parse_sentence, word_list2)    


"""
    
Change the parse_ methods and try to put them into a class rather than be just methods. Which design do you like better?
Make the parser more error resistant so that you can avoid annoying your users if they type words your lexicon doesn't understand.
Improve the grammar by handling more things like numbers.
Think about how you might use this Sentence class in your game to do more fun things with a user's input.

see: 
http://readthedocs.org/docs/nose/en
"""