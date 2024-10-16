def mad_libs_game():
    story_template = (
        "Once upon a time in a {adjective} land, there lived a {noun}. "
        "Every day, the {noun} would {verb} in the {place}. "
        "One day, a {adjective} {noun} appeared and changed everything!"
    )

    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    place1 = input("Enter a place: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")

    completed_story = story_template.format(
        adjective=adjective1,
        noun=noun1,
        verb=verb1,
        place=place1
    )

    print("\nHere is your Mad Libs story:")
    print(completed_story)

mad_libs_game()
