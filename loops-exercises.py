import random
# https://www.espressoenglish.net/100-common-adjectives-in-english/

adjectives = ["other", "new", "good", "high", "old", "great", "big", "American",
       "small", "large", "national", "young", "different", "black", "long",
       "little", "important", "political", "bad", "white", "real", "best",
       "right", "social", "only", "public", "sure", "low", "early", "able",
       "human", "local", "late", "hard", "major", "better", "economic",
       "strong", "possible", "whole", "free", "military", "true", "federal",
       "international", "full", "special", "easy", "clear", "recent",
       "certain", "personal", "open", "red", "difficult", "available",
       "likely", "short", "single", "medical", "current", "wrong", "private",
       "past", "foreign", "fine", "common", "poor", "natural", "significant",
       "similar", "hot", "dead", "central", "happy", "serious", "ready",
       "simple", "left", "physical", "general", "environmental", "financial",
       "blue", "democratic", "dark", "various", "entire", "close", "legal",
       "religious", "cold", "final", "main", "green", "nice", "huge",
       "popular", "traditional", "cultural"]

articles = ["the", "a", "an"]

# https://www.espressoenglish.net/100-common-nouns-in-english/
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman",
         "life", "child", "world", "school", "state", "family", "student",
         "group", "country", "problem", "hand", "part", "place", "case",
         "week", "company", "system", "program", "question", "work",
         "government", "number", "night", "point", "home", "water", "room",
         "mother", "area", "money", "story", "fact", "month", "lot", "right",
         "study", "book", "eye", "job", "word", "business", "issue", "side",
         "kind", "head", "house", "service", "friend", "father", "power",
         "hour", "game", "line", "end", "member", "law", "car", "city",
         "community", "name", "president", "team", "minute", "idea", "kid",
         "body", "information", "back", "parent", "face", "others", "level",
         "office", "door", "health", "person", "art", "war", "history",
         "party", "result", "change", "morning", "reason", "research", "girl",
         "guy", "moment", "air", "teacher", "force", "education"]

# https://www.espressoenglish.net/100-most-common-english-verbs/
verbs = ["be", "have", "do", "say", "go", "can", "get", "would", "make",
         "know", "will", "think", "take", "see", "come", "could", "want",
         "look", "use", "find", "give", "tell", "work", "may", "should",
         "call", "try", "ask", "need", "feel", "become", "leave", "put",
         "mean", "keep", "let", "begin", "seem", "help", "talk", "turn",
         "start", "might", "show", "hear", "play", "run", "move", "like",
         "live", "believe", "hold", "bring", "happen", "must", "write",
         "provide", "sit", "stand", "lose", "pay", "meet", "include",
         "continue", "set", "learn", "change", "lead", "understand", "watch",
         "follow", "stop", "create", "speak", "read", "allow", "add", "spend",
         "grow", "open", "walk", "win", "offer", "remember", "love",
         "consider", "appear", "buy", "wait", "serve", "die", "send", "expect",
         "build", "stay", "fall", "cut", "reach", "kill", "remain"]

print("Exercise 1")
for i in range(20):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    print(adjective + " " + noun)

print("\nExercise 2")
for i in range(20):
    art = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    print(art + " " + noun + " " + verb)

print("\nExercise 3")
combinations = list()
for art in articles:
    for noun in nouns:
        for verb in verbs:
            combinations.append(art + " " + noun + " " + verb)

print("All possible combinations: " + str(len(combinations)))
print("Here's a few of those combinations:")

for combination in range(10):
    print(random.choice(combinations))


print("\nExercise 1 in conditional statements")
for i in range(20):
    art = ""
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    if noun[0] in "aeiou":
        art = random.choice(articles[::len(articles)-1])
    else:
        art = articles[random.randint(0, 1)]
    print(art + " " + noun + " " + verb)
