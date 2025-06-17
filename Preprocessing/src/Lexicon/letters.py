import pickle
import bidict
import csv

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
    letters_file = f"Preprocessing/Input/{language}/letters.csv"
    letter_ids, letter_values, letter_frequencies = load_letters(letters_file)

    return {
        "letter_ids" : letter_ids,
        "letter_values" : letter_values,
        "letter_frequencies" : letter_frequencies,
    }