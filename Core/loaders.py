import pickle

with open("Core/language.txt", "r") as in_f:
    language = in_f.readline().strip()

to_load = {
    "Lexicon" : [
        "letter_ids",
        "letter_values",
        "letter_frequencies",
        "word_ids",
]
}

for module, all_data in to_load.items():
    for data in all_data:
        with open(f"Preprocessing/Output/{language}/{module}/{data}.pickle", "rb") as in_f:
            globals()[data] = pickle.load(in_f)