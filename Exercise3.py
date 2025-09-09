# ------------------------------
# SIMPLE MAD LIBS GAME
# ------------------------------
# Mad Libs is a fun word game where the player provides words 
# (nouns, verbs, adjectives, etc.) to complete a story.

# Step 1: Take user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# Step 2: Create the story using f-string
story = f"""
Once upon a time, {name} went to {place}. 
It was a very {adjective} day. 
Suddenly, {name} saw a {noun} that wanted to {verb}. 
What an adventure!
"""

# Step 3: Print the story
print("\n--- Your Mad Libs Story ---")
print(story)
