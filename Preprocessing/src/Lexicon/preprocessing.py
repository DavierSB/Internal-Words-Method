from Preprocessing.src.Lexicon.letters import preprocess as preprocess_letters
from Preprocessing.src.Lexicon.word_ids import preprocess as preprocess_word_ids
from Preprocessing.src.Lexicon.word_raw_points import preprocess as preprocess_word_raw_points

def preprocess(language):
    data = preprocess_letters(language)
    data.update(preprocess_word_ids(language, data["letter_ids"]))
    data.update(preprocess_word_raw_points(data))
    return data