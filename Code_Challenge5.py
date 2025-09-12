print("Welcome to the Manga Recommender! ")
print("Answer a few questions to find your next read.")
genre = input("What genre do you like? (action, romance, horror): ")
length = input("How long should the manga be? (short, medium, long): ")
decade = input("What decade? (2000s, 2010s, 2020s): ")

if genre == "action":
    if length == "short" and decade == "2000s":
        print("Recommendation: Black Lagoon")
    elif length == "short" and decade == "2010s":
        print("Recommendation: Gangsta")
    elif length == "short" and decade == "2020s":
        print("Recommendation: Gleipnir")
    elif length == "medium" and decade == "2000s":
        print("Recommendation: Naruto")
    elif length == "long" and decade == "2000s":
        print("Recommendation: Bleach")
    elif length == "long" and decade == "2010s":
        print("Recommendation: One Punch Man")
    elif length == "long" and decade == "2020s":
        print("Recommendation: Chainsaw Man")
    else:
        print("Sorry, no action manga matches your selection.")

elif genre == "romance":
    if length == "short" and decade == "2010s":
        print("Recommendation: Violet Evergarden")
    elif length == "medium" and decade == "2020s":
        print("Recommendation: Kubo Won't Let Me Be Invisible")
    elif length == "medium" and decade == "2010s":
        print("Recommendation: Kimi ni Todoke")
    elif length == "long" and decade == "2010s":
        print("Recommendation: Domestic Girlfriend")
    elif length == "long" and decade == "2020s":
        print("Recommendation: The Quintessential Quintuplets")
    else:
        print("Sorry, no romance manga matches your selection.")

elif genre == "horror":
    if length == "short" and decade == "2000s":
        print("Recommendation: Another")
    elif length == "short" and decade == "2010s":
        print("Recommendation: I Am a Hero")
    elif length == "short" and decade == "2020s":
        print("Recommendation: Dandadan")
    elif length == "medium" and decade == "2010s":
        print("Recommendation: Tokyo Ghoul")
    elif length == "medium" and decade == "2020s":
        print("Recommendation: Kaiju No. 8")
    elif length == "long" and decade == "2010s":
        print("Recommendation: Ajin")
    elif length == "long" and decade == "2020s":
        print("Recommendation: Jujutsu Kaisen")
    else:
        print("Sorry, no horror manga matches your selection.")

else:
    print("Invalid genre. Please choose from 'action', 'romance', or 'horror'.")

if length not in ["short", "medium", "long"]:
    print("Invalid length. Please choose from 'short', 'medium', or 'long'.")

if decade not in ["2000s", "2010s", "2020s"]:

    print("Invalid decade. Please choose from '2000s', '2010s', or '2020s'.")



