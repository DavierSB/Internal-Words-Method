import argparse
import importlib
import pickle

def precompute_and_save(module_name, language):
    module = importlib.import_module(f"Preprocessing.src.{module_name}.preprocessing")
    outputs = module.preprocess(language)
    for name, obj in outputs.items():
        with open(f"Preprocessing/Output/{language}/{module_name}/{name}.pickle", "wb") as out_f:
            pickle.dump(obj, out_f)

modules_to_precompute = [
    "Lexicon",
]

def main():
    #hyperparameter = 10
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--language')
    #parser.add_argument('-h', '--hyperparameter')
    language = parser.parse_args().language
    for module in modules_to_precompute:
        precompute_and_save(module, language)

if __name__ =="__main__":
    main()