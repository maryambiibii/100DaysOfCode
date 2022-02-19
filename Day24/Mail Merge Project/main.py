with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.readlines()

for name in names:
    stripped_name = name.strip()
    with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="a") as letter_to:
        for line in letter_template:
            sentence = line.replace("[name]", f"{stripped_name}")
            letter_to.write(sentence)
