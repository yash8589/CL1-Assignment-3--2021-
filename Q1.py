# classes we are considering for word generators:
# print("classes we are considering for word generators:")
# print("Class 1 = play, walk, talk")
# print("Class 2 = dance, mince")
# print("Class 3 = marry, carry")

# verb analysis
inp = input("what are u entering? verb or noun: ")
print("")
if (inp == "verb" or inp == "Verb"):
    wrd = input("Enter the word: ")
    print("")
    print("Word forms:")

    if (wrd[-1] == "e" and wrd[-2] != "i"
            and wrd != "leave"):  # dance, mince, bake
        print(wrd)
        print(wrd + "s")
        print(wrd[:-1] + "ed")
        print(wrd[:-1] + "ed")
        print(wrd[:-1] + "ing")
    elif (wrd[-1] == "y" and wrd != "play"
          and wrd != "slay"):  # marry, carry, cry
        print(wrd)
        print(wrd[:-1] + "ies")
        print(wrd[:-1] + "ied")
        print(wrd[:-1] + "ied")
        print(wrd + "ing")
    elif (wrd[-1] == "c"):  # panic, mimic, frolic
        print(wrd)
        print(wrd + "s")
        print(wrd + "ked")
        print(wrd + "ked")
        print(wrd + "king")
    elif (wrd[-1] == "h"):  # catch, watch, crouch
        print(wrd)
        print(wrd + "es")
        print(wrd + "ed")
        print(wrd + "ed")
        print(wrd + "ing")
    elif (wrd[-2] == "i" and wrd[-1] == "e"):  # lie, die, tie
        print(wrd)
        print(wrd + "s")
        print(wrd + "d")
        print(wrd + "d")
        print(wrd[:-2] + "ying")

    else:  # play, walk, talk, slay
        print(wrd)
        print(wrd + "s")
        print(wrd + "ed")
        print(wrd + "ed")
        print(wrd + "ing")
else:  # noun handeling
    wrd = input("Enter the word: ")
    print("")
    print("Word forms:")
    if (wrd[-1] == "s" or (wrd[-1] == "h" and wrd[-2] == "c")
            or (wrd[-1] == "h" and wrd[-2] == "s") or wrd[-1] == "x"
            or wrd[-1] == "z"):  # branch, dish, Quiz
        print(wrd)
        print(wrd + "es")
    elif (wrd[-1] == "f"):  # calf, elf, half, leaf
        print(wrd)
        print(wrd[:-1] + "ves")
    elif (wrd[-1] == "e" and wrd[-2] == "f"):  # knife, life, wife
        print(wrd)
        print(wrd[:-2] + "ves")
    elif (wrd[-1] == "y"
          and (wrd[-2] == "a" or wrd[-2] == "e" or wrd[-2] == "i"
               or wrd[-2] == "o" or wrd[-2] == "u")):  # annoy, toy, boy
        print(wrd)
        print(wrd + "s")
    elif (wrd[-1] == "y"):  # baby, berry, bully, bunny
        print(wrd)
        print(wrd[:-1] + "ies")
    elif (wrd[-1] == "o"):  # hero, potato, tomato
        print(wrd)
        print(wrd + "es")
    elif (wrd[-1] == "n" and wrd[-2] == "o"):  # phenomenon, criterion
        print(wrd)
        print(wrd[:-2] + "a")
    else:  # cat, house
        print(wrd)
        print(wrd + "s")
