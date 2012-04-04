# lexicon.py

dictionary = {
    "north": "direction", 
    "south": "direction", 
    "east": "direction", 
    "west": "direction", 
    "go": "verb", 
    "kill": "verb", 
    "eat": "verb", 
    "the": "stop", 
    "in": "stop", 
    "off": "stop", 
    "bear": "noun", 
    "princess": "noun", 
    "raji" : "noun"
    }

def scan(words):
    """Scans the string of words and determines their types based on dictionary. 
    Return error if there is no match."""
    try:
        result = list()
        for word in (words.split()):
            if word.lower() in dictionary.keys():
                result.append( (dictionary[word.lower()], word) )
            elif word.isdigit():
                result.append( ( 'number', int(word) ) )
            else:
                result.append( ('error', word) )
        return result
    except ValueError:
        return None
    
"""    
Extra Credit
1. Improve the unit test to make sure you cover more of the lexicon. LATER
2. Add to the lexicon and then update the unit test. LATER
3. Make your scanner handles user input in any capitalization and case. 
   Update the test to make sure this actually works. OK
4. Find another way to convert the number. isdigit() ???
5. My solution was 37 lines long. Is yours longer? Shorter? shoter
"""