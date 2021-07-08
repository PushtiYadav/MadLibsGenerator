"""Mad libs generator"""

loop = 1
while loop < 10:
    # All the questions asked to the user by the program
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a Place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")

    # Displays the story based on the user input
    print("_____________________________________")
    print("Be kind to your",noun,"- footed", p_noun)
    print("For a duck may be somebody's", noun2, ",")
    print("Be kind to your", p_noun, "in", place)
    print("Where the weather is always ", adjective, ".")
    print()
    print("You may think that is this the", noun3, ",")
    print("Well it is.")
    print("_________________________________________")
#     Loop back to loop=1
    loop += 1
