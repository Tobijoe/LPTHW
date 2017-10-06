def break_words(stuff):
    """This function breaks up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and returns the words sorted"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """ prints the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts words and then prints first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
