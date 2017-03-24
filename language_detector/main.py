# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

'''

def detect_language(text, languages):
    """Returns the detected language of given text."""
    spanish = 0
    german = 0
    english = 0
    txt_lst = text.split()
    for word in txt_lst:
        if word in languages[0]['common_words']:
            spanish += 1
        elif word in languages[1]['common_words']:
            german += 1
        elif word in languages[2]['common_words']:
            english += 1

    if spanish > (german and english):
        return "Spanish"
    elif german > (spanish and english):
        return "German"
    else:
        return "English"
'''


def detect_language(text, languages):
    """Returns the detected language of given text."""
    from collections import defaultdict
    language_score = defaultdict(int)
    
    for word in text.split():
        for language in languages:
            if word.lower() in language['common_words']:
                language_score[language['name']] += 1
                
    return max(language_score, key=language_score.get)
    
    
