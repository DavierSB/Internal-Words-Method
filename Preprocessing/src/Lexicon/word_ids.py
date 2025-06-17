import pickle
import bidict
import csv

def load_lexicon(lexicon_file):
    lexicon = set()
    with open(lexicon_file, "r") as in_f:
        for line in in_f:
            lexicon.add(line.strip())
    return lexicon

def preprocess(language, letters_data):
    lexicon_file = f"Preprocessing/Input/{language}/lexicon.txt"
    lexicon = load_lexicon(lexicon_file)
    word_ids = bidict.bidict()
    
    word_ids[""] = 0
    for letter, idx in letters_data.items():
        if letter == "#":
            continue
        word_ids[letter] = idx
    for word in sorted(lexicon, key= lambda word : (len(word), word)):
        word_ids[word] = len(word_ids)
    
    return {
        "word_ids" : word_ids,
    }