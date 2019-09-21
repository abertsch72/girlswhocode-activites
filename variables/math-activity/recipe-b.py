"""
This program gives the user a chocolate chip recipe. To keep track of the ingredients, it
uses something called a "dictionary" -- that's the variable named base_ingredients. The
dictionary has values that map to other values. This dictionary maps ingredients to the
amount of each ingredient you want to use.

To get a value from a dictionary, you can index into it with [brackets] like a list!
Instead of giving a number of where the item you want is, you give it one of the values
before the colon, and it gives you back the value after the colon. These are the "key"
and its associated "value".

So, for base_ingredients, if I wanted to get the number of teaspoons of vanilla extract,
I could access that by typing
    base_ingredients["vanilla"]
"""


NUM_COOKIES_PER_RECIPE = 24

# TODO: ask the user how many cookies they want to make!
user_cookie_count = 24

base_ingredients = {"butter": 0.5, "sugar": 0.33, "brown sugar": 0.5, "eggs": 1, "vanilla": 1,
                    "baking soda": 0.5, "salt": 0.5, "flour": 1.5, "chocolate chips": 1.5}

print("Ingredients:\n")
print(str(base_ingredients["butter"]) + " cups unsalted butter, melted")
print(str(base_ingredients["sugar"]) + " cups granulated sugar")
print(str(base_ingredients["brown sugar"]) + " cups packed light brown sugar")
print(str(base_ingredients["eggs"]) + " large eggs")

# TODO: get the base values of each of these variables and put them in here
print(" teaspoons vanilla extract")
print(" teaspoons baking soda")
print(" teaspoon salt")
print(" cups all-purpose flour")
print(" chocolate chips (semi-sweet or milk)")

# TODO: now go back and try to scale the recipe so that the user makes the number of cookies they want!
print("Number of cookies made: " + str((base_ingredients["butter"] / 0.5) * 24))

## these instructions will be the same no matter how many cookies you make ##
instructions = "Instructions\n\nNote: This dough requires chilling.\nPlace melted butter in "  + \
               "the bowl of a stand mixer fitted with the paddle attachment (or a large bowl "  + \
               "if using a hand mixer). Add granulated and brown sugars and mix on low speed "  + \
               "until the mixture is smooth. Mix in egg and vanilla extract and mix on medium"  + \
               " speed until combined.\nMix in baking soda and salt, then slowly mix in flour"  + \
               " and mix just until the batter is smooth and comes together. Be sure to scrape" + \
               " the sides of the bowl during mixing. Slowly mix in chocolate chips.\nLine a "  + \
               "cookie sheet with a silicone baking mat or parchment paper. Scoop 2 tablespoon" + \
               " balls of dough onto the cookie sheet. Spacing doesn’t matter because you will" + \
               " be chilling the dough. Cover with plastic wrap and chill for at least 2 hours" + \
               ".\nPreheat oven to 350°F. Line a second cookie sheet with parchment paper or a" + \
               " silicone baking mat.\nRemove the chilled cookie dough balls from the "         + \
               "refrigerator and space them 2-inches apart on the cookie sheets. Bake "         + \
               "(2-tablespoon sized cookies) for 11-15 minutes, or until the edges are a light" + \
               " golden and the tops are no longer glossy. Let cool on the cookie sheets at "   + \
               "least 10 minutes before removing."

print(instructions)