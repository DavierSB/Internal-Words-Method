import pickle
import bidict
import csv

def load_lexicon(lexicon_file):
    lexicon = set()
    with open(lexicon_file, "r") as in_f:
        for line in in_f:
            lexicon.add(line.strip())
    return lexicon

def load_letters(letters_file):
    letter_ids = bidict.bidict()
    letter_values = {}
    letter_frequencies = {}
    with open(letters_file, newline='') as in_f:
        reader = csv.DictReader(in_f)
        for row in reader:
            letter = row['letter']
            letter_ids[letter] = int(row['index'])
            letter_values[letter] = int(row['value'])
            letter_frequencies[letter] = int(row['frequency'])
    return letter_ids, letter_values, letter_frequencies

def preprocess(language):
    lexicon_file = f"Preprocessing/Input/{language}/lexicon.txt"
    letters_file = f"Preprocessing/Input/{language}/letters.csv"
    lexicon = load_lexicon(lexicon_file)
    letter_ids, letter_values, letter_frequencies = load_letters(letters_file)

    word_ids = bidict.bidict()
    word_ids[""] = 0
    for letter, idx in letter_ids.items():
        if letter == "#":
            continue
        word_ids[letter] = idx
    for word in sorted(lexicon, key= lambda word : (len(word), word)):
        word_ids[word] = len(word_ids)
    
    return {
        "letter_ids" : letter_ids,
        "letter_values" : letter_values,
        "letter_frequencies" : letter_frequencies,
        "word_ids" : word_ids,
    }