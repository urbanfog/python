import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
df_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def nato_alfa():
    word = input("Enter a word: ").upper()
    try:
        word_alfa = {letter: df_dict[letter] for letter in word}
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_alfa()
    else:
        print(word_alfa)


nato_alfa()
