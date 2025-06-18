def change_language_to(language):
    with open("Core/language.txt", "w") as out_f:
        out_f.write(language)