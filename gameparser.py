# List of "unimportant" words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list skip_words have been removed.
    For example:
    """

    return [word for word in words if word.lower() not in skip_words]

    
def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:
    """
    
    # ord() returns the unicode equivalent of a character
    # lower case a-z corresponds to values 97-122
    # so if ord(character) falls within that range, it is a valid character
    return "".join([char for char in text if 96 < ord(char.lower()) < 123 or char == " "])


def clean_whitespace(user_input):
    """This function is used to remove leading and trailing spaces from a string.
    It takes a string and returns a new string with does not have leading and
    trailing spaces. For example:
    """

    # str.split(s) splits a string into a list, seperating values at every occurance of s
    # splitting a string by " " gives us a new string for each word
    # consecutive whitespaces result in empty strings, which are removed
    # the final list can be joined with one whitespace between each word
    return " ".join([word for word in user_input.split(" ") if word != ""])


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:
    """

    return [word.lower() for word in filter_words(clean_whitespace(remove_punct(user_input)).split(" "), skip_words)]

"""
TESTED 18/10 15:02: PASSED

DOCTEST LOGS:

Trying:
    clean_whitespace("  Hello!  ")
Expecting:
    'Hello!'
ok
Trying:
    clean_whitespace("  Python  is  easy!   ")
Expecting:
    'Python is easy!'
ok
Trying:
    clean_whitespace("Python is easy!")
Expecting:
    'Python is easy!'
ok
Trying:
    clean_whitespace("")
Expecting:
    ''
ok
Trying:
    clean_whitespace("   ")
Expecting:
    ''
ok
Trying:
    filter_words(["help", "me", "please"], ["me", "please"])
Expecting:
    ['help']
ok
Trying:
    filter_words(["go", "south"], skip_words)
Expecting:
    ['go', 'south']
ok
Trying:
    filter_words(['how', 'about', 'i', 'go', 'through', 'that', 'little', 'passage', 'to', 'the', 'south'], skip_words)
Expecting:
    ['go', 'passage', 'south']
ok
Trying:
    normalise_input("  Go   south! ")
Expecting:
    ['go', 'south']
ok
Trying:
    normalise_input("!!!  tAkE,.    LAmp!?! ")
Expecting:
    ['take', 'lamp']
ok
Trying:
    normalise_input("HELP!!!!!!!")
Expecting:
    ['help']
ok
Trying:
    normalise_input("Now, drop the sword please.")
Expecting:
    ['drop', 'sword']
ok
Trying:
    normalise_input("Kill ~ tHe :-  gObLiN,. wiTH my SWORD!!!")
Expecting:
    ['kill', 'goblin', 'sword']
ok
Trying:
    normalise_input("I would like to drop my laptop here.")
Expecting:
    ['drop', 'laptop']
ok
Trying:
    normalise_input("I wish to take this large gem now!")
Expecting:
    ['take', 'gem']
ok
Trying:
    normalise_input("How about I go through that little passage to the south...")
Expecting:
    ['go', 'passage', 'south']
ok
Trying:
    remove_punct("Hello, World!")
Expecting:
    'Hello World'
ok
Trying:
    remove_punct("-- ...Hey! -- Yes?!...")
Expecting:
    ' Hey  Yes'
ok
Trying:
    remove_punct(",go!So.?uTh")
Expecting:
    'goSouTh'
ok
1 items had no tests:
    gameparser
4 items passed all tests:
   5 tests in gameparser.clean_whitespace
   3 tests in gameparser.filter_words
   8 tests in gameparser.normalise_input
   3 tests in gameparser.remove_punct
19 tests in 5 items.
19 passed and 0 failed.
Test passed.
"""