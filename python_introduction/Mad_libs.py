names = ["Alex", "Bella", "Chris", "Diana"]
nouns = ["dragon", "spaceship", "pizza", "robot"]
verbs = ["dance", "scream", "invent", "explore"]
adjectives = ["scary", "funny", "shiny", "weird"]

print("Names")
for name in names:
    print(f"- {name}")

print("\nNouns")
for noun in nouns:
    print(f"- {noun}")

print("\nVerbs")
for verb in verbs:
    print(f"- {verb}")

print("\nAdjectives")
for adjective in adjectives:
    print(f"- {adjective}")

print("\nFrom the list above, choose one name, one verb, one noun, and one adjective.")

noun_input = input("Enter a noun: ")
verb_input = input("Enter a verb: ")
adjective_input = input("Enter an adjective: ")
name_input = input("Enter a name: ")

story = f"\nOne day, {name_input} found a {adjective_input} {noun_input} in their backyard."
print(story)

# Story depending on Noun

# noinspection PyUnreachableCode
match noun_input:
    case "dragon":
        print(f"Without thinking, {name_input} decided to {verb_input} with it, and suddenly it flew into the sky!")
    case "spaceship":
        print(f"It turned out to be a secret alien craft! {name_input} chose to {verb_input} aboard and travel to Mars.")
    case "pizza":
        print(f"It smelled delicious, but when {name_input} tried to {verb_input} it, it exploded with glitter!")
    case "robot":
        print(f"The robot started to {verb_input} uncontrollably, and {name_input} had to shut it down quickly.")
    case _:
        print(f"{name_input} didn't know what to do with the strange {noun_input}.")

# Story depending on Adjective

# noinspection PyUnreachableCode
match adjective_input:
    case "scary":
        print("Everyone in town ran away in fear!")
    case "funny":
        print("It made everyone laugh for hours!")
    case "shiny":
        print("People came from all over just to take pictures.")
    case "weird":
        print("No one could understand what it was doing.")
    case _:
        print("It left everyone confused.")

print("\n--- End of Story ---")
