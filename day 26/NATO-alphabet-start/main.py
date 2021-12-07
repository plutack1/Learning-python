import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter:row.code for (index, row) in
              nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("enter a word").upper()
result = {letter:code for (letter, code) in dictionary.items() if letter  in
          list(word)}
print(result)
