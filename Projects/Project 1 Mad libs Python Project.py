#Mad libs Python Project
def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks.\n")

    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ")
    verb_past = input("Enter a past-tense verb: ")
    noun = input("Enter a noun: ")

    story = f"""
    Today I went to the zoo and saw a(n) {adjective} {animal}.
    It was so exciting that I had to {verb}!
    Suddenly, I heard someone yell, "{exclamation}!"
    I turned around and {verb_past} into a {noun}.
    What a wild day!
    """

    print("\nHere's your story:")
    print(story)

mad_libs()
