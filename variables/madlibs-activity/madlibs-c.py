"""
Nice work! But now let's think about related variables. If you glance
over madlibs-a or madlibs-b, you'll see that there are several
variables of each "category" -- adjectives, nouns, etc.

So what happens when you have multiple related variables?

You might want to put them into a list!

Lists in Python have [brackets] around values.
"""
emotions = ["happy", "sad", "angry", "frustrated", "glad"]
"""
You can index (access) any value by putting a number in brackets after 
the list name. The values (elements) in a list are numbered starting at 0.
"""
print(emotions[0])
"""
will print "happy" back.

Instead of asking the user for values, we can make lists of each type (like
a list of adjectives, or a list of colors) and pick random elements of
each list to print each time. Look at the adjectives for an example, and 
try adding to that list or making lists for the other types!

adjectives -- descriptive words, like "green" or "funny" or "large"
adverbs -- words describing verbs, like "quickly" or moodily" or "angrily"
nouns -- people, places, and things, like "my friend George" or "goats" or "Seattle"
"""
import random
adjectives = ["adorable", "amusing", "brainy", "calm", "determined", "enchanting",
              "fantastic"]
color = ""

number = ""

adverb = ""

plural_noun1 = ""
plural_noun2 = ""
plural_noun3 = ""

noun1 = ""
noun2 = ""
noun3 = ""
noun4 = ""

print("Dogs")
print("It has often been said that \"a dog is a man's best " + noun1 + ".\" ")
print("Dogs are very " + adjectives[random.randint(0, len(adjectives) - 1)] + " and can be taught many " +
      adjectives[random.randint(0, len(adjectives) - 1)] + " tricks.")
print("A dog can be trained to carry several " + plural_noun1 + " in his mouth. ")
print("And if you throw his " + plural_noun2 + ", he will run and fetch them. ")
print("Dogs will also bark " + adverb + " if someone tries to break into your " + noun2 + " during the night.")
print("One of the most popular canine pets today is the " + noun3 + " Spaniel.")
print("Spaniels have curly " + color + " coats and " + adjectives[random.randint(0, len(adjectives) - 1)] + " ears.")
print("They also have very " + adjectives[random.randint(0, len(adjectives) - 1)] + " dispositions and live to be " + number + " years old.")
print("Other popular dogs are " + adjectives[random.randint(0, len(adjectives) - 1)] + " Terriers, German " + plural_noun3 + ", and the "
      + adjectives[random.randint(0, len(adjectives) - 1)] + " Poodle.")
print("Every home should have a loyal dog for a " + noun4 + ".")


color = ""

adverb = ""

persons_name = ""

city = ""

plural_noun1 = ""
plural_noun2 = ""
plural_noun3 = ""
plural_noun4 = ""

plural_piece_of_clothing = ""

print("\nSpecial Spring Clothing Sale")
print(persons_name + " announced that their " + adjectives[random.randint(0, len(adjectives) - 1)] +
      " store in the heart of downtown " + city + " is having an " +
      adjectives[random.randint(0, len(adjectives) - 1)] + " sale of all merchandise, including " +
      adjectives[random.randint(0, len(adjectives) - 1)] +
      " suits and slightly irregular " + plural_piece_of_clothing + ".")
print("Men's cable-knit " + plural_noun1 + ", only $15.99. Hand-woven Italian " + plural_noun2 +
      ", half-price.")
print("Double-thick cashmere " + plural_noun3 + ", $50.00. Genuine imported " + color + " " +
      adjectives[random.randint(0, len(adjectives) - 1)] + " shoes, " +
      adjectives[random.randint(0, len(adjectives) - 1)] + " handkerchiefs, and women's embroidered " + plural_noun4 +
      ", all at rock-bottom prices. This is a chance to get some really " +
      adjectives[random.randint(0, len(adjectives) - 1)] + " bargains!")
