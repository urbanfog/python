from translate import morse_dict

sentence = input('Enter the string to convert to morse code?\n').lower()

str_list = list(sentence)
morse_list = [morse_dict[ltr] for ltr in str_list]
morse_sentence = "  ".join(morse_list)
print(f"Your morse code for '{sentence}' is: {morse_sentence}\n")
