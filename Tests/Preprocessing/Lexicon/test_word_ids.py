from Core.change_language import change_language_to
from Core.loader import word_ids, letter_ids
import csv

language_features = {}
with open("supported_languages.csv", newline='') as in_f:
    reader = csv.DictReader(in_f)
    for row in reader:
        language = row['language']
        language_features[language] = {}
        language_features[language]["n_letters"] = int(row['n_letters'])
        language_features[language]["n_words"] = int(row['n_words'])            

def test_word_ids():
    for language in language_features:
        n_letters = language_features[language]["n_letters"]
        n_words = language_features[language]["n_words"]
        assert len(word_ids) == (1 + n_letters + n_words)
        assert (word_ids[""] == 0)
        assert (len(word_ids.inverse[1]) == 1)
        assert (len(word_ids.inverse[n_letters]) == 1)
        assert (len(word_ids.inverse[n_letters + 1]) == 2)
        assert (len(word_ids.inverse[n_words + n_letters - 1]) == 15)