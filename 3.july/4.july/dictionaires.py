text = "Всем привет я я я я привет всем на тебе "
dictionairy = {}
for word in text.split:
    word = word.lower()
    if word in dictionairy:
        dictionairy[word] += 1
    else:
        dictionairy[word] = 1


for word, count in dictionairy.items():
    print(word, count)
