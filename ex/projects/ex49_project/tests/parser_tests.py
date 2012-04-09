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

    #test a line with multiple words
    line2 = "princess eat the bear"
    word_tuples2 = lexicon.scan(line2)
    assert_equals(4, len(word_tuples2))
    assert_equal("princess", parser.match(word_tuples2, "noun")[1])
    assert_equal("eat", parser.match(word_tuples2, "verb")[1])
    assert_equal("the", parser.match(word_tuples2, 'stop')[1])
    assert_equal("bear", parser.match(word_tuples2, 'noun')[1])

    """
def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [  ('verb', 'go'),
                            ('verb', 'kill'),
                            ('verb', 'eat')   ])
                            
def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in off")
    assert_equal(result, [  ('stop', 'the'),
                            ('stop', 'in'),
                            ('stop', 'off')   ])
                            
def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [  ('noun', 'bear'),
                            ('noun', 'princess')    ])
                          
def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [  ('number', 3),
                            ('number', 91234), ])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [  ('noun', 'bear'),
                            ('error', 'IAS'),
                            ('noun', 'princess')    ])              
                            
                            """

                