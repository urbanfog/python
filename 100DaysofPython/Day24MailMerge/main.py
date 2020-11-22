# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

clean_names = []

with open("Input/Names/invited_names.txt", mode="r") as names:
    list = names.readlines()
    for _ in list:
        clean_names.append(_.strip("\n"))

with open("Input/Letters/starting_letter.docx", mode="r") as letter:
    ltr = letter.read()
    for name in clean_names:
        with open(f"Output/ReadyToSend/{name}_letter.docx", mode="w") as named_letter:
            named_letter.write(ltr.replace("[name]", f"{name}"))
