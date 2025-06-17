import array

def raw_points(word, letter_values):
    return sum([letter_values[letter] for letter in word])

def preprocess(data):
    word_raw_points = array.array("B")
    word_ids = data["word_ids"]
    for idx in range(len(word_ids)):
        word = word_ids.inverse[idx]
        word_raw_points.append(raw_points(word, data["letter_values"]))
    return {
        "word_raw_points": word_raw_points,
    }