from Preprocessing.src.Lexicon.letters import preprocess as preprocess_letters
from Preprocessing.src.Lexicon.word_ids import preprocess as preprocess_word_ids

def preprocess(language):
    letters_data = preprocess_letters(language)
    words_ids_data = preprocess_word_ids(language, letters_data)
    return combine(
        [
            letters_data,
            words_ids_data,
        ]
    )

def combine(dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result