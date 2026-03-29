def madlib():
    # Prompt the user for input
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")
    adverb2 = input("Enter another adverb: ")

    # Print the madlib story
    print(f"Once upon a time, there was a {adjective1} {noun1}.")
    print(f"It loved to {verb1} {adverb1} through the forest.")
    print(f"One day, it encountered a {adjective2} {noun2}.")
    print(f"The {noun2} challenged the {noun1} to {verb2} {adverb2}.")
    print(f"And so, the {adjective1} {noun1} and the {adjective2} {noun2} became best friends.")
    print("The end.")
